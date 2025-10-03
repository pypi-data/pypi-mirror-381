import copy
import gc
import glob
import logging
import multiprocessing as mp
import os
import re
import shutil
import warnings
from fnmatch import fnmatch
from functools import partial

import numpy as np
from jwst.assign_wcs.util import update_fits_wcsinfo
from stdatamodels.jwst import datamodels
from tqdm import tqdm
from tweakwcs.correctors import JWSTWCSCorrector

from ..utils import band_exts

log = logging.getLogger(__name__)


class ApplyWCSAdjustStep:
    def __init__(
            self,
            wcs_adjust,
            in_dir,
            out_dir,
            step_ext,
            procs,
            overwrite=False,
    ):
        """Apply WCS adjustments to images

        Args:
            wcs_adjust: Dictionary for WCS adjustments
            in_dir: Input directory
            out_dir: Output directory
            step_ext: .fits extension for the files going
                into the step
            procs: Number of processes to run in parallel
            overwrite: Whether to overwrite or not. Defaults
                to False
        """

        self.wcs_adjust = wcs_adjust
        self.in_dir = in_dir
        self.out_dir = out_dir
        self.step_ext = step_ext
        self.procs = procs
        self.overwrite = overwrite

    def do_step(self):
        """Run applying the WCS adjustments"""

        if self.overwrite:
            shutil.rmtree(self.out_dir)

        if not os.path.exists(self.out_dir):
            os.makedirs(self.out_dir)

        # Check if we've already run the step
        step_complete_file = os.path.join(
            self.out_dir,
            "apply_wcs_adjust_step_complete.txt",
        )
        if os.path.exists(step_complete_file):
            log.info("Step already run")
            return True

        files = glob.glob(
            os.path.join(
                self.in_dir,
                f"*_{self.step_ext}.fits",
            )
        )
        files.sort()

        # Ensure we're not wasting processes
        procs = np.nanmin([self.procs, len(files)])

        successes = self.run_step(
            files,
            procs=procs,
        )

        if not np.all(successes):
            log.warning("Failures detected in applying WCS adjustments")
            return False

        with open(step_complete_file, "w+") as f:
            f.close()

        return True

    def run_step(
            self,
            files,
            procs=1,
    ):
        """Wrap paralellism around applying WCS adjusts

        Args:
            files: List of files to mask lyot in
            procs: Number of parallel processes to run.
                Defaults to 1
        """

        log.info(f"Applying WCS corrections")

        with mp.get_context("fork").Pool(procs) as pool:
            successes = []

            for success in tqdm(
                    pool.imap_unordered(
                        partial(
                            self.parallel_wcs_adjust,
                        ),
                        files,
                    ),
                    ascii=True,
                    desc="Applying WCS corrections",
                    total=len(files),
            ):
                successes.append(success)

            pool.close()
            pool.join()
            gc.collect()

        return successes

    def parallel_wcs_adjust(
            self,
            file,
    ):
        """Parallelise applying WCS adjustments

        Args:
            file: File to apply WCS corrections to
        """

        file_short = os.path.split(file)[-1]

        output_file = os.path.join(
            self.out_dir,
            file_short,
        )

        # Set up the WCSCorrector per tweakreg
        with datamodels.open(file) as input_im:

            model_name = os.path.splitext(input_im.meta.filename)[0].strip('_- ')

            refang = input_im.meta.wcsinfo.instance
            im = JWSTWCSCorrector(
                wcs=input_im.meta.wcs,
                wcsinfo={'roll_ref': refang['roll_ref'],
                         'v2_ref': refang['v2_ref'],
                         'v3_ref': refang['v3_ref']},
                meta={'image_model': input_im,
                      'name': model_name},
            )

            # Check if we're NIRCam
            is_nircam = fnmatch(file_short, f"*{band_exts['nircam']}")

            # Pull out the info we need to shift. If we have both
            # dithers ungrouped and grouped, prefer the ungrouped
            # ones
            visit_grouped = file_short.split("_")[0]
            visit_ungrouped = "_".join(file_short.split("_")[:3])

            matrix = [[1, 0], [0, 1]]
            shift = [0, 0]

            visit_found = False
            for visit in [visit_ungrouped, visit_grouped]:
                if not visit_found:

                    adjust_found = False
                    for adjust in self.wcs_adjust["wcs_adjust"]:

                        if adjust_found:
                            continue

                        # If we have a degrouped NIRCam module adjust, then edit this to
                        # look more like the file name
                        adjust_is_nircam_degrouped = fnmatch(adjust, f"*{band_exts['nircam']}")
                        adjust_edit = copy.deepcopy(adjust)

                        # If we've got a degrouped adjust, then split off this bit
                        adjust_split = adjust.split("_")
                        if adjust_is_nircam_degrouped:
                            adjust_edit = "_".join(adjust_split[:-1])

                        # Now, check this against the visit, and if this doesn't match,
                        # continue
                        if not adjust_edit == visit:
                            continue

                        # If they're both NIRCam, then we care about the
                        # particular module
                        if adjust_is_nircam_degrouped and is_nircam:
                            adjust_module = re.findall("nrc([ab])",
                                                       adjust_split[-1]
                                                       )
                            if len(adjust_module) > 0:
                                adjust_module = adjust_module[0]

                            file_module = re.findall("nrc([ab])",
                                                     file_short
                                                     )
                            if len(file_module) > 0:
                                file_module = file_module[0]

                            if not adjust_module == file_module:
                                continue

                        wcs_adjust_vals = self.wcs_adjust["wcs_adjust"][adjust]

                        try:
                            matrix = wcs_adjust_vals["matrix"]
                        except KeyError:
                            matrix = [[1, 0], [0, 1]]

                        try:
                            shift = wcs_adjust_vals["shift"]
                        except KeyError:
                            shift = [0, 0]

                        adjust_found = True
                        visit_found = True

            if not visit_found:
                log.info(f"No shifts found for {file_short}. Will write out without shifting")

            if visit_found:

                im.set_correction(matrix=matrix, shift=shift)

                image_model = im.meta["image_model"]
                image_model.meta.wcs = im.wcs

                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    try:
                        update_fits_wcsinfo(
                            image_model,
                        )
                    except (ValueError, RuntimeError) as e:
                        log.warning(
                            "Failed to update 'meta.wcsinfo' with FITS SIP "
                            f"approximation. Reported error is:\n'{e.args[0]}'"
                        )

            else:

                image_model = copy.deepcopy(im.meta["image_model"])

            image_model.save(output_file)

        del input_im
        del image_model
        del im
        gc.collect()

        return True

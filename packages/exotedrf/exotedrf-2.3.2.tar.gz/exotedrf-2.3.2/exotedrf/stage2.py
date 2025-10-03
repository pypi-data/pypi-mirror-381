#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thurs Jul 21 17:33 2022

@author: MCR

Custom JWST DMS pipeline steps for Stage 2 (Spectroscopic processing).
"""

from astropy.io import fits
import bottleneck as bn
import copy
from functools import partial
import glob
import more_itertools as mit
import numpy as np
import os
import pandas as pd
from sklearn.decomposition import PCA
from scipy.interpolate import griddata
from scipy.ndimage import median_filter
from tqdm import tqdm
import warnings

from jwst import datamodels
import jwst.assign_wcs.nirspec
from jwst.pipeline import calwebb_spec2

import exotedrf.stage1 as stage1
from exotedrf import utils, plotting
from exotedrf.utils import fancyprint


class AssignWCSStep:
    """Wrapper around default calwebb_spec2 Assign WCS step.
    """

    def __init__(self, input_data, output_dir='./'):
        """Step initializer.

        Parameters
        ----------
        input_data : array-like(str), array-like(datamodel)
            List of paths to input data or the input data itself.
        output_dir : str
            Path to directory to which to save outputs.
        """

        # Set up easy attributes.
        self.tag = 'assignwcsstep.fits'
        self.output_dir = output_dir

        # Unpack input data files.
        self.datafiles = utils.sort_datamodels(input_data)
        self.fileroots = utils.get_filename_root(self.datafiles)

        # Get instrument.
        self.instrument = utils.get_instrument_name(self.datafiles[0])

    def run(self, save_results=True, force_redo=False, **kwargs):
        """Method to run the step.

        Parameters
        ----------
        save_results : bool
            If True, save results.
        force_redo : bool
            If True, run step even if output files are detected.
        kwargs : dict
            Keyword arguments for calwebb_spec2.assign_wcs_step.AssignWcsStep.

        Returns
        -------
        results : list(datamodel)
            Input data files processed through the step.
        """

        results = []
        all_files = glob.glob(self.output_dir + '*')
        for i, segment in enumerate(self.datafiles):
            # If an output file for this segment already exists, skip the step.
            expected_file = self.output_dir + self.fileroots[i] + self.tag
            if expected_file in all_files and force_redo is False:
                fancyprint('File {} already exists.'.format(expected_file))
                fancyprint('Skipping Assign WCS Step.')
                res = expected_file
            # If no output files are detected, run the step.
            else:
                if self.instrument == 'NIRSPEC':
                    jwst.assign_wcs.nirspec.nrs_wcs_set_input = partial(
                        jwst.assign_wcs.nirspec.nrs_wcs_set_input,
                        wavelength_range=[6e-08, 6e-06]
                    )
                    # Edit slit parameters so wavelength solution can be correctly calculated.
                    slit_y_low, slit_y_high = -50, 50
                else:
                    slit_y_low, slit_y_high = -0.55, 0.55
                step = calwebb_spec2.assign_wcs_step.AssignWcsStep()
                res = step.call(segment, output_dir=self.output_dir, save_results=save_results,
                                slit_y_low=slit_y_low, slit_y_high=slit_y_high, **kwargs)
                # Verify that filename is correct.
                if save_results is True:
                    current_name = self.output_dir + res.meta.filename
                    if expected_file != current_name:
                        res.close()
                        os.rename(current_name, expected_file)
                        thisfile = fits.open(expected_file)
                        thisfile[0].header['FILENAME'] = self.fileroots[i] + self.tag
                        thisfile.writeto(expected_file, overwrite=True)
                    res = expected_file
            results.append(res)

        return results


class Extract2DStep:
    """Wrapper around default calwebb_spec2 2D Extraction step.
    """

    def __init__(self, input_data, output_dir='./'):
        """Step initializer.

        Parameters
        ----------
        input_data : array-like(str), array-like(datamodel)
            List of paths to input data or the input data itself.
        output_dir : str
            Path to directory to which to save outputs.
        """

        # Set up easy attributes.
        self.tag = 'extract2dstep.fits'
        self.output_dir = output_dir

        # Unpack input data files.
        self.datafiles = utils.sort_datamodels(input_data)
        self.fileroots = utils.get_filename_root(self.datafiles)

        # Get instrument.
        self.instrument = utils.get_instrument_name(self.datafiles[0])

    def run(self, save_results=True, force_redo=False, **kwargs):
        """Method to run the step.

        Parameters
        ----------
        save_results : bool
            If True, save results.
        force_redo : bool
            If True, run step even if output files are detected.
        kwargs : dict
            Keyword arguments for calwebb_spec2.extract_2d_step.Extract2dStep.

        Returns
        -------
        results : list(datamodel)
            Input data files processed through the step.
        """

        # Only run for NIRSpec observations.
        if self.instrument != 'NIRSPEC':
            fancyprint('2D extraction only necessary for NIRSpec.')
            fancyprint('Skipping 2D Extraction Step.')
            return self.datafiles

        results = []
        all_files = glob.glob(self.output_dir + '*')
        for i, segment in enumerate(self.datafiles):
            # If an output file for this segment already exists, skip the step.
            expected_file = self.output_dir + self.fileroots[i] + self.tag
            if expected_file in all_files and force_redo is False:
                fancyprint('File {} already exists.'.format(expected_file))
                fancyprint('Skipping 2D Extraction Step.')
                res = expected_file
            # If no output files are detected, run the step.
            else:
                step = calwebb_spec2.extract_2d_step.Extract2dStep()
                res = step.call(segment, output_dir=self.output_dir,
                                save_results=save_results, **kwargs)
                # Verify that filename is correct.
                if save_results is True:
                    current_name = self.output_dir + res.meta.filename
                    if expected_file != current_name:
                        res.close()
                        os.rename(current_name, expected_file)
                        thisfile = fits.open(expected_file)
                        thisfile[0].header['FILENAME'] = self.fileroots[i] + self.tag
                        thisfile.writeto(expected_file, overwrite=True)
                    res = expected_file
            results.append(res)

        return results


class SourceTypeStep:
    """Wrapper around default calwebb_spec2 Source Type Determination step.
    """

    def __init__(self, input_data, output_dir='./'):
        """Step initializer.

        Parameters
        ----------
        input_data : array-like(str), array-like(datamodel)
            List of paths to input data or the input data itself.
        output_dir : str
            Path to directory to which to save outputs.
        """

        # Set up easy attributes.
        self.tag = 'sourcetypestep.fits'
        self.output_dir = output_dir

        # Unpack input data files.
        self.datafiles = utils.sort_datamodels(input_data)
        self.fileroots = utils.get_filename_root(self.datafiles)

    def run(self, save_results=True, force_redo=False, **kwargs):
        """Method to run the step.

        Parameters
        ----------
        save_results : bool
            If True, save results.
        force_redo : bool
            If True, run step even if output files are detected.
        kwargs : dict
            Keyword arguments for calwebb_spec2.srctype_step.SourceTypeStep.

        Returns
        -------
        results : list(datamodel)
            Input data files processed through the step.
        """

        results = []
        all_files = glob.glob(self.output_dir + '*')
        for i, segment in enumerate(self.datafiles):
            # If an output file for this segment already exists, skip the step.
            expected_file = self.output_dir + self.fileroots[i] + self.tag
            if expected_file in all_files and force_redo is False:
                fancyprint('File {} already exists.'.format(expected_file))
                fancyprint('Skipping Source Type Determination Step.')
                res = expected_file
            # If no output files are detected, run the step.
            else:
                step = calwebb_spec2.srctype_step.SourceTypeStep()
                res = step.call(segment, output_dir=self.output_dir, save_results=save_results,
                                **kwargs)
                # Verify that filename is correct.
                if save_results is True:
                    current_name = self.output_dir + res.meta.filename
                    if expected_file != current_name:
                        res.close()
                        os.rename(current_name, expected_file)
                        thisfile = fits.open(expected_file)
                        thisfile[0].header['FILENAME'] = self.fileroots[i] + self.tag
                        thisfile.writeto(expected_file, overwrite=True)
                    res = expected_file
            results.append(res)

        return results


class WaveCorrStep:
    """Wrapper around default calwebb_spec2 Wavelength Correction step.
    """

    def __init__(self, input_data, output_dir='./'):
        """Step initializer.

        Parameters
        ----------
        input_data : array-like(str), array-like(datamodel)
            List of paths to input data or the input data itself.
        output_dir : str
            Path to directory to which to save outputs.
        """

        # Set up easy attributes.
        self.tag = 'wavecorrstep.fits'
        self.output_dir = output_dir

        # Unpack input data files.
        self.datafiles = utils.sort_datamodels(input_data)
        self.fileroots = utils.get_filename_root(self.datafiles)

        # Get instrument.
        self.instrument = utils.get_instrument_name(self.datafiles[0])

    def run(self, save_results=True, force_redo=False, **kwargs):
        """Method to run the step.

        Parameters
        ----------
        save_results : bool
            If True, save results.
        force_redo : bool
            If True, run step even if output files are detected.
        kwargs : dict
            Keyword arguments for calwebb_spec2.wavecorr_step.WavecorrStep.

        Returns
        -------
        results : list(datamodel)
            Input data files processed through the step.
        """

        # Only run for NIRSpec observations.
        if self.instrument != 'NIRSPEC':
            fancyprint('Wavelength correction only necessary for NIRSpec.')
            fancyprint('Skipping Wavelength Correction Step.')
            return self.datafiles

        results = []
        all_files = glob.glob(self.output_dir + '*')
        for i, segment in enumerate(self.datafiles):
            # If an output file for this segment already exists, skip the step.
            expected_file = self.output_dir + self.fileroots[i] + self.tag
            if expected_file in all_files and force_redo is False:
                fancyprint('File {} already exists.'.format(expected_file))
                fancyprint('Skipping Wavelength Correction Step.')
                res = expected_file
            # If no output files are detected, run the step.
            else:
                step = calwebb_spec2.wavecorr_step.WavecorrStep()
                res = step.call(segment, output_dir=self.output_dir, save_results=save_results,
                                **kwargs)
                # Verify that filename is correct.
                if save_results is True:
                    current_name = self.output_dir + res.meta.filename
                    if expected_file != current_name:
                        res.close()
                        os.rename(current_name, expected_file)
                        thisfile = fits.open(expected_file)
                        thisfile[0].header['FILENAME'] = self.fileroots[i] + self.tag
                        thisfile.writeto(expected_file, overwrite=True)
                    res = expected_file
            results.append(res)

        return results


class BackgroundStep:
    """Wrapper around custom Background Subtraction step.
    """

    def __init__(self, input_data, baseline_ints=None, background_model=None, miri_method='median',
                 output_dir='./'):
        """Step initializer.

        Parameters
        ----------
        input_data : array-like(str), array-like(datamodel)
            List of paths to input data or the input data itself.
        baseline_ints : array-like(int)
            Integration number(s) to use as ingress and/or egress -- SOSS only.
        background_model : np.ndarray(float), str, None
            Model of background flux -- SOSS only.
        miri_method : str
            Method to calculate MIRI background; either 'median' or 'slope'.
        output_dir : str
            Path to directory to which to save outputs.
        """

        # Set up easy attributes.
        self.tag = 'backgroundstep.fits'
        self.baseline_ints = baseline_ints
        self.output_dir = output_dir

        # Unpack input data files.
        self.datafiles = utils.sort_datamodels(input_data)
        self.fileroots = utils.get_filename_root(self.datafiles)
        self.fileroot_noseg = utils.get_filename_root_noseg(self.fileroots)

        # Get instrument name.
        self.instrument = utils.get_instrument_name(self.datafiles[0])

        # Unpack background model.
        if self.instrument == 'NIRISS':
            msg = 'A background model must be provided to correct SOSS observations.'
            assert background_model is not None, msg
            if isinstance(background_model, str):
                fancyprint('Reading background model file: {}...'.format(background_model))
                self.background_model = np.load(background_model)
            elif (isinstance(background_model, np.ndarray) or
                  background_model is None):
                self.background_model = background_model
            else:
                raise ValueError('Invalid type for background model: {}'
                                 .format(type(background_model)))
            msg = 'Baseline integration must be provided for NIRISS obseravtions.'
            assert self.baseline_ints is not None, msg

        # For MIRI, save method.
        self.miri_method = miri_method

    def run(self, save_results=True, force_redo=False, do_plot=False, show_plot=False,
            miri_trace_width=20, miri_background_width=14, **kwargs):
        """Method to run the step.

        Parameters
        ----------
        save_results : bool
            If True, save results.
        force_redo : bool
            If True, run step even if output files are detected.
        do_plot : bool
            If True, do step diagnostic plot -- SOSS only.
        show_plot : bool
            If True, show the step diagnostic plot -- SOSS only.
        miri_trace_width : int
            Full width of the MIRI trace.
        miri_background_width : int
            Width of the MIRI background region.
        kwargs : dict
            Keyword arguments for stage2.backgroundstep.

        Returns
        -------
        results : list(datamodel)
            Input data files processed through the step.
        bkg_model : np.ndarray(float)
            Background model, scaled to the flux level of each group median.
        """

        # Warn user that datamodels will be returned if not saving results.
        if save_results is False:
            fancyprint('Setting "save_results=False" can be memory intensive.', msg_type='WARNING')

        fancyprint('BackgroundStep instance created.')

        all_files = glob.glob(self.output_dir + '*')
        results = []
        first_time = True
        for i, segment in enumerate(self.datafiles):
            # If an output file for this segment already exists, skip the step.
            expected_file = self.output_dir + self.fileroots[i] + self.tag
            expected_bkg = self.output_dir + self.fileroot_noseg + 'background.npy'
            if expected_file in all_files and force_redo is False:
                fancyprint('File {} already exists.'.format(expected_file))
                fancyprint('Skipping Background Subtraction Step.')
                res = expected_file
                if self.instrument == 'NIRISS':
                    bkg_model = expected_bkg
                else:
                    bkg_model = None
                # Do not do plots if skipping step.
                do_plot, show_plot = False, False
            # If no output files are detected, run the step.
            # This step is for both NIRISS and MIRI observations, though the functionalities are
            # very different. Split off here.
            else:
                if self.instrument == 'NIRISS':
                    # Generate some necessary quantities -- only do this for the first segment.
                    if first_time:
                        fancyprint('Creating reference deep stack.')
                        deepstack = utils.make_baseline_stack_general(datafiles=self.datafiles,
                                                                      baseline_ints=self.baseline_ints)
                        first_time = False

                    with warnings.catch_warnings():
                        warnings.filterwarnings('ignore')
                        step_results = backgroundstep_soss(datafile=segment,
                                                           background_model=self.background_model,
                                                           deepstack=deepstack,
                                                           output_dir=self.output_dir,
                                                           save_results=save_results,
                                                           fileroot=self.fileroots[i],
                                                           fileroot_noseg=self.fileroot_noseg,
                                                           **kwargs)
                        res, bkg_model = step_results
                else:
                    res = backgroundstep_miri(datafile=segment, trace_mask_width=miri_trace_width,
                                              background_width=miri_background_width,
                                              output_dir=self.output_dir, save_results=save_results,
                                              fileroot=self.fileroots[i], method=self.miri_method,
                                              **kwargs)
                    bkg_model = None
            results.append(res)

        # Do step plot if requested.
        if do_plot is True and self.instrument == 'NIRISS':
            if save_results is True:
                plot_file1 = self.output_dir + self.tag.replace('.fits', '_1.png')
                plot_file2 = self.output_dir + self.tag.replace('.fits', '_2.png')
            else:
                plot_file1 = None
                plot_file2 = None
            plotting.make_background_plot(results, outfile=plot_file1, show_plot=show_plot)
            plotting.make_background_row_plot(self.datafiles[0], results[0], bkg_model,
                                              outfile=plot_file2, show_plot=show_plot)

        fancyprint('Step BackgroundStep done.')

        return results, bkg_model


class FlatFieldStep:
    """Wrapper around default calwebb_spec2 Flat Field Correction step.
    """

    def __init__(self, input_data, output_dir='./'):
        """Step initializer.

        Parameters
        ----------
        input_data : array-like(str), array-like(datamodel)
            List of paths to input data or the input data itself.
        output_dir : str
            Path to directory to which to save outputs.
        """

        # Set up easy attributes.
        self.tag = 'flatfieldstep.fits'
        self.output_dir = output_dir

        # Unpack input data files.
        self.datafiles = utils.sort_datamodels(input_data)
        self.fileroots = utils.get_filename_root(self.datafiles)

    def run(self, save_results=True, force_redo=False, **kwargs):
        """Method to run the step.

        Parameters
        ----------
        save_results : bool
            If True, save results.
        force_redo : bool
            If True, run step even if output files are detected.
        kwargs : dict
            Keyword arguments for calwebb_spec2.flat_field_step.FlatFieldStep.

        Returns
        -------
        results : list(datamodel)
            Input data files processed through the step.
        """

        results = []
        all_files = glob.glob(self.output_dir + '*')
        for i, segment in enumerate(self.datafiles):
            # If an output file for this segment already exists, skip the step.
            expected_file = self.output_dir + self.fileroots[i] + self.tag
            if expected_file in all_files and force_redo is False:
                fancyprint('File {} already exists.'.format(expected_file))
                fancyprint('Skipping Flat Field Correction Step.')
                res = expected_file
            # If no output files are detected, run the step.
            else:
                step = calwebb_spec2.flat_field_step.FlatFieldStep()
                res = step.call(segment, output_dir=self.output_dir, save_results=save_results,
                                **kwargs)

                # From jwst v1.12.5-1.16.0, again STScI made a change to set DO_NOT_USE pixels to
                # NaNs when applying the flat field. Cosmetically interpolate these. Just as with
                # ramp fitting, this does not supercede any bad pixel interpolation later.
                nint, dimy, dimx = res.data.shape
                px, py = np.meshgrid(np.arange(dimx), np.arange(dimy))
                fancyprint('Doing cosmetic NaN interpolation.')
                for j in range(nint):
                    ii = np.where(np.isfinite(res.data[j]))
                    res.data[j] = griddata(ii, res.data[j][ii], (py, px), method='nearest')
                if save_results is True:
                    res.save(self.output_dir + res.meta.filename)

                # Verify that filename is correct.
                if save_results is True:
                    current_name = self.output_dir + res.meta.filename
                    if expected_file != current_name:
                        res.close()
                        os.rename(current_name, expected_file)
                        thisfile = fits.open(expected_file)
                        thisfile[0].header['FILENAME'] = self.fileroots[i] + self.tag
                        thisfile.writeto(expected_file, overwrite=True)
                    res = expected_file
            results.append(res)

        return results


class BadPixStep:
    """Wrapper around custom Bad Pixel Correction Step.
    """

    def __init__(self, input_data, baseline_ints, output_dir='./'):
        """Step initializer.

        Parameters
        ----------
        input_data : array-like(str), array-like(datamodel)
            List of paths to input data or the input data itself.
        baseline_ints : array-like(int)
            Integration number(s) to use as ingress and/or egress.
        output_dir : str
            Path to directory to which to save outputs.
        """

        # Set up easy attributes,
        self.tag = 'badpixstep.fits'
        self.output_dir = output_dir
        self.baseline_ints = baseline_ints

        # Unpack input data files.
        self.datafiles = utils.sort_datamodels(input_data)
        self.fileroots = utils.get_filename_root(self.datafiles)
        self.fileroot_noseg = utils.get_filename_root_noseg(self.fileroots)

        # Get instrument.
        self.instrument = utils.get_instrument_name(self.datafiles[0])

    def run(self, space_thresh=15, time_thresh=10, box_size=5, window_size=5, save_results=True,
            force_redo=False, do_plot=False, show_plot=False):
        """Method to run the step.

        Parameters
        ----------
        space_thresh : int
            Sigma threshold for a pixel to be flagged as an outlier spatially.
        time_thresh : int
            Sigma threshold for a pixel to be flagged as an outlier temporally.
        box_size : int
            Size of box around each pixel to test for spatial outliers.
        window_size : int
            Size of temporal window around each pixel to text for deviations. Must be odd.
        save_results : bool
            If True, save results.
        force_redo : bool
            If True, run step even if output files are detected.
        do_plot : bool
            If True, do step diagnostic plot.
        show_plot : bool
            If True, show the step diagnostic plot.

        Returns
        -------
        results : list(datamodel)
            Input data files processed through the step.
        """

        # Warn user that datamodels will be returned if not saving results.
        if save_results is False:
            fancyprint('Setting "save_results=False" can be memory intensive.', msg_type='WARNING')

        fancyprint('BadPixStep instance created.')

        all_files = glob.glob(self.output_dir + '*')
        results = []
        first_time = True
        for i, segment in enumerate(self.datafiles):
            # If an output file for this segment already exists, skip the step.
            expected_file = self.output_dir + self.fileroots[i] + self.tag
            if expected_file in all_files and force_redo is False:
                fancyprint('File {} already exists.'.format(expected_file))
                fancyprint('Skipping Bad Pixel Correction Step.')
                res = expected_file
                # Do not do plots if skipping step.
                do_plot, show_plot = False, False
            # If no output files are detected, run the step.
            else:
                # Generate some necessary quantities -- only do this for the first segment.
                if first_time:
                    fancyprint('Creating reference deep stack.')
                    deepstack = utils.make_baseline_stack_general(datafiles=self.datafiles,
                                                                  baseline_ints=self.baseline_ints)

                    to_flag = None  # No pixels yet identified to flag.
                    first_time = False

                step_results = badpixstep(segment, deepframe=deepstack, output_dir=self.output_dir,
                                          save_results=save_results, fileroot=self.fileroots[i],
                                          space_thresh=space_thresh, time_thresh=time_thresh,
                                          box_size=box_size, window_size=window_size,
                                          do_plot=do_plot, show_plot=show_plot, to_flag=to_flag)
                res, to_flag = step_results
            results.append(res)

        if save_results is True:
            # Save hot pixel mask.
            outfile = self.output_dir + self.fileroot_noseg + 'hot_pixels.npy'
            np.save(outfile, to_flag)
            fancyprint('Hot pixel map saved to file: {}.'.format(outfile))

        fancyprint('Step BadPixStep done.')

        return results


class PCAReconstructStep:
    """Wrapper around custom PCA Reconstruction Step.
    """

    def __init__(self, input_data, baseline_ints, output_dir='./'):
        """Step initializer.

        Parameters
        ----------
        input_data : array-like(str), array-like(datamodel)
            List of paths to input data or the input data itself.
        baseline_ints : array-like(int)
            Integration number(s) to use as ingress and/or egress.
        output_dir : str
            Path to directory to which to save outputs.
        """

        # Set up easy attributes.
        self.tag = 'pcareconstructstep.fits'
        self.output_dir = output_dir
        self.baseline_ints = baseline_ints

        # Unpack input data files.
        self.datafiles = utils.sort_datamodels(input_data)
        self.fileroots = utils.get_filename_root(self.datafiles)
        self.fileroot_noseg = utils.get_filename_root_noseg(self.fileroots)

    def run(self, pca_components=10, remove_components=None, skip_pca=False, save_results=True,
            do_plot=True, show_plot=False, force_redo=False):
        """Method to run the step.

        Parameters
        ----------
        pca_components : int
            Number of PCA components to fit.
        remove_components : list(int), None
            Indices of PCA components to remove from the reconstruction.
        skip_pca : bool
            If True, only generate the deep stack and don't do the PCA. Might be necessary for very
            large datasets.
        save_results : bool
            If True, save results to file.
        do_plot : bool
            If True, do the step diagnostic plot.
        show_plot : bool
            If True, show the step diagnostic plot instead of/in addition to saving it to file.
        force_redo : bool
            If True, run step even if output files are detected.

        Returns
        -------
        result : list(CubeModel), list(str)
            Input datamodels, after PCA reconstruction.
        deepstack : np.ndarray(float)
            Deep stack of the observation.
        """

        # Warn user that datamodels will be returned if not saving results.
        if save_results is False:
            fancyprint('Setting "save_results=False" can be memory intensive.', msg_type='WARNING')

        fancyprint('PCAReconstructStep instance created.')

        all_files = glob.glob(self.output_dir + '*')
        do_step, results = 1, []
        # The PCA needs to be run on the whole TSO simultaneously. So we need to check whether all
        # expected outputs are present, and if any are missing, then rerun.
        for i in range(len(self.datafiles)):
            expected_file = self.output_dir + self.fileroots[i] + self.tag
            expected_deep = self.output_dir + self.fileroot_noseg + 'deepframe.fits'
            # If an output is missing, then we need to re run.
            if expected_file not in all_files:
                do_step = 0
                break
            # If ouput is present add to return.
            else:
                if save_results is True:
                    results.append(expected_file)
                    deepstack = expected_deep
                else:
                    results.append(datamodels.open(expected_file))
                    deepstack = fits.getdata(expected_deep)
        if do_step == 1 and force_redo is False:
            fancyprint('Output files already exist.')
            fancyprint('Skipping PCA Reconstruction Step.')
            return results, deepstack

        # Run the step.
        if skip_pca is False:
            fancyprint('The PCA can be memory intensive, especially for large datasets.',
                       msg_type='WARNING')
            fancyprint('If you run into memory issues, the PCA component of this step can be '
                       'skipped by specifying skip_pca=True.', msg_type='WARNING')
            results = pcareconstructionstep(datafiles=self.datafiles,
                                            pca_components=pca_components,
                                            remove_components=remove_components,
                                            output_dir=self.output_dir, save_results=save_results,
                                            fileroot_noseg=self.fileroot_noseg,
                                            fileroots=self.fileroots, do_plot=do_plot,
                                            show_plot=show_plot)
        else:
            results = self.datafiles

        # Generate the final deep stack.
        fancyprint('Generating a deep stack for the TSO.')
        deepstack = utils.make_baseline_stack_general(self.datafiles, self.baseline_ints)

        if save_results is True:
            # Save deep frame.
            hdu = fits.PrimaryHDU(deepstack)
            hdul = fits.HDUList([hdu])
            outfile = self.output_dir + self.fileroot_noseg + 'deepframe.fits'
            hdul.writeto(outfile, overwrite=True)
            fancyprint('Deepframe saved to file: {}.'.format(outfile))
            deepstack = outfile

        fancyprint('Step PCAReconstructStep done.')

        return results, deepstack


class TracingStep:
    """Wrapper around custom Tracing Step.
    """

    def __init__(self, input_data, deepframe, output_dir='./', generate_order0_mask=False,
                 f277w=None, generate_lc=False, baseline_ints=None):
        """Step initializer.

        Parameters
        ----------
        input_data : array-like(str), array-like(datamodel)
            List of paths to input data or the input data itself.
        deepframe : str, np.ndarray(float)
            Path to observation deep frame or the deep frame itself.
        output_dir : str
            Path to directory to which to save outputs.
        generate_order0_mask : bool
            If True, generate a mask of background star order 0s using an
            F277W exposure. For SOSS observations only.
        f277w : str, np.ndarray(float)
            F277W exposure deepstack or path to a file containing one.
        generate_lc : bool
            If True, generate an estimate of the order 1 white light curve. For SOSS observations
            only.
        baseline_ints : array-like(int), None
            Integration number(s) to use as ingress and/or egress. Only necessary if generate_lc
            is True.
        """

        # Set up easy attributes.
        self.output_dir = output_dir
        self.baseline_ints = baseline_ints

        # Set toggles for functionalities.
        self.generate_order0_mask = generate_order0_mask
        self.generate_lc = generate_lc

        # Unpack input data files.
        self.datafiles = utils.sort_datamodels(input_data)
        self.fileroots = utils.get_filename_root(self.datafiles)
        self.fileroot_noseg = utils.get_filename_root_noseg(self.fileroots)

        # Unpack deepframe.
        if isinstance(deepframe, str):
            fancyprint('Reading deepframe file: {}...'.format(deepframe))
            self.deepframe = fits.getdata(deepframe)
        elif isinstance(deepframe, np.ndarray) or deepframe is None:
            self.deepframe = deepframe
        else:
            msg = 'Invalid type for deepframe: {}'.format(type(deepframe))
            raise ValueError(msg)

        # Unpack F277W exposure.
        if isinstance(f277w, str):
            fancyprint('Reading F277W exposure file: {}...'.format(f277w))
            self.f277w = np.load(f277w)
        elif isinstance(f277w, np.ndarray) or f277w is None:
            self.f277w = f277w
        else:
            msg = 'Invalid type for f277w: {}'.format(type(f277w))
            raise ValueError(msg)

        # Get instrument.
        self.instrument = utils.get_instrument_name(self.datafiles[0])
        if self.instrument != 'NIRISS':
            if generate_order0_mask is True:
                fancyprint('generate_order0_mask is set to True, but mode is not NIRISS/SOSS. '
                           'Ignoring generate_order0_mask.', msg_type='WARNING')
                self.generate_order0_mask = False
            if generate_lc is True:
                fancyprint('generate_lc is set to True, but mode is not NIRISS/SOSS. Ignoring '
                           'generate_lc.', msg_type='WARNING')
                self.generate_lc = False

    def run(self, pixel_flags=None, save_results=True, force_redo=False, smoothing_scale=None,
            do_plot=False, show_plot=False, allow_miri_slope=False):
        """Method to run the step.

        Parameters
        ----------
        pixel_flags : array-like(str), None
            Paths to files containing existing pixel flags to which the order 0 mask should be
            added. Only necesssary if generate_order0_mask is True.
        save_results : bool
            If True, save results.
        force_redo : bool
            If True, run step even if output files are detected.
        smoothing_scale : int, None
            Timescale on which to smooth light curve estimate. Only necessary if generate_lc is
            True.
        do_plot : bool
            If True, do step diagnostic plot.
        show_plot : bool
            If True, show the step diagnostic plot.
        allow_miri_slope : bool
            If True, allow the MIRI centroids to be sloped.

        Returns
        -------
        centroids : np.ndarray(float), str
            Trace centroids for all orders or path to centroids file.
        """

        fancyprint('TracingStep instance created.')

        all_files = glob.glob(self.output_dir + '*')
        # If an output file for this segment already exists, skip the step.
        suffix = 'centroids.csv'
        expected_file = self.output_dir + self.fileroot_noseg + suffix
        if expected_file in all_files and force_redo is False:
            fancyprint('Main output file already exists.')
            fancyprint('If you wish to still produce secondary outputs, run with force_redo=True.')
            fancyprint('Skipping Tracing Step.')
            centroids = expected_file
        # If no output files are detected, run the step.
        else:
            centroids = tracingstep(datafiles=self.datafiles, deepframe=self.deepframe,
                                    pixel_flags=pixel_flags, baseline_ints=self.baseline_ints,
                                    generate_order0_mask=self.generate_order0_mask,
                                    f277w=self.f277w, generate_lc=self.generate_lc,
                                    smoothing_scale=smoothing_scale, output_dir=self.output_dir,
                                    save_results=save_results, fileroot_noseg=self.fileroot_noseg,
                                    do_plot=do_plot, show_plot=show_plot,
                                    allow_miri_slope=allow_miri_slope)

        fancyprint('Step TracingStep done.')

        return centroids


def backgroundstep_miri(datafile, trace_mask_width=20, background_width=14, method='slope',
                        output_dir='./', save_results=True, fileroot=None):
    fancyprint('Starting MIRI background subtraction step.')

    # Output directory formatting.
    if output_dir is not None:
        if output_dir[-1] != '/':
            output_dir += '/'

    # Load in data.
    if isinstance(datafile, str):
        cube = fits.getdata(datafile, 1)
        filename = datafile
    else:
        with utils.open_filetype(datafile) as currentfile:
            cube = currentfile.data
            filename = currentfile.meta.filename
    fancyprint('Processing file: {}.'.format(filename))

    trace_halfwidth = int(trace_mask_width / 2)
    fancyprint('Starting background subtraction using the {} method'.format(method))
    # Knowing that the MIRI trace is centered more or less on pixel column 36.
    # Create a cube with only the background columns and median over each row.
    if method == 'median':
        # Construct the cube of background columns.
        bkg_cube = np.concatenate(
            [cube[:, :, (36 - trace_halfwidth - background_width):(36 - trace_halfwidth + 1)],
             cube[:, :, (36 + trace_halfwidth):(36 + trace_halfwidth + background_width + 1)]],
            axis=2)
        # Median over this cube and subtract the background level.
        bkg = np.nanmedian(bkg_cube, axis=2)
        cube_corr = cube - bkg[:, :, None]
    # Or fit a slope to the background region.
    elif method == 'slope':
        nint, dimy, dimx = np.shape(cube)
        bkg_cube, bkg = np.copy(cube), np.zeros_like(cube)
        # Mask out the frame edge columns and the trace.
        bkg_cube[:, :, :(36 - trace_halfwidth - background_width + 1)] = np.nan
        bkg_cube[:, :, (36 + trace_halfwidth + background_width):] = np.nan
        bkg_cube[:, :, (36 - trace_halfwidth):(36 + trace_halfwidth + 1)] = np.nan
        # Loop over all integrations and rows and fit a slope to the unmasked background columns.
        xx = np.arange(dimx)
        for i in tqdm(range(nint)):
            for j in range(dimy):
                pp = utils.robust_polyfit(xx, bkg_cube[i, j], order=1)
                bkg[i, j] = np.polyval(pp, xx)
        # Subtract off the background
        cube_corr = cube - bkg
    else:
        raise ValueError('Unknown method: {}.'.format(method))

    # Save interpolated data.
    if save_results is True:
        # Open input file and subtract background from data
        thisfile = fits.open(datafile)
        thisfile[1].data = cube_corr
        # Save corrected data.
        result = output_dir + fileroot + 'backgroundstep.fits'
        thisfile[0].header['FILENAME'] = fileroot + 'backgroundstep.fits'
        thisfile.writeto(result, overwrite=True)
        fancyprint('File saved to: {}.'.format(result))
    # If not saving results, need to work in datamodels to not break interoperability with stsci
    # pipeline.
    else:
        currentfile = utils.open_filetype(datafile)
        result = copy.deepcopy(currentfile)
        result.data = cube - bkg[:, :, None]

    return result


def backgroundstep_soss(datafile, background_model, deepstack, output_dir='./', save_results=True,
                        fileroot=None, fileroot_noseg='', scale1=None, background_coords1=None,
                        scale2=None, background_coords2=None, differential=False):
    """Background subtraction must be carefully treated with SOSS observations. Due to the extent
    of the PSF wings, there are very few, if any, non-illuminated pixels to serve as a sky region.
    Furthermore, the zodi background has a unique stepped shape, which would render a constant
    background subtraction ill-advised. Therefore, a background subtracton is performed by scaling
    a model background to the counts level of a median stack of the exposure. This scaled model
    background is then subtracted from each integration.

    Parameters
    ----------
    datafile : str, RampModel, CubeModel
        Data segment for a SOSS exposure, or path to one.
    background_model : array-like(float)
        Background model. Should be 2D (dimy, dimx)
    deepstack : array-like[float]
        Median stack of the baseline integrations.
    output_dir : str
        Directory to which to save outputs.
    save_results : bool
        If True, save outputs to file.
    fileroot : str
        Root name for output files.
    fileroot_noseg : str
        Root name with no segment information.
    scale1 : float, array-like(float), None
        Scaling value to apply to background model to match data. Will take precedence over
        calculated scaling value. If applied at group level, length of scaling array must equal
        ngroup.
    background_coords1 : array-like(int), None
        Region of frame to use to estimate the background. Must be 1D: [x_low, x_up, y_low, y_up].
    scale2 : float, array-like(float), None
        Scaling value to apply to background model to match post-step data. Will take precedence
        over calculated scaling value. If applied at group level, length of scaling array must
        equal ngroup.
    background_coords2 : array-like(int), None
        Region of frame to use to estimate the post-step background. Must be 1D:
        [x_low, x_up, y_low, y_up].
    differential : bool
        if True, calculate the background scaling seperately for the pre- and post-step frame.

    Returns
    -------
    result : CubeModel
        Input data segment, corrected for the background.
    model_scaled : np.ndarray(float)
        Background model, scaled to the flux level of each group median.
    """

    fancyprint('Starting SOSS background subtraction step.')
    if isinstance(datafile, str):
        filename = datafile
    else:
        with utils.open_filetype(datafile) as thisfile:
            filename = thisfile.meta.filename
    fancyprint('Processing file: {}.'.format(filename))

    # Output directory formatting.
    if output_dir is not None:
        if output_dir[-1] != '/':
            output_dir += '/'

    # If applied at the integration level, reshape median stack to 3D.
    if np.ndim(deepstack) != 3:
        dimy, dimx = np.shape(deepstack)
        deepstack = deepstack.reshape(1, dimy, dimx)
    ngroup, dimy, dimx = np.shape(deepstack)
    # Ensure if user-defined scalings are provided that there is one per group.
    if scale1 is not None:
        scale1 = np.atleast_1d(scale1)
        assert len(scale1) == ngroup
    if scale2 is not None:
        scale2 = np.atleast_1d(scale2)
        assert len(scale2) == ngroup

    fancyprint('Calculating background model scaling.')
    model_scaled = np.zeros_like(deepstack)
    shifts = np.zeros(ngroup)
    for i in range(ngroup):
        if scale1 is None:
            if background_coords1 is None:
                # If region to estimate background is not provided, use a
                # default region.
                if dimy == 96:
                    # Use area in bottom left corner for SUBSTRIP96.
                    xl, xu = 5, 21
                    yl, yu = 5, 401
                else:
                    # Use area in the top left corner for SUBSTRIP256
                    xl, xu = 230, 250
                    yl, yu = 350, 550
            else:
                # Use user-defined background scaling region.
                assert len(background_coords1) == 4
                # Convert to int if not already.
                background_coords1 = np.array(background_coords1).astype(int)
                xl, xu, yl, yu = background_coords1
            scale_factor1 = -1000
            while scale_factor1 < 0:
                bkg_ratio = ((deepstack[i, xl:xu, yl:yu] + shifts[i]) /
                             background_model[xl:xu, yl:yu])
                # Instead of a straight median, use the median of the 2nd quartile to limit the
                # effect of any remaining illuminated pixels.
                q1 = np.nanpercentile(bkg_ratio, 25)
                q2 = np.nanpercentile(bkg_ratio, 50)
                ii = np.where((bkg_ratio > q1) & (bkg_ratio < q2))
                scale_factor1 = np.nanmedian(bkg_ratio[ii])
                if scale_factor1 < 0:
                    shifts[i] -= (scale_factor1 * np.median(background_model[xl:xu, yl:yu]))
        else:
            scale_factor1 = scale1[i]

        # Repeat for post-jump scaling if necessary
        if scale2 is None and differential is True:
            if background_coords2 is None:
                # If region to estimate background is not provided, use a default region.
                if dimy == 96:
                    raise NotImplementedError
                else:
                    xl, xu = 235, 250
                    yl, yu = 715, 750
            else:
                # Use user-defined background scaling region.
                assert len(background_coords2) == 4
                # Convert to int if not already.
                background_coords2 = np.array(background_coords2).astype(int)
                xl, xu, yl, yu = background_coords2
            bkg_ratio = ((deepstack[i, xl:xu, yl:yu] + shifts[i]) / background_model[xl:xu, yl:yu])
            # Instead of a straight median, use the median of the 2nd quartile to limit the effect
            # of any remaining illuminated pixels.
            q1 = np.nanpercentile(bkg_ratio, 25)
            q2 = np.nanpercentile(bkg_ratio, 50)
            ii = np.where((bkg_ratio > q1) & (bkg_ratio < q2))
            scale_factor2 = np.nanmedian(bkg_ratio[ii])
            if scale_factor2 < 0:
                scale_factor2 = 0
        elif scale2 is not None and differential is True:
            scale_factor2 = scale2[i]
        else:
            scale_factor2 = scale_factor1

        # Apply scaling to background model.
        if differential is True:
            fancyprint('Using differential background scale factors: {0:.5f}, {1:.5f}, and shift: '
                       '{2:.5f}'.format(scale_factor1, scale_factor2, shifts[i]))
            # Locate background step.
            grad_bkg = np.gradient(background_model, axis=1)
            step_pos = np.argmax(grad_bkg[:, 10:-10], axis=1) + 10 - 4
            # Apply differential scaling to either side of step.
            for j in range(256):
                model_scaled[i, j, :step_pos[j]] = (background_model[j, :step_pos[j]] *
                                                    scale_factor1 - shifts[i])
                model_scaled[i, j, step_pos[j]:] = (background_model[j, step_pos[j]:] *
                                                    scale_factor2 - shifts[i])
        else:
            fancyprint('Using background scale factor: {0:.5f}, and shift: '
                       '{1:.5f}'.format(scale_factor1, shifts[i]))
            model_scaled[i] = background_model * scale_factor1 - shifts[i]

    # Subtract the background from the input segment.
    if save_results is True:
        # Open input file and subtract background from data
        thisfile = fits.open(datafile)
        thisfile[1].data -= model_scaled
        # Save corrected data.
        result = output_dir + fileroot + 'backgroundstep.fits'
        thisfile[0].header['FILENAME'] = fileroot + 'backgroundstep.fits'
        thisfile.writeto(result, overwrite=True)
        fancyprint('File saved to: {}.'.format(result))
        # Also save the scaled background.
        bkg_file = output_dir + fileroot_noseg + 'background.npy'
        np.save(bkg_file, model_scaled)
        fancyprint('Background model saved to {}.'.format(bkg_file))
    # If not saving results, need to work in datamodels to not break interoperability with stsci
    # pipeline.
    else:
        currentfile = utils.open_filetype(datafile)
        result = copy.deepcopy(currentfile)
        # Subtract the scaled background model.
        data_backsub = result.data - model_scaled
        result.data = data_backsub

    return result, model_scaled


def badpixstep(datafile, deepframe, space_thresh=15, time_thresh=10, box_size=5, window_size=5,
               output_dir='./', save_results=True, fileroot=None, do_plot=False, show_plot=False,
               to_flag=None):
    """Identify and correct outlier pixels remaining in the dataset, using both a spatial and
    temporal approach. First, find spatial outlier pixels in the median stack and correct them in
    each integration via the median of a box of surrounding pixels. Then flag outlier pixels in the
    temporal direction and again replace with the surrounding median in time.

    Parameters
    ----------
    datafile : RampModel, str
        Datamodel for a segment of the TSO, or path to one.
    deepframe : array-like(float)
        Median stack of baseline integrations.
    space_thresh : int
        Sigma threshold for a deviant pixel to be flagged spatially.
    time_thresh : int
        Sigma threshold for a deviant pixel to be flagged temporally.
    box_size : int
        Size of box around each pixel to test for deviations.
    window_size : int
        Size of temporal window around each pixel to text for deviations.
        Must be odd.
    output_dir : str
        Directory to which to output results.
    save_results : bool
        If True, save results to file.
    fileroot : str, None
        Root names for output files.
    do_plot : bool
        If True, do the step diagnostic plot.
    show_plot : bool
        If True, show the step diagnostic plot instead of/in addition to saving it to file.
    to_flag : array-like(int)
        Map of pixels to interpolate.

    Returns
    -------
    result : CubeModel, str
        Input datamodel, corrected for outlier pixels.
    badpix : ndarray(int)
        Map of pixels in the deepframe to interpolate.
    """

    fancyprint('Starting outlier pixel interpolation step.')

    # Output directory formatting.
    if output_dir is not None:
        if output_dir[-1] != '/':
            output_dir += '/'

    # Load in data.
    if isinstance(datafile, str):
        cube = fits.getdata(datafile, 1)
        err_cube = fits.getdata(datafile, 2)
        dq_cube = fits.getdata(datafile, 3)
        filename = datafile
    else:
        with utils.open_filetype(datafile) as currentfile:
            cube = currentfile.data
            err_cube = currentfile.err
            dq_cube = currentfile.dq
            filename = currentfile.meta.filename
    fancyprint('Processing file: {}.'.format(filename))

    # Initialize starting loop variables.
    newdata = np.copy(cube)
    newdq = np.copy(dq_cube)
    nint, dimy, dimx = np.shape(newdata)

    # ===== Spatial Outlier Flagging ======
    fancyprint('Starting spatial outlier flagging...')
    instrument = utils.get_instrument_name(datafile)

    # Set detector Y-axis limits.
    if instrument == 'NIRISS':
        ymax = dimy - 5
        ybox_size = 0
        xbox_size = box_size
    elif instrument == 'NIRSPEC':
        ymax = dimy
        ybox_size = 0
        xbox_size = box_size
    else:
        ymax = dimy
        ybox_size = box_size
        xbox_size = 0

    # For MIRI, we don't want to do the spatial flagging as it tends to flag the peak of the trace
    # itself and is of limited value picking out other potentially bad pixels.
    # We'll still interpolate known DO_NOT_USE or other bad pixels, but we won't flag any more. So
    # set the space threshold to an arbitrarily high value.
    if instrument == 'MIRI':
        space_thresh = int(1e6)

    # Find locations of bad pixels in the deep frame.
    if to_flag is None:
        # Initialize storage arrays.
        hotpix = np.zeros_like(deepframe)
        nanpix = np.zeros_like(deepframe)
        otherpix = np.zeros_like(deepframe)

        # Set all negatives to zero.
        newdata[newdata < 0] = 0
        # Get locations of all hot pixels.
        hot_pix = utils.get_dq_flag_metrics(dq_cube[10], ['HOT', 'WARM', 'DO_NOT_USE'])

        # Loop over whole deepstack and flag deviant pixels.
        for i in tqdm(range(5, dimx - 5)):
            for j in range(ymax):
                # If the pixel is known to be hot, add it to list to interpolate.
                if hot_pix[j, i]:
                    hotpix[j, i] = 1
                # If not already flagged, double check that the pixel isn't deviant in some other
                # manner.
                else:
                    xbox_size_i = box_size
                    box_prop = utils.get_interp_box(deepframe, xbox_size_i, ybox_size, i, j)
                    # Ensure that the median and std dev extracted are good.
                    # If not, increase the box size until they are.
                    while np.any(np.isnan(box_prop)):
                        xbox_size_i += 1
                        box_prop = utils.get_interp_box(deepframe, xbox_size_i, ybox_size, i, j)
                    med, std = box_prop[0], box_prop[1]

                    # If central pixel is too deviant (or nan) flag it.
                    if np.isnan(deepframe[j, i]):
                        nanpix[j, i] = 1
                    elif np.abs(deepframe[j, i] - med) >= (space_thresh * std):
                        otherpix[j, i] = 1

        # Combine all flagged pixel maps.
        badpix = (hotpix.astype(bool) | nanpix.astype(bool) |
                  otherpix.astype(bool))
        badpix = badpix.astype(int)
        fancyprint('{0} hot, {1} nan, and {2} deviant pixels identified.'
                   .format(int(np.sum(hotpix)), int(np.sum(nanpix)), int(np.sum(otherpix))))

    # If a bad pixel map is passed, just use that.
    else:
        fancyprint('Using passed bad pixel map.')
        badpix = to_flag

    # Replace the flagged pixels in each integration.
    fancyprint('Doing pixel replacement...')
    for i in tqdm(range(nint)):
        newdata[i], thisdq = utils.do_replacement(newdata[i], badpix, dq=np.ones_like(newdata[i]),
                                                  xbox_size=xbox_size, ybox_size=ybox_size)
        # Set DQ flags for these pixels to zero (use the pixel).
        thisdq = ~thisdq.astype(bool)
        newdq[:, thisdq] = 0

    # ===== Temporal Outlier Flagging =====
    fancyprint('Starting temporal outlier flagging...')
    # Median filter the data.
    cube_filt = median_filter(newdata, (window_size, 1, 1))
    if instrument == 'NIRISS':
        cube_filt[:2] = np.median(cube_filt[2:7], axis=0)
        cube_filt[-2:] = np.median(cube_filt[-8:-3], axis=0)
    else:
        cube_filt[:5] = np.median(cube_filt[5:15], axis=0)
        cube_filt[-5:] = np.median(cube_filt[-16:-6], axis=0)
    # Check along the time axis for outlier pixels.
    std_dev = bn.nanmedian(np.abs(0.5*(newdata[0:-2] + newdata[2:]) - newdata[1:-1]), axis=0)
    std_dev = np.where(std_dev == 0, np.nanmedian(std_dev), std_dev)
    scale = np.abs(newdata - cube_filt) / std_dev
    ii = np.where((scale > time_thresh))
    fancyprint('{} outliers detected.'.format(len(ii[0])))
    # Replace the flagged pixels in each integration.
    fancyprint('Doing pixel replacement...')
    newdata[ii] = cube_filt[ii]
    newdq[ii] = 0

    # Lastly, do a final check for any remaining invalid flux or error values.
    ii = np.where(np.isnan(newdata))
    newdata[ii] = cube_filt[ii]
    ii = np.where(np.isnan(err_cube))
    err_cube[ii] = np.nanmedian(err_cube)
    # And replace any negatives with zeros.
    newdata[newdata < 0] = 0
    newdata[np.isnan(newdata)] = 0

    # Egregious hack...don't ask.
    if instrument == 'NIRISS':
        # Get of pixels where an artifact intersects the order 1 trace edge are just never
        # corrected properly and I don't know why. So manual interpolation...
        mm = np.nanmedian(np.concatenate([newdata[:, 82:84, 2018:], newdata[:, 88:90, 2018:]],
                                         axis=1), axis=1)
        newdata[:, 84:88, 2018:] = mm[:, None, :]

    # Replace NIRISS reference pixels with 0s.
    if instrument == 'NIRISS':
        newdata[:, :, :5] = 0
        newdata[:, :, -5:] = 0
        newdata[:, -5:] = 0

    # Save interpolated data.
    if save_results is True:
        # Open input file and subtract background from data
        thisfile = fits.open(datafile)
        thisfile[1].data = newdata
        thisfile[2].data = err_cube
        thisfile[3].data = newdq
        # Save corrected data.
        result = output_dir + fileroot + 'badpixstep.fits'
        thisfile[0].header['FILENAME'] = fileroot + 'badpixstep.fits'
        thisfile.writeto(result, overwrite=True)
        fancyprint('File saved to: {}.'.format(result))
    # If not saving results, need to work in datamodels to not break interoperability with stsci
    # pipeline.
    else:
        currentfile = utils.open_filetype(datafile)
        result = copy.deepcopy(currentfile)
        result.data = newdata
        result.err = err_cube
        result.dq = newdq

    if do_plot is True and to_flag is None:
        if save_results is True:
            outfile = output_dir + 'badpixstep.png'
            # Get proper detector names for NIRSpec.
            instrument = utils.get_instrument_name(result)
            if instrument == 'NIRSPEC':
                det = utils.get_nrs_detector_name(result)
                outfile = outfile.replace('.png', '_{}.png'.format(det))
        else:
            outfile = None
        hotpix = np.where(hotpix != 0)
        nanpix = np.where(nanpix != 0)
        otherpix = np.where(otherpix != 0)
        deepframe[np.isnan(deepframe)] = 0
        if instrument == 'MIRI':
            miri = True
        else:
            miri = False
        plotting.make_badpix_plot(deepframe, hotpix, nanpix, otherpix, outfile=outfile,
                                  show_plot=show_plot, miri_scale=miri)

    return result, badpix


def pcareconstructionstep(datafiles, pca_components=10, remove_components=None, output_dir='./',
                          save_results=True, fileroot_noseg='', fileroots=None, do_plot=False,
                          show_plot=False):
    """Perform a reconstruction of the TSO datacube using principle component analysis (PCA).
    This allows for the identification and removal of components related to detector-based noise
    (e.g., drifts in the position of the spectral trace).
    Some of these functionalities were previously part of the TracingStep.

    Parameters
    ----------
    datafiles : array-like(RampModel, str)
        List of datamodels for a TSO, or paths to them.
    pca_components : int
        Number of PCA components to fit.
    remove_components : list(int), None
        Indices of PCA components to remove from the reconstruction.
    output_dir : str
        Directory to which to output results.
    save_results : bool
        If True, save results to file.
    fileroots : array-like(str), None
        Root names for output files.
    fileroot_noseg : str
        File root names without segment information.
    do_plot : bool
        If True, do the step diagnostic plot.
    show_plot : bool
        If True, show the step diagnostic plot instead of/in addition to saving it to file.

    Returns
    -------
    result : list(CubeModel, str)
        Input datamodels, after PCA reconstruction.
    """

    fancyprint('Starting PCA Reconstruction Step.')

    datafiles = np.atleast_1d(datafiles)
    # Construct datacube from the data files.
    for i, file in enumerate(datafiles):
        if isinstance(file, str):
            this_data = fits.getdata(file, 1)
        else:
            this_data = file.data
        if i == 0:
            cube = this_data
        else:
            cube = np.concatenate([cube, this_data], axis=0)

    # Get instrument name.
    instrument = utils.get_instrument_name(datafiles[0])

    # Calculate the trace stability using PCA -- original pass without any components removed.
    fancyprint('Calculating TSO stability.')
    if save_results is True:
        outfile = output_dir + 'stability_pca.png'
        # Get proper detector names for NIRSpec.
        if instrument == 'NIRSPEC':
            det = utils.get_nrs_detector_name(datafiles[0])
            outfile = outfile.replace('.png', '_{}.png'.format(det))
    else:
        outfile = None

    # For MIRI trim the frame down to get rid of e.g., the lightsaber artifact which introduces its
    # own signals.
    if instrument == 'MIRI':
        cube_clipped = cube[:, :, 12:61]
    else:
        cube_clipped = cube

    pcs, var, _ = soss_stability_pca(cube_clipped, n_components=pca_components, outfile=outfile,
                                     do_plot=do_plot, show_plot=show_plot)

    # If requested, reconstruct the data cube removing PCs associated with detector trends.
    if remove_components is not None:
        remove_components = np.atleast_1d(remove_components)
        fancyprint('Starting data cube reconstruction removing components {}.'
                   .format(remove_components))

        # Warn if the user wants to potentially remove the light curve.
        if 1 in remove_components:
            fancyprint('Removing component #1 -- this is generally the light curve!',
                       msg_type='WARNING')

        newcube = np.copy(cube)
        for pc in remove_components:
            # Get the reconstruction of the data using the specified component.
            if pc != 1:
                out_ncmo = soss_stability_pca(cube_clipped, n_components=pc-1)[2]
                out_nc = soss_stability_pca(cube_clipped, n_components=pc)[2]
                thiscomp = out_nc - out_ncmo
            else:
                thiscomp = soss_stability_pca(cube_clipped, n_components=pc)[2]
            # Remove the reconstruction.
            if instrument == 'MIRI':
                newcube[:, :, 12:61] -= thiscomp
            else:
                newcube -= thiscomp

        # Calculate the trace stability using PCA -- final result, with components removed.
        fancyprint('Calculating reconstructed TSO stability.')
        outfile = output_dir + 'stability_pca_reconstructed.png'
        # Get proper detector names for NIRSpec.
        instrument = utils.get_instrument_name(datafiles[0])
        if instrument == 'NIRSPEC':
            det = utils.get_nrs_detector_name(datafiles[0])
            outfile = outfile.replace('.png', '_{}.png'.format(det))
        # Again, trim MIRI.
        if instrument == 'MIRI':
            newcube_clipped = newcube[:, :, 12:61]
        else:
            newcube_clipped = newcube
        pcs, var, _ = soss_stability_pca(newcube_clipped, n_components=pca_components,
                                         outfile=outfile, do_plot=do_plot, show_plot=show_plot)

        # Save the reconstructed datafiles.
        results, current_int = [], 0
        fancyprint('Saving reconstructed data.')
        for n, file in enumerate(datafiles):
            if save_results is True:
                thisfile = fits.open(file)
                nints = np.shape(thisfile[1].data)[0]
                thisfile[1].data = newcube[current_int:(current_int + nints)]
                # Save reconstructed data.
                result = output_dir + fileroots[n] + 'pcareconstructstep.fits'
                thisfile[0].header['FILENAME'] = (fileroots[n] + 'pcareconstructstep.fits')
                thisfile.writeto(result, overwrite=True)
                fancyprint('File saved to: {}.'.format(result))
            # If not saving results, need to work in datamodels to not break interoperability with
            # stsci pipeline.
            else:
                with utils.open_filetype(file) as result:
                    nints = np.shape(result.data)[0]
                    result.data = newcube[current_int:(current_int + nints)]
            current_int += nints

            results.append(result)

    # If not reconstructing, just return the input datafiles.
    else:
        results = datafiles

    # Save the stability results.
    stability_results = {}
    for i, pc in enumerate(pcs):
        stability_results['Component {}'.format(i + 1)] = pc
    # Save stability results.
    suffix = 'stability.csv'
    if instrument == 'NIRSPEC':
        suffix = suffix.replace('.csv', '_{}.csv'.format(det))
    if os.path.exists(output_dir + fileroot_noseg + suffix):
        os.remove(output_dir + fileroot_noseg + suffix)
    df = pd.DataFrame(data=stability_results)
    df.to_csv(output_dir + fileroot_noseg + suffix, index=False)

    return results


def tracingstep(datafiles, deepframe=None, pixel_flags=None, generate_order0_mask=False,
                f277w=None, generate_lc=True, baseline_ints=None, smoothing_scale=None,
                output_dir='./', save_results=True, fileroot_noseg='', do_plot=False,
                show_plot=False, allow_miri_slope=False):
    """A multipurpose step to perform some initial analysis of the 2D dataframes and produce
    products which can be useful in further reduction iterations. The three functionalities are
    detailed below:
    1. Locate the centroids of all three SOSS orders via the edgetrigger algorithm.
    2. (optional) Generate a mask of order 0 contaminants from background stars.
    3. (optional) Create a smoothed estimate of the order 1 white light curve.

    Parameters
    ----------
    datafiles : array-like(RampModel), array-like(str)
        Datamodels for each segment of the TSO.
    deepframe : ndarray(float), None
        Deep stack for the TSO. Should be 2D (dimy, dimx). If None is passed, one will be generated.
    pixel_flags: array-like(str), None
        Paths to files containing existing pixel flags to which the order 0 mask should be added.
        Only necesssary if generate_order0_mask is True.
    generate_order0_mask : bool
        If True, generate a mask of order 0 cotaminants using an F277W filter exposure.
    f277w : ndarray(float), None
        F277W filter exposure which has been superbias and background corrected. Only necessary if
        generate_order0_mask is True.
    generate_lc : bool
        If True, also produce a smoothed order 1 white light curve.
    baseline_ints : array-like(int)
        Integrations of ingress and egress. Only necessary if generate_lc=True.
    smoothing_scale : int, None
        Timescale on which to smooth the lightcurve. Only necessary if generate_lc=True.
    output_dir : str
        Directory to which to save outputs.
    save_results : bool
        If Tre, save results to file.
    fileroot_noseg : str
        Root file name with no segment information.
    do_plot : bool
        If True, do the step diagnostic plot.
    show_plot : bool
        If True, show the step diagnostic plot instead of/in addition to saving it to file.
    allow_miri_slope : bool
        If True, allow the MIRI centroids to be sloped.

    Returns
    -------
    centroids : np.ndarray(float), str
        Trace centroids for all orders, or path to centroids file.
    """

    fancyprint('Starting Tracing Step.')

    datafiles = np.atleast_1d(datafiles)
    # If no deepframe is passed, construct one. Also generate a datacube for later white light
    # curve or stability calculations.
    if deepframe is None or generate_lc is True:
        # Construct datacube from the data files.
        for i, file in enumerate(datafiles):
            if isinstance(file, str):
                this_data = fits.getdata(file, 1)
            else:
                this_data = file.data
            if i == 0:
                cube = this_data
            else:
                cube = np.concatenate([cube, this_data], axis=0)
        deepframe = utils.make_deepstack(cube)

    # ===== PART 1: Get centroids for orders one to three =====
    fancyprint('Finding trace centroids.')
    instrument = utils.get_instrument_name(datafiles[0])
    if instrument == 'NIRISS':
        subarray = utils.get_soss_subarray(datafiles[0])
        # Get the most up to date trace table file.
        step = calwebb_spec2.extract_1d_step.Extract1dStep()
        tracetable = step.get_reference_file(datafiles[0], 'spectrace')
        # Get centroids via the edgetrigger method.
        save_filename = output_dir + fileroot_noseg
        centroids = utils.get_centroids_soss(deepframe, tracetable, subarray,
                                             save_results=save_results, save_filename=save_filename)
    elif instrument == 'NIRSPEC':
        # Get centroids via the edgetrigger method.
        save_filename = output_dir + fileroot_noseg
        det = utils.get_nrs_detector_name(datafiles[0])
        subarray = utils.get_soss_subarray(datafiles[0])
        grating = utils.get_nrs_grating(datafiles[0])
        xstart = utils.get_nrs_trace_start(det, subarray, grating)
        centroids = utils.get_centroids_nirspec(deepframe, xstart=xstart, save_results=save_results,
                                                save_filename=save_filename)
    else:
        # Get centroids via the edgetrigger method.
        save_filename = output_dir + fileroot_noseg
        centroids = utils.get_centroids_miri(deepframe, ystart=50, save_results=save_results,
                                             save_filename=save_filename,
                                             allow_slope=allow_miri_slope)

    # Do diagnostic plot if requested.
    if do_plot is True:
        if save_results is True:
            if instrument == 'NIRSPEC':
                outfile = output_dir + 'centroiding_{}.png'.format(det)
            else:
                outfile = output_dir + 'centroiding.png'
        else:
            outfile = None
        miri_scale = False
        if instrument == 'MIRI':
            miri_scale = True
        plotting.make_centroiding_plot(deepframe, centroids, instrument, show_plot=show_plot,
                                       outfile=outfile, miri_scale=miri_scale)

    if save_results is True:
        centroids = save_filename + 'centroids.csv'

    # If not saving outputs, skip optional parts.
    if generate_lc is True or generate_order0_mask is True:
        if save_results is False:
            fancyprint('Optional outputs requested but save_results=False. '
                       'Skipping optional outputs.', msg_type='WARNING')
            generate_order0_mask = False
            generate_lc = False

    # ===== PART 2: Create order 0 background contamination mask =====
    # If requested, create a mask for all background order 0 contaminants.
    if generate_order0_mask is True:
        fancyprint('Generating background order 0 mask.')
        order0mask = make_order0_mask_from_f277w(f277w)

        # Save the order 0 mask to file.
        if save_results is True:
            # If we are to combine the trace mask with existing pixel mask.
            if pixel_flags is not None:
                pixel_flags = np.atleast_1d(pixel_flags)
                # Ensure there is one pixel flag file per data file
                assert len(pixel_flags) == len(datafiles)
                # Combine with existing flags and overwrite old file.
                for flag_file in pixel_flags:
                    with fits.open(flag_file) as old_flags:
                        currentflag = old_flags[1].data.astype(bool) | order0mask.astype(bool)
                        old_flags[1].data = currentflag.astype(int)
                        old_flags.writeto(flag_file, overwrite=True)
                # Overwrite old flags file.
                parts = pixel_flags[0].split('seg')
                outfile = parts[0] + 'seg' + 'XXX' + parts[1][3:]
                fancyprint('Order 0 mask added to {}'.format(outfile))
            else:
                hdu = fits.PrimaryHDU(order0mask)
                suffix = 'order0_mask.fits'
                outfile = output_dir + fileroot_noseg + suffix
                hdu.writeto(outfile, overwrite=True)
                fancyprint('Order 0 mask saved to {}'.format(outfile))

    # ===== PART 3: Calculate a smoothed light curve =====
    # If requested, generate a smoothed estimate of the order 1 white light curve.
    if generate_lc is True:
        fancyprint('Generating a smoothed light curve')
        # Format the baseline frames.
        assert baseline_ints is not None
        baseline_ints = utils.format_out_frames(baseline_ints)

        # Use an area centered on the peak of the order 1 blaze to estimate the photometric light
        # curve.
        postage = cube[:, 20:60, 1500:1550]
        timeseries = np.nansum(postage, axis=(1, 2))
        # Normalize by the baseline flux level.
        timeseries = timeseries / np.nanmedian(timeseries[baseline_ints])
        # If not smoothing scale is provided, smooth the time series on a timescale of roughly 2%
        # of the total length.
        if smoothing_scale is None:
            smoothing_scale = int(0.02 * np.shape(cube)[0])
        smoothed_lc = median_filter(timeseries, smoothing_scale)

        if save_results is True:
            outfile = output_dir + fileroot_noseg + 'lcestimate.npy'
            fancyprint('Smoothed light curve saved to {}'.format(outfile))
            np.save(outfile, smoothed_lc)

    return centroids


def make_order0_mask_from_f277w(f277w, thresh_std=1, thresh_size=10):
    """Locate order 0 contaminants from background stars using an F277W filter exposure data frame.

    Parameters
    ----------
    f277w : array-like(float)
        An F277W filter exposure, superbias and background subtracted.
    thresh_std : int
        Threshold above which a group of pixels will be flagged.
    thresh_size : int
        Size of pixel group to be considered an order 0.

    Returns
    -------
    mask : array-like(int)
        Frame with locations of order 0 contaminants.
    """

    dimy, dimx = np.shape(f277w)
    mask = np.zeros_like(f277w)

    # Loop over all columns and find groups of pixels which are significantly above the column
    # median.
    # Start at column 700 as that is ~where pickoff mirror effects start.
    for col in range(700, dimx):
        # Subtract median from column and get the standard deviation
        diff = f277w[:, col] - np.nanmedian(f277w[:, col])
        dev = np.nanstd(diff)
        # Find pixels which are deviant.
        vals = np.where(np.abs(diff) > thresh_std * dev)[0]
        # Mark consecutive groups of pixels found above.
        for group in mit.consecutive_groups(vals):
            group = list(group)
            if len(group) > thresh_size:
                # Extend 3 columns and rows to either size.
                min_g = np.max([0, np.min(group) - 3])
                max_g = np.min([dimy - 1, np.max(group) + 3])
                mask[min_g:max_g, (col - 3):(col + 3)] = 1

    return mask


def soss_stability_pca(cube, n_components=10, outfile=None, do_plot=False, show_plot=False):
    """Calculate the stability of the SOSS trace over the course of a TSO using a PCA method.

    Parameters
    ----------
    cube : array-like(float)
        Cube of TSO data.
    n_components : int
        Maximum number of principle components to calcaulte.
    outfile : None, str
        File to which to save plot.
    do_plot : bool
        If True, do the step diagnostic plot.
    show_plot : bool
        If True, show the step diagnostic plot instead of/in addition to saving it to file.

    Returns
    -------
    pcs : np.ndarray(float)
        Extracted principle components.
    var : np.ndarray(float)
        Explained variance of each principle component.
    reconstruction : np.adarray(float)
        Input cube reconstructed using n_components PCs.
    """

    # Flatten cube along frame direction.
    nints, dimy, dimx = np.shape(cube)
    cube = np.reshape(cube, (nints, dimx * dimy))

    # Replace any remaining nan-valued pixels.
    cube2 = np.reshape(np.copy(cube), (nints, dimy*dimx))
    ii = np.where(np.isnan(cube2))
    med = bn.nanmedian(cube2)
    cube2[ii] = med

    # Do PCA.
    pca = PCA(n_components=n_components)
    pca.fit(cube2.transpose())

    # Get PCA results.
    pcs = pca.components_
    var = pca.explained_variance_ratio_

    # Reproject PCs onto data.
    projection = pca.transform(cube2.transpose())
    projection = np.reshape(projection, (dimy, dimx, n_components))

    if do_plot is True:
        # Do plot.
        plotting.make_pca_plot(pcs, var, projection.transpose(2, 0, 1), outfile=outfile,
                               show_plot=show_plot)

    # Reconstruct input data using extracted PCs.
    reconstruction = pca.inverse_transform(projection)
    reconstruction = reconstruction.reshape(dimy, dimx, nints)
    reconstruction = reconstruction.transpose(2, 0, 1)

    return pcs, var, reconstruction


def run_stage2(results, mode, soss_background_model=None, baseline_ints=None, save_results=True,
               force_redo=False, space_thresh=15, time_thresh=15,  remove_components=None,
               pca_components=10, soss_timeseries=None, soss_timeseries_o2=None,
               oof_method='scale-achromatic', root_dir='./', output_tag='', smoothing_scale=None,
               skip_steps=None, generate_lc=True, soss_inner_mask_width=40,
               soss_outer_mask_width=70, nirspec_mask_width=16, pixel_masks=None,
               generate_order0_mask=True, f277w=None, do_plot=False, show_plot=False,
               centroids=None, miri_trace_width=20, miri_background_width=14,
               miri_background_method='median', **kwargs):
    """Run the exoTEDRF Stage 2 pipeline: spectroscopic processing, using a combination of official
    STScI DMS and custom steps. Documentation for the official DMS steps can be found here:
    https://jwst-pipeline.readthedocs.io/en/latest/jwst/pipeline/calwebb_spec2.html

    Parameters
    ----------
    results : array-like(str), array-like(CubeModel)
        exoTEDRF Stage 1 output files.
    mode : str
        Instrument mode which produced the data being analyzed.
    soss_background_model : array-like(float), None
        SOSS background model or path to a file containing it.
    baseline_ints : array-like(int), None
        Integrations of ingress and egress.
    save_results : bool
        If True, save results of each step to file.
    force_redo : bool
        If True, redo steps even if outputs files are already present.
    space_thresh : int
        Sigma threshold for pixel to be flagged as an outlier spatially.
    time_thresh : int
        Sigma threshold for pixel to be flagged as an outlier temporally.
    remove_components : list(int), None
        Numbers of PCA components to remove during the data reconstruction.
    pca_components : int
        Number of PCA components to calculate.
    soss_timeseries : array-like(float), None
        Normalized 1D or 2D light curve(s) for order 1, or path to a file containing it.
    soss_timeseries_o2 : array-like(float), None
        Normalized 2D light curves for order 2, or path to a file contanining them. Only necessary
        if oof_method is "scale-chromatic".
    oof_method : str
        1/f correction method. Options are "scale-chromatic", "scale-achromatic",
        "scale-achromatic-window", or "solve".
    root_dir : str
        Directory from which all relative paths are defined.
    output_tag : str
        Name tag to append to pipeline outputs directory.
    smoothing_scale : int, None
        Timescale on which to smooth the lightcurve.
    skip_steps : list(str), None
        Step names to skip (if any).
    generate_lc : bool
        If True, produce a smoothed order 1 white light curve.
    soss_inner_mask_width : int
        Inner mask width, in pixels, around the trace centroids.
    soss_outer_mask_width : int
        Outer mask width, in pixels, around the trace centroids.
    nirspec_mask_width : int
        Full-width (in pixels) around the target trace to mask for NIRSpec.
    pixel_masks: None, str, array-like(str)
        Paths to files containing existing pixel flags to which the order 0 mask should be added.
        Only necesssary if generate_order0_mask is True.
    generate_order0_mask : bool
        If True, generate a mask of order 0 cotaminants using an F277W filter exposure.
    f277w : None, str, array-like(float)
        F277W filter exposure which has been superbias and background corrected.
        Only necessary if generate_order0_mask is True.
    do_plot : bool
        If True, make step diagnostic plots.
    show_plot : bool
        Only necessary if do_plot is True. Show the diagnostic plots in addition to/instead of
        saving to file.
    centroids : str, None
        Path to file containing trace positions for all orders.
    miri_trace_width : int
        Full width of the MIRI trace.
    miri_background_width : int
        Width of the MIRI background region.
    miri_background_method : str
        Method to calculate MIRI background; either 'median' or 'slope'.

    Returns
    -------
    results : list(CubeModel)
        Datafiles for each segment processed through Stage 2.
    centroids : ndarray(fllat), str
        Centroids for all spectral orders.
    """

    # ============== DMS Stage 2 ==============
    # Spectroscopic processing.
    fancyprint('**Starting exoTEDRF Stage 2**')
    fancyprint('Spectroscopic processing')

    if output_tag != '':
        output_tag = '_' + output_tag
    # Create output directories and define output paths.
    utils.verify_path(root_dir + 'pipeline_outputs_directory' + output_tag)
    utils.verify_path(root_dir + 'pipeline_outputs_directory' + output_tag + '/Stage2')
    outdir = root_dir + 'pipeline_outputs_directory' + output_tag + '/Stage2/'

    if skip_steps is None:
        skip_steps = []

    # ===== Assign WCS Step =====
    # Default DMS step.
    if 'AssignWCSStep' not in skip_steps:
        if 'AssignWCSStep' in kwargs.keys():
            step_kwargs = kwargs['AssignWCSStep']
        else:
            step_kwargs = {}
        step = AssignWCSStep(results, output_dir=outdir)
        results = step.run(save_results=save_results, force_redo=force_redo, **step_kwargs)

    # ===== Extract 2D Step =====
    # Default DMS step.
    if 'Extract2DStep' not in skip_steps:
        if 'NIRSPEC' in mode.upper():
            if 'Extract2DStep' in kwargs.keys():
                step_kwargs = kwargs['Extract2DStep']
            else:
                step_kwargs = {}
            step = Extract2DStep(results, output_dir=outdir)
            results = step.run(save_results=save_results, force_redo=force_redo, **step_kwargs)
        else:
            fancyprint('Extract2DStep not supported for {}.'.format(mode), msg_type='WARNING')

    # ===== Source Type Determination Step =====
    # Default DMS step.
    if 'SourceTypeStep' not in skip_steps:
        if 'SourceTypeStep' in kwargs.keys():
            step_kwargs = kwargs['SourceTypeStep']
        else:
            step_kwargs = {}
        step = SourceTypeStep(results, output_dir=outdir)
        results = step.run(save_results=save_results, force_redo=force_redo, **step_kwargs)

    # ===== Wavelength Correction Step =====
    # Default DMS step.
    if 'WaveCorrStep' not in skip_steps:
        if 'NIRSPEC' in mode.upper():
            if 'WaveCorrStep' in kwargs.keys():
                step_kwargs = kwargs['WaveCorrStep']
            else:
                step_kwargs = {}
            step = WaveCorrStep(results, output_dir=outdir)
            results = step.run(save_results=save_results, force_redo=force_redo, **step_kwargs)
        else:
            fancyprint('WaveCorrStep not supported for {}.'.format(mode), msg_type='WARNING')

    # ===== Flat Field Correction Step =====
    # Default DMS step.
    if 'FlatFieldStep' not in skip_steps:
        if 'NIRSPEC' not in mode.upper():
            if 'FlatFieldStep' in kwargs.keys():
                step_kwargs = kwargs['FlatFieldStep']
            else:
                step_kwargs = {}
            step = FlatFieldStep(results, output_dir=outdir)
            results = step.run(save_results=save_results, force_redo=force_redo, **step_kwargs)
        else:
            fancyprint('FlatFieldStep not supported for {}.'.format(mode), msg_type='WARNING')

    # ===== Background Subtraction Step =====
    # Custom DMS step.
    if 'BackgroundStep' not in skip_steps:
        if 'NIRSPEC' not in mode.upper():
            if 'BackgroundStep' in kwargs.keys():
                step_kwargs = kwargs['BackgroundStep']
            else:
                step_kwargs = {}
            step = BackgroundStep(results, baseline_ints=baseline_ints,
                                  background_model=soss_background_model,
                                  miri_method=miri_background_method, output_dir=outdir)
            results = step.run(save_results=save_results, force_redo=force_redo, do_plot=do_plot,
                               show_plot=show_plot, miri_trace_width=miri_trace_width,
                               miri_background_width=miri_background_width, **step_kwargs)[0]
        else:
            fancyprint('BackgroundStep not supported for {}.'.format(mode), msg_type='WARNING')

    # ===== 1/f Noise Correction Step =====
    # Custom DMS step.
    if 'OneOverFStep' not in skip_steps:
        if mode.upper() != 'MIRI/LRS':
            if 'OneOverFStep' in kwargs.keys():
                step_kwargs = kwargs['OneOverFStep']
            else:
                step_kwargs = {}
            step = stage1.OneOverFStep(results, output_dir=outdir, baseline_ints=baseline_ints,
                                       pixel_masks=pixel_masks, centroids=centroids,
                                       method=oof_method, soss_timeseries=soss_timeseries,
                                       soss_timeseries_o2=soss_timeseries_o2)
            results = step.run(soss_inner_mask_width=soss_inner_mask_width,
                               soss_outer_mask_width=soss_outer_mask_width,
                               nirspec_mask_width=nirspec_mask_width, save_results=save_results,
                               force_redo=force_redo, do_plot=do_plot, show_plot=show_plot,
                               **step_kwargs)
        else:
            fancyprint('OneOverFStep not supported for {}.'.format(mode), msg_type='WARNING')

    # ===== Bad Pixel Correction Step =====
    # Custom DMS step.
    if 'BadPixStep' not in skip_steps:
        if 'BadPixStep' in kwargs.keys():
            step_kwargs = kwargs['BadPixStep']
        else:
            step_kwargs = {}
        step = BadPixStep(results, baseline_ints=baseline_ints, output_dir=outdir)
        results = step.run(save_results=save_results, space_thresh=space_thresh,
                           time_thresh=time_thresh, force_redo=force_redo, do_plot=do_plot,
                           show_plot=show_plot, **step_kwargs)

    # ===== PCA Reconstruction Step =====
    # Custom DMS step.
    if 'PCAReconstructStep' not in skip_steps:
        if 'PCAReconstructStep' in kwargs.keys():
            step_kwargs = kwargs['PCAReconstructStep']
        else:
            step_kwargs = {}
        step = PCAReconstructStep(results, baseline_ints=baseline_ints, output_dir=outdir)
        step_results = step.run(save_results=save_results, pca_components=pca_components,
                                remove_components=remove_components, force_redo=force_redo,
                                do_plot=do_plot, show_plot=show_plot, **step_kwargs)
        results, deepframe = step_results
    else:
        deepframe = None

    # ===== Tracing Step =====
    # Custom DMS step.
    if 'TracingStep' not in skip_steps:
        step = TracingStep(results, deepframe=deepframe, output_dir=outdir,
                           generate_order0_mask=generate_order0_mask, f277w=f277w,
                           generate_lc=generate_lc, baseline_ints=baseline_ints)
        centroids = step.run(pixel_flags=pixel_masks, smoothing_scale=smoothing_scale,
                             save_results=save_results, do_plot=do_plot, show_plot=show_plot,
                             force_redo=force_redo)
    else:
        centroids = None

    return results, centroids

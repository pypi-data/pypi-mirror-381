#
# Delft University of Technology (TU Delft) hereby disclaims all copyright interest in the program 'LocScale'
# written by the Author(s).
# Copyright (C) 2021 Alok Bharadwaj and Arjen J. Jakobi
# This software may be modified and distributed under the terms of the BSD license. 
# You should have received a copy of the BSD 3-clause license along with this program (see LICENSE file file for details).
# If not see https://opensource.org/license/bsd-3-clause/.
#

import numpy as np
import os
import sys
from locscale.include.emmer.ndimage.map_utils import save_as_mrc
#import gemmi


def compute_radial_profile_proper(vol, frequency_map):

    vol_fft = np.fft.rfftn(vol, norm="ortho");
    dim = vol_fft.shape;
    ps = np.real(np.abs(vol_fft));
    frequencies = np.fft.rfftfreq(dim[0]);
    #bins = np.digitize(frequency_map, frequencies);
    #bins = bins - 1;
    x, y, z = np.indices(ps.shape)
    radii = np.sqrt(x**2 + y**2 + z**2)
    radii = radii.astype(int)
    radial_profile = np.bincount(radii.ravel(), ps.ravel()) / np.bincount(radii.ravel())
    radial_profile = radial_profile[0:int(ps.shape[0]/2)+1]

    return radial_profile, frequencies;

def compute_scale_factors(em_profile, ref_profile, apix, scale_factor_arguments, 
                          use_theoretical_profile=True, check_scaling=False, measure_bfactors=False):
    """Function to calculate the scale factors given two profiles.
    This function is compatible with both pseudo-atomic model routine and 
    regular atomic model routine.

    Args:
        em_profile (numpy array (1D)): The profile of the unsharpened EM map
        ref_profile (numpy array (1D)): The profile of the reference map
        apix (float): The pixel size of the map 
        scale_factor_arguments (dict): The arguments for the scaling function for pseudomodle routine
        use_theoretical_profile (bool, optional): Flag to check if pseudomodel routine is to be followed 
                                                            (using theoretical profiles). Defaults to True.
        check_scaling (bool, optional): Flag to collect local profile information for auditing later. 
                                        Defaults to False.

    Returns:
        scale_factor (numpy array (1D)): The scale factors for the EM map
        bfactor (float): The local bfactor of the reference map 
        qfit (float): The local qfit of the reference map for bfactor calculation
    """
    import warnings
    from locscale.include.emmer.ndimage.profile_tools import scale_profiles, merge_two_profiles, \
        add_deviations_to_reference_profile, frequency_array, estimate_bfactor_standard, get_theoretical_profile
    from locscale.utils.file_tools import RedirectStdoutToLogger
    
    ################################################################################
    # SCALING WITHOUT REFERENCE
    # Scaling without a reference profile is done by measuring the local bfactor
    # and obtaining a "sharpening profile" which has the negative bfactor of the 
    # unsharpened cube. This is then used to calculate the scale factors.
    # This method is not recommended since it is not robust to noise.
    ################################################################################
    warnings.filterwarnings("ignore")
    if scale_factor_arguments['no_reference']:
        use_theoretical_profile = False
        ################################################################################
        # Get a theoretical profile to add deviations
        ################################################################################
        theoretical_profile_tuple = get_theoretical_profile(length=len(em_profile),apix=apix)
        freq = theoretical_profile_tuple[0]
        scaled_theoretical_amplitude = theoretical_profile_tuple[1]

        ################################################################################
        # Calculate local B-factors
        ################################################################################
        wilson_cutoff = scale_factor_arguments['wilson']
        fsc_cutoff = scale_factor_arguments['fsc_cutoff']
        bfactor, amplitude, qfit = estimate_bfactor_standard(
            freq, em_profile, wilson_cutoff, fsc_cutoff, return_amplitude=True, 
            return_fit_quality=True, standard_notation=True)

        ################################################################################
        # Calculate the sharpening profile
        ################################################################################
        set_local_bfactor = scale_factor_arguments['set_local_bfactor']
        assert set_local_bfactor >= 0, "Local bfactor must be positive or zero"
        b_sharpen = bfactor - set_local_bfactor
        sharpening_profile = np.exp(0.25 * b_sharpen * freq**2)
        
        ################################################################################
        # Scale the reference profile using sharpening profile
        ################################################################################
        scaled_reference_profile = em_profile * sharpening_profile

        ################################################################################
        # Filter the scaled reference profile at FSC resolution
        ################################################################################
        fsc_filtered_reference_profile = merge_two_profiles(scaled_reference_profile, np.zeros(len(freq)), freq, smooth=10, d_cutoff=fsc_cutoff)
        
        
        reference_profile_for_scaling = fsc_filtered_reference_profile
        if check_scaling:
            temporary_dictionary = {}
            temporary_dictionary['em_profile'] = em_profile
            temporary_dictionary['input_ref_profile'] = fsc_filtered_reference_profile
            temporary_dictionary['freq'] = freq
            temporary_dictionary['theoretical_amplitude'] = theoretical_profile_tuple[1]
            temporary_dictionary['scaled_theoretical_amplitude'] = scaled_theoretical_amplitude
            temporary_dictionary['scaled_reference_profile'] = scaled_reference_profile
            temporary_dictionary['fsc_filtered_reference_profile'] = fsc_filtered_reference_profile
            temporary_dictionary['deviated_reference_profile'] = np.zeros(len(freq)) ## temp to save errors later
            temporary_dictionary['bfactor'] = bfactor
            temporary_dictionary['qfit'] = qfit
            temporary_dictionary['amplitude'] = amplitude
            temporary_dictionary['scaling_condition'] = scale_factor_arguments
    
    ################################################################################
    # SCALING WITH A REFERENCE:
    # Scaling is done with a reference. The reference is generated either 
    # from pseudo-atomic model map modulated by a theoretical profile or
    # from a regular atomic model map.
    ################################################################################

    ##############################################################################################
    ## Stage 1: Prepare the reference profile to be used for scaling
    ##############################################################################################
    elif use_theoretical_profile:
        ##########################################################################################
        # Follow pseudomodel routine using theoretical profiles
        ##########################################################################################
        theoretical_profile_tuple = get_theoretical_profile(length=len(ref_profile),apix=apix)
        freq = theoretical_profile_tuple[0]
        
        ##########################################################################################
        # Calculate the local wilson cutoff to apply deviations
        ##########################################################################################
        num_atoms = ref_profile[0]
        mol_weight = num_atoms * 16  # daltons 
        wilson_cutoff_local = 1/(0.309 * np.power(mol_weight, -1/12))   ## From Amit Singer
        wilson_cutoff_local = np.clip(wilson_cutoff_local, scale_factor_arguments['fsc_cutoff']*1.5, scale_factor_arguments['wilson'])

        ##########################################################################################
        # Scale the theoretical profile to match the bfactor of the reference profile
        ##########################################################################################
        reference_profile_tuple = (freq, ref_profile)
        scaled_theoretical_tuple,(bfactor,amp, qfit) = scale_profiles(reference_profile_tuple, theoretical_profile_tuple,
                                                wilson_cutoff=wilson_cutoff_local, fsc_cutoff=scale_factor_arguments['nyquist'], \
                                                return_bfactor_properties=True)
        bfactor = -1 * bfactor  ## Standard notation
        scaled_theoretical_amplitude = scaled_theoretical_tuple[1]
        
        smooth = scale_factor_arguments['smooth']
        
        ## Using merge_profile
        scaled_reference_profile = merge_two_profiles(ref_profile,scaled_theoretical_amplitude,freq,smooth=smooth,d_cutoff=wilson_cutoff_local)
        
        ############################################################################################
        ## Apply the required deviations to the reference profile to match theoretical prediction
        ############################################################################################
        deviations_begin = wilson_cutoff_local
        deviations_end = scale_factor_arguments['fsc_cutoff']
        magnify = scale_factor_arguments['boost_secondary_structure']
        
        deviated_reference_profile, exp_fit = add_deviations_to_reference_profile(
            freq, ref_profile, scaled_theoretical_amplitude, wilson_cutoff=wilson_cutoff_local, \
            nyquist_cutoff=scale_factor_arguments['nyquist'], deviation_freq_start=deviations_begin, \
            deviation_freq_end=deviations_end, magnify=magnify)
                
        reference_profile_for_scaling = deviated_reference_profile 
        ## ^ This is the profile used for scale factor calculation

        ############################################################################################
        ## Collect profile information if check_scaling is True
        ############################################################################################
        if check_scaling:
            temporary_dictionary = {}
            temporary_dictionary['em_profile'] = em_profile
            temporary_dictionary['input_ref_profile'] = ref_profile
            temporary_dictionary['freq'] = freq
            temporary_dictionary['theoretical_amplitude'] = theoretical_profile_tuple[1]
            temporary_dictionary['scaled_theoretical_amplitude'] = scaled_theoretical_amplitude
            temporary_dictionary['scaled_reference_profile'] = scaled_reference_profile
            temporary_dictionary['deviated_reference_profile'] = deviated_reference_profile
            temporary_dictionary['exponential_fit'] = exp_fit
            temporary_dictionary['bfactor'] = bfactor
            temporary_dictionary['amplitude'] = amp
            temporary_dictionary['qfit'] = qfit
            temporary_dictionary['local_wilson'] = wilson_cutoff_local
            temporary_dictionary['deviations_begin'] = deviations_begin
            temporary_dictionary['deviations_end'] = deviations_end
            temporary_dictionary['magnify'] = magnify
            temporary_dictionary['scaling_condition'] = scale_factor_arguments
    else:
        ##########################################################################################
        # Follow regular atomic model routine and use the input reference profile for calculation
        ##########################################################################################

        freq = frequency_array(ref_profile, apix=apix)
        wilson_cutoff_traditional = 10
        ##########################################################################################
        # Calculate the local bfactor information from refernce profile
        ##########################################################################################
        if measure_bfactors:
            bfactor, amp, qfit = estimate_bfactor_standard(freq=freq, amplitude=ref_profile, wilson_cutoff=wilson_cutoff_traditional, 
                                                        fsc_cutoff=scale_factor_arguments['fsc_cutoff'], return_amplitude=True, return_fit_quality=True, standard_notation=True)
        else:
            bfactor = 99
            amp = 99
            qfit = 0.99
        
        reference_profile_for_scaling = ref_profile
    
    ##############################################################################################
    # Stage 2: Calculate the scale factor
    ##############################################################################################

    np.seterr(divide='ignore', invalid='ignore')
    scale_factor = np.divide(np.abs(reference_profile_for_scaling), np.abs(em_profile))
    scale_factor[ ~ np.isfinite( scale_factor )] = 0; #handle division by zero    
    
    # Collect results in a dictionary and return
    scale_factor_results = {}
    scale_factor_results['scale_factors'] = scale_factor
    scale_factor_results['bfactor'] = bfactor
    scale_factor_results['quality_fit'] = qfit

    if check_scaling and (use_theoretical_profile or scale_factor_arguments['no_reference']):
        temporary_dictionary['scale_factor'] = scale_factor
        scale_factor_results['report'] = temporary_dictionary
    
    else:
        scale_factor_results['report'] = None
        
    return scale_factor_results

def set_radial_profile(vol, scale_factors, frequencies, frequency_map, shape):
    vol_fft = np.fft.rfftn(np.copy(vol), norm='ortho');
    scaling_map = np.interp(frequency_map, frequencies, scale_factors);
    scaled_map_fft = scaling_map * vol_fft;
    scaled_map = np.real(np.fft.irfftn(scaled_map_fft, shape, norm='ortho'));

    return scaled_map, scaled_map_fft;

def get_central_scaled_pixel_vals_after_scaling(scaling_dictionary):

    """ 
    This function performs calls the scaling function in a rolling window fashion. 
    Once the scaled cubes are calculated the central voxels in each cube is extracted
    into a list. This list is then returned. This function is compatible with 
    both MPI and non-MPI environments.
    """
    from tqdm import tqdm
    from locscale.include.emmer.ndimage.map_tools import compute_real_space_correlation
    from locscale.include.emmer.ndimage.map_utils import load_map
    from locscale.utils.math_tools import true_percent_probability
    from locscale.include.confidenceMapUtil import FDRutil
    from locscale.utils.general import pad_or_crop_volume
    import pickle
    import pandas as pd
    import os
    from locscale.utils.math_tools import round_up_proper
    
    ###############################################################################
    # Stage 1: Initialize and collect variables
    ###############################################################################
    sharpened_vals = []
    qfit_voxels = []
    bfactor_voxels = []
    audit = True

    wn = scaling_dictionary['wn']
    apix = scaling_dictionary['apix']
    if audit:
        profiles_audit = {}

    temp_folder = scaling_dictionary['processing_files_folder']
    hybrid_model_scaling = scaling_dictionary['complete_model']
    measure_bfactors = scaling_dictionary['measure_bfactors']
    preprocess_intermediate_pickle_file = os.path.join(temp_folder, 'intermediate_outputs.pickle')
    # If the intermediate pickle file exists, load it and continue from there
    if os.path.exists(preprocess_intermediate_pickle_file):
        preprocess_outputs = pd.read_pickle(preprocess_intermediate_pickle_file)
    if hybrid_model_scaling:
        difference_mask_path = preprocess_outputs['difference_mask_path']
        difference_mask = load_map(difference_mask_path)[0]
        # check for window bleeding
        if scaling_dictionary["win_bleed_pad"]:
            new_emmap_shape = scaling_dictionary["emmap"].shape
            difference_mask = pad_or_crop_volume(difference_mask, new_emmap_shape, 0)

        difference_mask_bool = difference_mask.astype(bool)
    else:
        difference_mask_bool = None

    central_pix = round_up_proper(wn / 2.0)
    total = (scaling_dictionary['masked_xyz_locs'] - wn / 2).shape[0]
    cnt = 1.0

    ###############################################################################
    # Stage 1a: Create a progress bar 
    ###############################################################################

    mpi=False
    if scaling_dictionary['use_mpi']:
        mpi=True
        from mpi4py import MPI
        
        comm = MPI.COMM_WORLD
        rank=comm.Get_rank()
        size=comm.Get_size()
        
        pbar = {}
        if rank == 0:
            pbar = tqdm(total=len(scaling_dictionary['masked_xyz_locs'])*size,desc="LocScale MPI",file=sys.stdout)
    else:
        progress_bar=tqdm(total=len(scaling_dictionary['masked_xyz_locs']), desc="LocScale",file=sys.stdout)
    
    ###############################################################################
    # Stage 2: Perform the scaling in a rolling window fashion
    ###############################################################################
    frequency_map_window = FDRutil.calculate_frequency_map(np.zeros((wn, wn, wn)));
    
    for k, j, i in scaling_dictionary['masked_xyz_locs'] - wn / 2:
        try:
            # k,j,i are indices of the corner voxel in each cube. Ensure it is rounded up to integer.
            k,j,i,wn = round_up_proper(k), round_up_proper(j), round_up_proper(i), round_up_proper(wn)
            
            #######################################################################
            # Stage 2a: Extract the cube from the EM map and model maps
            #######################################################################
            emmap_wn = scaling_dictionary['emmap'][k: k+wn, j: j+wn, i: i+ wn]
            modmap_wn = scaling_dictionary['modmap'][k: k+wn, j: j+wn, i: i+ wn]

            #######################################################################
            # Stage 2b: Compute the radial profile of the two cubes        
            #######################################################################
            em_profile, frequencies_map = compute_radial_profile_proper(emmap_wn, frequency_map_window)
            mod_profile, _ = compute_radial_profile_proper(modmap_wn, frequency_map_window)
            
            # Checks scaling operation for 1% of all voxels. 
            check_scaling=true_percent_probability(1) 
            
            #######################################################################
            # Stage 2c: Compute the scale factors given the two radial profiles
            #######################################################################

            
            if hybrid_model_scaling: 
                k_center, j_center, i_center = round_up_proper(k + wn // 2), round_up_proper(j + wn // 2), round_up_proper(i + wn // 2)

                central_voxel_inside_mask = difference_mask_bool[k_center, j_center, i_center]
                use_theoretical_profile = central_voxel_inside_mask
            else:
                use_theoretical_profile = scaling_dictionary['use_theoretical_profile']


            scale_factor_result = compute_scale_factors(
                em_profile,mod_profile, apix=apix, check_scaling=check_scaling, \
                scale_factor_arguments=scaling_dictionary['scale_factor_arguments'], \
                use_theoretical_profile=use_theoretical_profile, measure_bfactors=measure_bfactors)
            
            scale_factors = scale_factor_result['scale_factors']
            bfactor = scale_factor_result['bfactor']
            quality_fit = scale_factor_result['quality_fit']

            if check_scaling and use_theoretical_profile:
                report = scale_factor_result['report']
                profiles_audit[(k,j,i)] = report
            
            # if check_scaling and scaling_dictionary['use_theoretical_profile']:

            #     ### A profile audit is done for pseudo-atomic model routine 
            #     ### to check if the theoretical profiles were scaled properly

            #     scale_factors, bfactor, quality_fit, report = compute_scale_factors(
            #         em_profile, mod_profile,apix=apix,scale_factor_arguments=scaling_dictionary['scale_factor_arguments'], \
            #         use_theoretical_profile=scaling_dictionary['use_theoretical_profile'], check_scaling=check_scaling)

            #     profiles_audit[(k,j,i)] = report
            # else:
            #     scale_factors, bfactor, quality_fit = compute_scale_factors(
            #         em_profile, mod_profile,apix=apix, scale_factor_arguments=scale_factor_arguments, \
            #         use_theoretical_profile=use_theoretical_profile, check_scaling=check_scaling)
                
            #######################################################################
            # Stage 2d: Get the scaled cube by applying the scale factors
            #######################################################################
            map_b_sharpened, map_b_sharpened_fft = set_radial_profile(emmap_wn, scale_factors, frequencies_map, frequency_map_window, emmap_wn.shape)
        
            #######################################################################
            # Stage 2e: For each cube, get the central voxel value of the scaled cube
            # and the bfactor information along with quality of fit
            #######################################################################
            sharpened_vals.append(map_b_sharpened[central_pix, central_pix, central_pix])
            bfactor_voxels.append(bfactor)
            qfit_voxels.append(quality_fit)
            
        except Exception as e:

            #######################################################################
            # ERROR: If any error occurs, print the error and stop the operation
            #######################################################################
            print("Rogue voxel detected!  \n")
            print("Location (kji): {},{},{} \n".format(k,j,i))
            print("Skipping this voxel for calculation \n")
            k,j,i,wn = round_up_proper(k), round_up_proper(j), round_up_proper(i), round_up_proper(wn)
            
            emmap_wn = scaling_dictionary['emmap'][k: k+wn, j: j+wn, i: i+ wn]
            modmap_wn = scaling_dictionary['modmap'][k: k+wn, j: j+wn, i: i+ wn]
        
            em_profile, frequencies_map = compute_radial_profile_proper(emmap_wn, frequency_map_window);
            mod_profile, _ = compute_radial_profile_proper(modmap_wn, frequency_map_window);
            
            print("."*80)
            print("EM profile:\n")
            print(em_profile)
            print("."*80)
            print("Model profile:\n")
            print(mod_profile)
            print("."*80)
            print("Error: \n")
            print(e)
            print(e.args)

            print("="*80)
            
            if mpi:
                print("Error occured at process: {}".format(rank))
            
            raise
        
        #### Progress bar update
        if mpi:
            if rank == 0:
                pbar.update(size)
        else:
            progress_bar.update(n=1)
    
    ###############################################################################
    # Stage 3: Save the processing files (the profile_audit file)
    ###############################################################################
    if mpi:
        if audit and scaling_dictionary['use_theoretical_profile'] and rank==0:
            import os
            
            pickle_file_output = os.path.join(temp_folder,"profiles_audit.pickle")
            with open(pickle_file_output,"wb") as audit:
                pickle.dump(profiles_audit, audit)
    else:
        if audit and scaling_dictionary['use_theoretical_profile']:
            import os
            
            pickle_file_output = os.path.join(temp_folder,"profiles_audit.pickle")
            with open(pickle_file_output,"wb") as audit:
                pickle.dump(profiles_audit, audit)

    
    ###############################################################################
    # Stage 4: Convert to numpy array and return the values
    ###############################################################################                                
    sharpened_vals_array = np.array(sharpened_vals, dtype=np.float32)
    bfactor_vals_array = np.array(bfactor_voxels, dtype=np.float32)
    qfit_vals_array = np.array(qfit_voxels, dtype=np.float32)
    
    results = {'sharpened_vals': sharpened_vals_array, 'bfactor_vals': bfactor_vals_array, 'qfit_vals': qfit_vals_array}
    return results

def run_window_function_including_scaling(parsed_inputs_dict):
    """
    This is a function which performs high level data processing for Locscale

    """
    from locscale.utils.general import get_xyz_locs_and_indices_after_edge_cropping_and_masking
    from locscale.utils.general import save_list_as_map, put_scaled_voxels_back_in_original_volume_including_padding
    from locscale.utils.general import merge_sequence_of_sequences, split_sequence_evenly, write_out_final_volume_window_back_if_required
    from joblib import Parallel, delayed
    ###############################################################################
    # Stage 1: Collect inputs from the dictionary
    ###############################################################################

    scaling_dictionary = parsed_inputs_dict
    ###############################################################################
    # Stage 2: Extract masked locations and indices from the mask
    ###############################################################################
    
    masked_xyz_locs, masked_indices, map_shape = get_xyz_locs_and_indices_after_edge_cropping_and_masking(
        scaling_dictionary['mask'], scaling_dictionary['wn'])

    masked_xyz_locs_split = split_sequence_evenly(masked_xyz_locs, scaling_dictionary['number_processes'])

    scaling_dictionary["masked_indices"] = masked_indices
    scaling_dictionary["map_shape"] = map_shape
    

    scaling_dictionary_split = {}
    for i in range(scaling_dictionary['number_processes']):
        scaling_dictionary_split[i] = scaling_dictionary.copy()
        scaling_dictionary_split[i]["masked_xyz_locs"] = masked_xyz_locs_split[i]
        scaling_dictionary_split[i]["use_mpi"] = False
    ###############################################################################
    # Stage 3: Run the window function to get sharpened values and bfactor information
    ###############################################################################
    # Use joblib to parallelize the window function 
    if scaling_dictionary['number_processes'] > 1:
        results = Parallel(n_jobs=scaling_dictionary['number_processes'])(
            delayed(get_central_scaled_pixel_vals_after_scaling)(scaling_dictionary_split[i]) for i in range(scaling_dictionary['number_processes']))
    else:
        scaling_dictionary_split[0]["use_mpi"] = False
        results = [get_central_scaled_pixel_vals_after_scaling(scaling_dictionary_split[0])]
    
    ###############################################################################
    # Stage 4: Merge the results from the parallelized window function
    ###############################################################################
    if scaling_dictionary['number_processes'] > 1:
        sharpened_vals = merge_sequence_of_sequences([results[i]['sharpened_vals'] for i in range(scaling_dictionary['number_processes'])])
        bfactor_vals = merge_sequence_of_sequences([results[i]['bfactor_vals'] for i in range(scaling_dictionary['number_processes'])])
        qfit_vals = merge_sequence_of_sequences([results[i]['qfit_vals'] for i in range(scaling_dictionary['number_processes'])])
    else:
        sharpened_vals = results[0]['sharpened_vals']
        bfactor_vals = results[0]['bfactor_vals']
        qfit_vals = results[0]['qfit_vals']


    ###############################################################################
    # Stage 5: Put the sharpened values back in the original volume
    ###############################################################################

    map_scaled = put_scaled_voxels_back_in_original_volume_including_padding(sharpened_vals, masked_indices, map_shape)
    
    ###############################################################################
    # Stage 5: Save processing files such as bfactor map and qfit maps 
    ###############################################################################
    
    bfactor_path = os.path.join(scaling_dictionary['processing_files_folder'], "bfactor_map.mrc")
    qfit_path = os.path.join(scaling_dictionary['processing_files_folder'], "qfit_map.mrc")
    bfactor_map = save_list_as_map(bfactor_vals, masked_indices, map_shape, bfactor_path, scaling_dictionary['apix'])
    qfit_map = save_list_as_map(qfit_vals, masked_indices, map_shape, qfit_path, scaling_dictionary['apix'])

    if scaling_dictionary["win_bleed_pad"]:
        #map_shape = [(LocScaleVol.shape[0] - wn), (LocScaleVol.shape[1] - wn), (LocScaleVol.shape[2] - wn)]
        from locscale.utils.general import pad_or_crop_volume
        map_shape = scaling_dictionary["original_map_shape"]
        bfactor_map = pad_or_crop_volume(bfactor_map, (map_shape))
        qfit_map = pad_or_crop_volume(qfit_map, (map_shape))
    save_as_mrc(bfactor_map, bfactor_path, scaling_dictionary['apix'])
    save_as_mrc(qfit_map, qfit_path, scaling_dictionary['apix'])

    ###############################################################################
    # Stage 6: Return the scaled map
    ###############################################################################
    return map_scaled

def run_window_function_including_scaling_mpi(parsed_inputs_dict):
    """
    This is a function which performs high level data processing for Locscale in a MPI environment

    """

    from mpi4py import MPI
    from locscale.utils.general import get_xyz_locs_and_indices_after_edge_cropping_and_masking
    from locscale.utils.general import save_list_as_map, merge_sequence_of_sequences, split_sequence_evenly
    from locscale.utils.general import put_scaled_voxels_back_in_original_volume_including_padding
                                   
    ###############################################################################
    # Stage 1: Collect inputs from the dictionary
    ###############################################################################
    scaling_dictionary_mpi = parsed_inputs_dict
    
    ###############################################################################
    # Stage 1a: Setup MPI environment
    ###############################################################################
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    ###############################################################################
    # Stage 2: Extract masked locations and indices from the mask from root node
    ###############################################################################
    if rank == 0:
        masked_xyz_locs, masked_indices, map_shape = \
        get_xyz_locs_and_indices_after_edge_cropping_and_masking(scaling_dictionary_mpi['mask'], scaling_dictionary_mpi['wn'])

        zs, ys, xs = masked_xyz_locs.T
        zs = split_sequence_evenly(zs, size)
        ys = split_sequence_evenly(ys, size)
        xs = split_sequence_evenly(xs, size)
    else:
        zs = None
        ys = None
        xs = None

    zs = comm.scatter(zs, root=0)
    ys = comm.scatter(ys, root=0)
    xs = comm.scatter(xs, root=0)

    masked_xyz_locs = np.column_stack((zs, ys, xs))

    process_name = 'LocScale process {0} of {1}'.format(rank + 1, size)
    scaling_dictionary_mpi['masked_xyz_locs'] = masked_xyz_locs
    scaling_dictionary_mpi["use_mpi"] = True
    if rank == 0:
        scaling_dictionary_mpi['masked_indices'] = masked_indices
        scaling_dictionary_mpi['map_shape'] = map_shape
        
    ###############################################################################
    # Stage 3: Run the window function to get sharpened values and bfactor information
    ###############################################################################

    results = get_central_scaled_pixel_vals_after_scaling(scaling_dictionary_mpi)
    
    ###############################################################################
    # Stage 4: Put the sharpened values back into the original volume
    ###############################################################################
    sharpened_vals = results['sharpened_vals']
    bfactor_vals = results['bfactor_vals']
    qfit_vals = results['qfit_vals']
    ###############################################################################
    # Stage 4a: Gather the computed values from all nodes to the root node
    ###############################################################################
    sharpened_vals = comm.gather(sharpened_vals, root=0)
    bfactor_vals = comm.gather(bfactor_vals, root=0)
    qfit_vals = comm.gather(qfit_vals, root=0)

    if rank == 0:
        sharpened_vals = merge_sequence_of_sequences(sharpened_vals)
        bfactor_vals = merge_sequence_of_sequences(bfactor_vals)
        qfit_vals = merge_sequence_of_sequences(qfit_vals)
        
        map_scaled = put_scaled_voxels_back_in_original_volume_including_padding(np.array(sharpened_vals),
        masked_indices, map_shape)

        ###########################################################################
        # Stage 5: Save the processing files 
        ###########################################################################
        
        print("Saving bfactor and qfist maps in here: {}".format(scaling_dictionary_mpi['processing_files_folder']))
        bfactor_path = os.path.join(scaling_dictionary_mpi['processing_files_folder'], "bfactor_map.mrc")
        qfit_path = os.path.join(scaling_dictionary_mpi['processing_files_folder'], "qfit_map.mrc")
        save_list_as_map(bfactor_vals, masked_indices, map_shape, bfactor_path, scaling_dictionary_mpi['apix'])
        save_list_as_map(qfit_vals, masked_indices, map_shape, qfit_path, scaling_dictionary_mpi['apix'])
        
    else:
        map_scaled = None

    ######## Wait for all processes to finish #########
    comm.barrier()

    ###############################################################################
    # Stage 6: Return the scaled map
    ###############################################################################
    return map_scaled, rank





#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 00:01:47 2021

@author: alok
"""

import unittest
import numpy as np
import os

class test_locscale(unittest.TestCase):
    def setUp(self):
        from locscale.utils.file_tools import get_locscale_path
        import pickle
        from locscale.include.confidenceMapUtil import FDRutil

        self.locscale = get_locscale_path()
        data_folder = os.path.join(self.locscale,"locscale",'tests','test_data') 
        self.emmap_path = os.path.join(data_folder, "emd5778_map_chainA.mrc")
        self.emmap_path_full = os.path.join(data_folder, "emd5778_map_full.mrc")
        self.mask_path = os.path.join(data_folder, "emd5778_mask_chainA.mrc")
        self.mask_path_full = os.path.join(data_folder, "emd5778_mask_full.mrc")
        self.model_coordinates = os.path.join(data_folder, "pdb3j5p_refined_chainA.pdb")
        self.reference_locscale_MB = os.path.join(data_folder, "reference_mb_locscale.mrc")
        self.reference_locscale_MF = os.path.join(data_folder, "reference_mf_locscale.mrc")
        self.resolution = 3.4
        
    def copy_files(self, file_path, tempDir):
        import os
        from subprocess import run
        run(["cp",file_path,tempDir])
        if os.path.exists(os.path.join(tempDir, os.path.basename(file_path))):               
            return os.path.join(tempDir, os.path.basename(file_path))
            
        else:
            raise UserWarning("Could not copy {} to {}".format(file_path,tempDir))
    
    def resample_map(self,emmap_path):
        from locscale.include.emmer.ndimage.map_utils import resample_map, load_map, save_as_mrc
        import os
        emmap,apix = load_map(emmap_path)
        emmap_resampled = resample_map(emmap,apix=apix,apix_new=3)
        
        resampled_map_path = os.path.join(os.path.dirname(emmap_path),"resampled_"+os.path.basename(emmap_path))
        save_as_mrc(emmap_resampled,resampled_map_path, apix=3)
        return resampled_map_path


    
    def test_run_model_based_locscale(self):
        from tempfile import TemporaryDirectory
        
        print("Testing: Model Based LocScale")
        with TemporaryDirectory() as tempDir: 
            from locscale.include.emmer.ndimage.map_tools import compute_real_space_correlation as rsc
            import os
            from subprocess import run
            
            os.chdir(tempDir)
            # copy emmap
            copied_emmap_path = self.copy_files(self.emmap_path, tempDir)
            copied_mask_path = self.copy_files(self.mask_path, tempDir)
            copied_model_coordinates = self.copy_files(self.model_coordinates, tempDir)
            
            os.chdir(tempDir)

            output_locscale_path = os.path.join(tempDir, "locscale_unittest.mrc")
            output_processing_files = "locscale_processing_files"
            locscale_script_path = os.path.join(self.locscale,"locscale","main.py")
            
            locscale_command = ["python",locscale_script_path,"--emmap_path",\
                copied_emmap_path, "--model_coordinates",copied_model_coordinates,"--mask",copied_mask_path, \
                "--outfile",output_locscale_path,"--skip_refine","--verbose",\
                "--output_processing_files",output_processing_files]
            
            locscale_test_run = run(locscale_command)
            
            self.assertTrue(os.path.exists(output_locscale_path))
            
            rscc_test = rsc(self.reference_locscale_MB,output_locscale_path)
            
            self.assertTrue(rscc_test>0.9)

    def test_MPI_run_model_based_locscale(self):
        from tempfile import TemporaryDirectory
        
        print("Testing: MPI Model Based LocScale")

        with TemporaryDirectory() as tempDir:
            from locscale.include.emmer.ndimage.map_tools import compute_real_space_correlation as rsc
            import os
            from subprocess import run
            import multiprocessing

            # copy emmap
            copied_emmap_path = self.copy_files(self.emmap_path, tempDir)
            copied_mask_path = self.copy_files(self.mask_path, tempDir)
            copied_model_coordinates = self.copy_files(self.model_coordinates, tempDir)

            os.chdir(tempDir)

            output_locscale_path = os.path.join(tempDir, "locscale_unittest.mrc")
            output_processing_files = os.path.join(tempDir,"locscale_processing_files")
            locscale_script_path = os.path.join(self.locscale,"locscale","main.py")

            ## Find number of processors
            n_proc = os.cpu_count()
            
            ## Limit to 2 processors
            if n_proc > 2:
                n_proc = 2
            
            locscale_command = ["mpirun","-np",str(n_proc),"python",locscale_script_path,"--emmap_path",\
                copied_emmap_path, "--model_coordinates",copied_model_coordinates,"--mask",copied_mask_path, \
                "--ref_resolution","3.4","--outfile",output_locscale_path,"--skip_refine","--verbose","--mpi",\
                "--output_processing_files",output_processing_files]
            
            locscale_test_run = run(locscale_command)

            self.assertTrue(os.path.exists(output_locscale_path))

            rscc_test = rsc(self.reference_locscale_MB,output_locscale_path)
            self.assertTrue(rscc_test>0.9)

    def test_run_model_free_locscale(self):
        from tempfile import TemporaryDirectory
        
        print("Testing: Model Free LocScale")
        with TemporaryDirectory() as tempDir: 
            from locscale.include.emmer.ndimage.map_tools import compute_real_space_correlation as rsc
            import os
            from subprocess import run
            
            # copy emmap
            copied_emmap_path = self.copy_files(self.emmap_path, tempDir)
            copied_mask_path = self.copy_files(self.mask_path, tempDir)
            copy_reference_locscale_MF = self.copy_files(self.reference_locscale_MF, tempDir)
                        
            os.chdir(tempDir)

            
            output_locscale_path = os.path.join(tempDir, "locscale_MF_unittest.mrc")
            locscale_script_path = os.path.join(self.locscale,"locscale","main.py")
            
            locscale_command = ["python",locscale_script_path,"--emmap_path",copied_emmap_path,\
                "--mask",copied_mask_path, "--outfile",output_locscale_path,"--ref_resolution","3.4","--verbose", "-pm_it","10","-ref_it","2"]
                        
            locscale_test_run = run(locscale_command)
            
            self.assertTrue(os.path.exists(output_locscale_path))
            
            rscc_test = rsc(copy_reference_locscale_MF,output_locscale_path)
            
            self.assertTrue(rscc_test>0.9)
    def test_model_based_integrated_locscale(self):
        from tempfile import TemporaryDirectory
        
        print("Testing: Model Based Integrated LocScale")
        with TemporaryDirectory() as tempDir: 
            from locscale.include.emmer.ndimage.map_tools import compute_real_space_correlation as rsc
            import os
            import gemmi
            from subprocess import run
            
            # copy emmap
            copied_emmap_path = self.copy_files(self.emmap_path, tempDir)
            copied_mask_path = self.copy_files(self.mask_path, tempDir)
            copied_model_coordinates = self.copy_files(self.model_coordinates, tempDir)

            # delete first few residues 
            st = gemmi.read_structure(copied_model_coordinates)
            num_atoms_original = st[0].count_atom_sites()
            chain = st[0][0]
            for i in range(250):
                chain.__delitem__(0)
            
            num_atoms_trimmed = st[0].count_atom_sites()
            print("Number of atoms in original model: ",num_atoms_original)
            print("Number of atoms in trimmed model: ",num_atoms_trimmed)
            print("Difference: ",num_atoms_original-num_atoms_trimmed)
            copied_model_coordinates_trimmed = copied_model_coordinates.replace(".pdb","_trimmed.pdb")
            st.write_pdb(copied_model_coordinates_trimmed)
                        
            os.chdir(tempDir)

            output_locscale_path = os.path.join(tempDir, "locscale_MBI_unittest.mrc")
            locscale_script_path = os.path.join(self.locscale,"locscale","main.py")
            
            locscale_command = ["python",locscale_script_path,"--emmap_path",\
                copied_emmap_path, "--model_coordinates",copied_model_coordinates_trimmed,"--mask",copied_mask_path, \
                "--outfile",output_locscale_path,"-ref_it","1","-pm_it","1","--verbose","--complete_model", "--ref_resolution", "3.4"]
            
            locscale_test_run = run(locscale_command)
            
            self.assertTrue(os.path.exists(output_locscale_path))

           
    
   
            
            
            
            
        

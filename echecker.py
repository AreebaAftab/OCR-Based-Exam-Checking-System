# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 16:34:03 2018

@author: Areeba aftab
"""

# Define if you want to download data from the original database or use the dataset one already provided and preprocessed
# Use:
# 'load': If you want to load the datase from the directory
# 'download': To download data from the database and process the images
dataset_load_method = 'download'

# Define if you want to save the dataset to a file
save_dataset = False nve,

# Define if you want to load the trained classifiers from the directory
#load_classifiers = False
load_classifiers = False


# Define if you want to save the trained classifiers to a file
#save_classifiers = True
save_classifiers = False


# Define if you want to save classification test output to a file
save_results = True
if (save_results):
    result_output_file = open('result_output.txt','w') 

# Define if you want to print errors and warnings
enable_error_output = False
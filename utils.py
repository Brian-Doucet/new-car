# Set of helper functions
import os
from glob import glob

import pandas as pd
pd.set_option('display.max_columns', 30)
pd.set_option('display.width', 250)


def file_list(file_path, pattern):
    """Return a list of files from a directory"""
    list_of_files = glob(os.path.join(file_path, pattern))
    
    return list_of_files

def combine_data(files):
    """Take a list of files and return a DataFrame"""
    df_list = [pd.read_csv(file) for file in files]
    
    # For QA purposes we want to know where the data came from
    for dataframe, filename in zip(df_list, files):
        dataframe['source_file'] = filename.split('/')[-1]
    
    combined_data = pd.concat(df_list, ignore_index=True)
    
    return combined_data


f = file_list(r'data', '*.csv')
data = combine_data(f)
print(data.head())
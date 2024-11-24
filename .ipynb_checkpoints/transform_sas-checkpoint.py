import pandas as pd
from pathlib import Path

curr_dir = Path.cwd()
# get current working directory



dataset_path = curr_dir / 'dataset'
# adding dataset folder path to current dir

print(dataset_path)

def find_file_path(directory=dataset_path, extension='XPT' ,file_name=None):
    # Create a Path object for the directory
    dir_path = Path(directory)
    extension = f'*.{extension}'
    print(extension)
    # Use glob to find all .xpt files in the directory
    xpt_files = list(dir_path.glob(extension))
    print(xpt_files)

    # Check if any .xpt files were found
    if xpt_files:
        if file_name:
            # Filter files that match the filename pattern
            matching_files = [f for f in xpt_files if file_name.lower() in f.stem.lower()]
            if matching_files:
                # Return the full path of the first matching .xpt file found
                return matching_files[0].resolve()
        else:
            # If no filename pattern is specified, return None
            return None
    
    # Return None if no matching file is found
    return None
 

if __name__ == '__main__':

    file_path = find_file_path(directory=dataset_path, extension='XPT', file_name='LLCP2023')
    # searching the file with the .xpt extension and matching filename to get the absolute path

    df = pd.read_sas(file_path, format='xport', encoding='iso-8859-1')
    # reading the sas file into pandas dataframe

    save_file_path = dataset_path / 'transformed_dataset.csv'
    # save the csv into the folder with the filename 

    df_to_csv = df.to_csv(save_file_path, encoding='utf-8', sep=',')
    #transform the dataframe into a csv file
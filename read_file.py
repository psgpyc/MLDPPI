import pandas as pd

from transform_sas import find_file_path

file_path = find_file_path(file_name='transformed_dataset', extension='csv')

df = pd.read_csv(file_path, index_col=None)
print(df.head())
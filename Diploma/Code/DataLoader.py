from pandas import read_csv, concat
from Common import LabelNames

def load_labeled_data(path):
    labeled_dataframes = [read_csv(f'{path}//{label_name}.csv', names=['id', 'project_name', 'label'], skiprows=1) for label_name in LabelNames]
    result_df = concat(labeled_dataframes)
    result_df['project_name'] = result_df['project_name'].str.strip('"')
    return result_df
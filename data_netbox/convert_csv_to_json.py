import pandas as pd
import json

def convert_data(file_csv, file_json):
    readfile_csv = pd.read_csv (r'{}' .format(file_csv))
    readfile_csv.to_json (r'{}' .format(file_json))
    with open('{}' .format(file_json)) as json_file:
        data_import = json.load(json_file)
    return data_import
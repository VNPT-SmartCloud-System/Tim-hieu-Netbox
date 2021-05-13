import pandas as pd
import json
import config

# DCIM
file_csv_dcim = config.PWD_FILE_CSV_DCIM
file_json_dcim = config.PWD_FILE_JSON_DCIM
# IPAM
file_csv_ipam = config.PWD_FILE_CSV_IPAM
file_json_ipam = config.PWD_FILE_JSON_IPAM
# Interface
file_csv_tpl = config.PWD_FILE_CSV_TPL
file_json_tpl = config.PWD_FILE_JSON_TPL
# Cable connection
file_csv_cbl = config.PWD_FILE_CSV_CABLE
file_json_cbl = config.PWD_FILE_JSON_CABLE
# IP addresses
file_csv_ip = config.PWD_FILE_CSV_IP
file_json_ip = config.PWD_FILE_JSON_IP

def convert_data_dcim():
    try:
        readfile_csv = pd.read_csv (r'{}' .format(file_csv_dcim))
        readfile_csv.to_json (r'{}' .format(file_json_dcim))
    except Exception as ex:
        print(ex)
    return

def get_json_data_dcim():
    convert_data_dcim()
    with open('{}' .format(file_json_dcim)) as json_file:
        data_dcim = json.load(json_file)
    return data_dcim

def convert_data_ipam():
    try:
        readfile_csv = pd.read_csv (r'{}' .format(file_csv_ipam))
        readfile_csv.to_json (r'{}' .format(file_json_ipam))
    except Exception as ex:
        print(ex)
    return

def get_json_data_ipam():
    convert_data_ipam()
    with open('{}' .format(file_json_ipam)) as json_file:
        data_ipam = json.load(json_file)
    return data_ipam

def convert_templates():
    try:
        readfile_csv = pd.read_csv (r'{}' .format(file_csv_tpl))
        readfile_csv.to_json (r'{}' .format(file_json_tpl))
    except Exception as ex:
        print(ex)
    return

def get_data_templates():
    convert_templates()
    with open('{}' .format(file_json_tpl)) as json_file:
        data_tpl = json.load(json_file)
    return data_tpl

def convert_data_cable():
    try:
        readfile_csv = pd.read_csv (r'{}' .format(file_csv_cbl))
        readfile_csv.to_json (r'{}' .format(file_json_cbl))
    except Exception as ex:
        print(ex)
    return

def get_data_cables():
    convert_data_cable()
    with open('{}' .format(file_json_cbl)) as json_file:
        data_cbl = json.load(json_file)
    return data_cbl

def convert_data_ipaddr():
    try:
        readfile_csv = pd.read_csv (r'{}' .format(file_csv_ip))
        readfile_csv.to_json (r'{}' .format(file_json_ip))
    except Exception as ex:
        print(ex)
    return

def get_data_ipaddr():
    convert_data_ipaddr()
    with open('{}' .format(file_json_ip)) as json_file:
        data_ipaddr = json.load(json_file)
    return data_ipaddr

def get_key_data(data):
    key_data = []
    for key, value in data.items():
        for stt in value:
            stt = int(stt)
            if stt not in key_data: 
                key_data.append(stt)
    return key_data
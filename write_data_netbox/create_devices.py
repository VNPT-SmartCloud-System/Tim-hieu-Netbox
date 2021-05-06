import pynetbox
import re
from convert_csv_to_json import convert_data
import config
import check_data_netbox

file_csv = config.PWD_FILE_CSV
file_json = config.PWD_FILE_JSON

def get_json_data():
    try:
        data = convert_data(file_csv, file_json)
    except Exception as ex:
        print(ex)
    return data

def get_key_data(data):
    key_data = []
    for key, value in data.items():
        for stt in value:
            stt = int(stt)
            if stt not in key_data: 
                key_data.append(stt)
    return key_data

def get_data_devices(numerical_order, data):
    device_type=data['device_type']['{}' .format(numerical_order)]
    device_role=data['device_role']['{}' .format(numerical_order)]
    site=data['site']['{}' .format(numerical_order)]
    rack=data['rack_name']['{}' .format(numerical_order)]
    manufacturer=data['manufacturer']['{}' .format(numerical_order)]
    manufact_id= check_data_netbox.check_manufacs(manufacturer)
    device_type_id= check_data_netbox.check_device_types(manufact_id, device_type)
    site_id = check_data_netbox.check_sites(site)
    rack_id = check_data_netbox.check_racks(rack)
    role_id = check_data_netbox.check_device_roles(device_role)
    add_data = list()
    add_data.append(
        dict (
            name= data['name']['{}' .format(numerical_order)],
            device_type= device_type_id,
            device_role= role_id,
            serial= data['serial']['{}' .format(numerical_order)],
            site= site_id,
            rack= rack_id,
            position= data['position']['{}' .format(numerical_order)],
            face= 'front',
            comments=data['comments']['{}' .format(numerical_order)],
        )
    )
    return add_data 

def create_devices(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_devices(numerical_order, data)
        try: 
            check_data_netbox.netbox.dcim.devices.create(add_data)
        except pynetbox.RequestError as e:
            print(e.error)
    return

def main():
    data = get_json_data()
    key_data = get_key_data(data)
    create_devices(key_data, data)
    return 
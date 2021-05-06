import pynetbox
from convert_csv_to_json import convert_data
import config

netbox = pynetbox.api(url=config.URL_NB, token=config.TOKEN_NB)
file_csv = config.PWD_FILE_CSV
file_json = config.PWD_FILE_JSON

try:
    data = convert_data(file_csv, file_json)
except:
    print("No data")

def check_manufacs(manufact_name):
    manufact_info = netbox.dcim.manufacturers.get(name="{}" .format(manufact_name))
    manufact_id = manufact_info['id']
    return manufact_id

def check_device_types(manufact_id, device_model):
    device_type_info = netbox.dcim.device_types.get(manufacturer_id='{}' .format(manufact_id), model='{}' .format(device_model))
    device_type_id = device_type_info['id']
    return device_type_id

def check_sites(site_name):
    site_info = netbox.dcim.sites.get(name="{}" .format(site_name))
    site_id = site_info['id']
    return site_id

def check_racks(rack_name):
    rack_info = netbox.dcim.racks.get(name="{}" .format(rack_name))
    rack_id = rack_info['id']
    return rack_id

def check_device_roles(role_name):
    device_role_info = netbox.dcim.device_roles.get(name="{}" .format(role_name))
    device_role_id = device_role_info['id']
    return device_role_id
    
def check_position_racks(rack_id):
    device_used = []
    check_device_in_racks = netbox.dcim.devices.filter(rack_id='{}' .format(rack_id))
    for device in check_device_in_racks:
        if device not in device_used:
            device_used.append(device)
    position_used = []
    for deivce_name in device_used:
        device_info = netbox.dcim.devices.get(name='{}' .format(deivce_name))
        position = device_info['position']
        manufact_id = device_info['device_type']['manufacturer']['id']
        device_model = device_info['device_type']['model']
        device_type_info = netbox.dcim.device_types.get(manufacturer_id='{}' .format(manufact_id), model='{}' .format(device_model))
        u_height = device_type_info['u_height']
        if ((position not in position_used) and ((position+u_height-1) not in position_used)): 
            position_used.extend(range (position, position+u_height))
    return position_used

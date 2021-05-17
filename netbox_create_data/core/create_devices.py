import pynetbox
from get_data_json import get_devices, get_key_data
from check_data_netbox import check_manufacs, check_device_types, check_sites, check_racks, check_device_roles, check_platforms, netbox

def get_data_devices(numerical_order, data):
    device_type=data['device_type']['{}' .format(numerical_order)]
    device_role=data['device_role']['{}' .format(numerical_order)]
    site=data['site']['{}' .format(numerical_order)]
    rack=data['rack']['{}' .format(numerical_order)]
    manufacturer=data['manufacturer']['{}' .format(numerical_order)]
    platform=data['platform']['{}' .format(numerical_order)]
    platform_id=check_platforms(platform)
    manufact_id= check_manufacs(manufacturer)
    device_type_id= check_device_types(manufact_id, device_type)
    site_id = check_sites(site)
    rack_id = check_racks(rack)
    role_id = check_device_roles(device_role)
    add_data = list()
    add_data.append(
        dict (
            name= data['name']['{}' .format(numerical_order)],
            device_type= device_type_id,
            device_role= role_id,
            platform= platform_id,
            serial= data['serial']['{}' .format(numerical_order)],
            asset_tag= data['asset_tag']['{}' .format(numerical_order)],
            site= site_id,
            rack= rack_id,
            position= data['position']['{}' .format(numerical_order)],
            face= data['face']['{}' .format(numerical_order)],
            status= data['status']['{}' .format(numerical_order)],
            comments=data['comments']['{}' .format(numerical_order)],
        )
    )
    return add_data

def create_devices(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_devices(numerical_order, data)
        try: 
            netbox.dcim.devices.create(add_data)
        except pynetbox.RequestError as e:
            print(e.error)
    return

def create_devices_main():
    data = get_devices()
    key_data = get_key_data(data)
    create_devices(key_data, data)
    return 
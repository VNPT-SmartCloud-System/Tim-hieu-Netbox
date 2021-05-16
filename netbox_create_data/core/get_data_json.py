import config
import json

regions_json=config.REGIONS_JSON
sites_json=config.SITES_JSON
racks_json=config.RACK_JSON
device_types_json=config.DEVICE_TYPES_JSON
device_roles_json = config.DEIVE_ROLE_JSON
devices_json=config.DEVICES_JSON
vlans_json=config.VLANS_JSON
aggregates_json = config.AGGREGATES_JSON
prefixes_json=config.PREFIXES_JSON
interface_tpl_json=config.INTERFACE_TPL
cable_connections_json=config.CABLE_CONNECT

def get_regions():
    from convert_csv_to_json import convert_region
    convert_region()
    with open('{}' .format(regions_json)) as json_file:
        data_region = json.load(json_file)
    return data_region

def get_sites():
    from convert_csv_to_json import convert_site
    convert_site()
    with open('{}' .format(sites_json)) as json_file:
        data_site = json.load(json_file)
    return data_site

def get_racks():
    from convert_csv_to_json import convert_rack
    convert_rack()
    with open('{}' .format(racks_json)) as json_file:
        data_rack = json.load(json_file)
    return data_rack

def get_device_types():
    from convert_csv_to_json import convert_device_type
    convert_device_type()
    with open('{}' .format(device_types_json)) as json_file:
        data_device_type = json.load(json_file)
    return data_device_type

def get_device_roles():
    from convert_csv_to_json import convert_device_role
    convert_device_role()
    with open('{}' .format(device_roles_json)) as json_file:
        data_device_role = json.load(json_file)
    return data_device_role

def get_devices():
    from convert_csv_to_json import convert_device
    convert_device()
    with open('{}' .format(devices_json)) as json_file:
        data_device = json.load(json_file)
    return data_device

def get_vlans():
    from convert_csv_to_json import convert_vlans
    convert_vlans()
    with open('{}' .format(vlans_json)) as json_file:
        data_vlan = json.load(json_file)
    return data_vlan

def get_aggregates():
    from convert_csv_to_json import convert_aggregates
    convert_aggregates()
    with open('{}' .format(aggregates_json)) as json_file:
        data_aggregate = json.load(json_file)
    return data_aggregate

def get_prefixes():
    from convert_csv_to_json import convert_prefix
    convert_prefix()
    with open('{}' .format(prefixes_json)) as json_file:
        data_preifx = json.load(json_file)
    return data_preifx

def get_inf_tpls():
    from convert_csv_to_json import convert_inf_tpl
    convert_inf_tpl()
    with open('{}' .format(interface_tpl_json)) as json_file:
        data_inf_tpl = json.load(json_file)
    return data_inf_tpl

def get_cables():
    from convert_csv_to_json import convert_cable_connect
    convert_cable_connect()
    with open('{}' .format(cable_connections_json)) as json_file:
        data_cable = json.load(json_file)
    return data_cable

def get_key_data(data):
    key_data = []
    for key, value in data.items():
        for stt in value:
            stt = int(stt)
            if stt not in key_data: 
                key_data.append(stt)
    return key_data
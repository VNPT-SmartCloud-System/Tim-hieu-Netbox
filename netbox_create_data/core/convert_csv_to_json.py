'''
Module này chứa các funtion để convert thông tin các sheet trong file excel thành json
    sau đó lưu vào các file json đã tạo trước đó.
'''
import pandas as ps
import config

# Lấy file excel và các file json từ config
netbox_excel_data = config.NETBOX_INFO_EXCEL
regions_sites_json=config.REGION_SITE_JSON
racks_json=config.RACK_JSON
device_types_json=config.DEVICE_TYPES_JSON
device_roles_json = config.DEIVE_ROLE_JSON
devices_json=config.DEVICES_JSON
aggregates_json = config.AGGREGATES_JSON
interface_tpl_json=config.INTERFACE_TPL
cable_connections_json=config.CABLE_CONNECT
vlans_json=config.VLANS_JSON
platform_json=config.PLATFORM

# Lấy thông tin về tên sheet
regions_sites = config.regions_sites
racks = config.racks
device_types = config.device_types
inf_template = config.inf_template
device_roles = config.device_roles
devices = config.devices
aggregates= config.aggregates
vlans = config.vlans
cable_ip = config.cable_ip
platform = config.platform

def convert_region_site():
    try:
        excel_data_df = ps.read_excel('{}' .format(netbox_excel_data),
                                      sheet_name='{}' .format(regions_sites),
                                      engine='openpyxl')
        excel_data_df.to_json('{}' .format(regions_sites_json))
    except Exception as ex:
        print(ex)
    return

def convert_rack():
    try:
        excel_data_df = ps.read_excel('{}' .format(netbox_excel_data),
                                      sheet_name='{}' .format(racks),
                                      engine='openpyxl')
        excel_data_df.to_json('{}' .format(racks_json))
    except Exception as ex:
        print(ex)
    return

def convert_device_type():
    try:
        excel_data_df = ps.read_excel('{}' .format(netbox_excel_data),
                                      sheet_name='{}' .format(device_types),
                                      engine='openpyxl')
        excel_data_df.to_json('{}' .format(device_types_json))
    except Exception as ex:
        print(ex)
    return

def convert_device_role():
    try:
        excel_data_df = ps.read_excel('{}' .format(netbox_excel_data),
                                      sheet_name='{}' .format(device_roles),
                                      engine='openpyxl')
        excel_data_df.to_json('{}' .format(device_roles_json))
    except Exception as ex:
        print(ex)
    return

def convert_device():
    try:
        excel_data_df = ps.read_excel('{}' .format(netbox_excel_data),
                                      sheet_name='{}' .format(devices),
                                      engine='openpyxl')
        excel_data_df.to_json('{}' .format(devices_json))
    except Exception as ex:
        print(ex)
    return

def convert_vlans():
    try:
        excel_data_df = ps.read_excel('{}' .format(netbox_excel_data),
                                      sheet_name='{}' .format(vlans),
                                      engine='openpyxl')
        excel_data_df.to_json('{}' .format(vlans_json))
    except Exception as ex:
        print(ex)
    return

def convert_aggregates():
    try:
        excel_data_df = ps.read_excel('{}' .format(netbox_excel_data),
                                      sheet_name='{}' .format(aggregates),
                                      engine='openpyxl')
        excel_data_df.to_json('{}' .format(aggregates_json))
    except Exception as ex:
        print(ex)
    return

# def convert_prefix():
#     try:
#         excel_data_df = ps.read_excel('{}' .format(netbox_excel_data),
#                                       sheet_name='prefixes',
#                                       engine='openpyxl')
#         excel_data_df.to_json('{}' .format(prefixes_json))
#     except Exception as ex:
#         print(ex)
#     return

def convert_inf_tpl():
    try:
        excel_data_df = ps.read_excel('{}' .format(netbox_excel_data),
                                      sheet_name='{}' .format(inf_template),
                                      engine='openpyxl')
        excel_data_df.to_json('{}' .format(interface_tpl_json))
    except Exception as ex:
        print(ex)
    return

def convert_cable_connect():
    try:
        excel_data_df = ps.read_excel('{}' .format(netbox_excel_data),
                                      sheet_name='{}' .format(cable_ip),
                                      engine='openpyxl')
        excel_data_df = excel_data_df.fillna(method='ffill', axis=0)
        excel_data_df.to_json('{}' .format(cable_connections_json))
    except Exception as ex:
        print(ex)
    return

# def convert_ip_addr():
#     try:
#         excel_data_df = ps.read_excel('{}' .format(netbox_excel_data),
#                                       sheet_name='ip_addresses',
#                                       engine='openpyxl')
#         excel_data_df.to_json('{}' .format(ip_addr_json))
#     except Exception as ex:
#         print(ex)
#     return

def convert_platform():
    try:
        excel_data_df = ps.read_excel('{}' .format(netbox_excel_data),
                                      sheet_name='{}' .format(platform),
                                      engine='openpyxl')
        excel_data_df.to_json('{}' .format(platform_json))
    except Exception as ex:
        print(ex)
    return
import pynetbox
from get_data_json import get_devices, get_key_data
from check_data_netbox import check_manufacs, check_tenants, check_device_types, check_sites, check_racks, check_device_roles, check_platforms, netbox

def get_data_devices(numerical_order, data):
    device_type=data['Kiểu thiết bị']['{}' .format(numerical_order)]
    device_role=data['Tên vai trò thiết bị']['{}' .format(numerical_order)]
    site=data['Tên DC']['{}' .format(numerical_order)]
    rack=data['Tên rack']['{}' .format(numerical_order)]
    manufacturer=data['Nhà sản xuất']['{}' .format(numerical_order)]
    platform=data['Hệ điều hành']['{}' .format(numerical_order)]
    device_name = data['Tên thiết bị']['{}' .format(numerical_order)]
    if device_name == None or device_type == None:
        add_data = None
    else:
        if platform == None:
            platform_id = None
        else: 
            platform_id=check_platforms(platform)
        tenant_name = data['Người sở hữu']['{}' .format(numerical_order)]
        if tenant_name == None:
            tenant_id = None
        else:
            tenant_id = check_tenants(tenant_name)
        manufact_id= check_manufacs(manufacturer)
        device_type_id= check_device_types(manufact_id, device_type)
        site_id = check_sites(site)
        rack_id = check_racks(rack)
        role_id = check_device_roles(device_role)
        add_data = list()
        add_data.append(
            dict (
                name= device_name,
                device_type= device_type_id,
                device_role= role_id,
                tenant = tenant_id,
                platform= platform_id,
                serial= data['Serial']['{}' .format(numerical_order)],
                asset_tag= data['Mã tài sản']['{}' .format(numerical_order)],
                site= site_id,
                rack= rack_id,
                position= data['Vị trí trên rack']['{}' .format(numerical_order)],
                face= data['Rack face']['{}' .format(numerical_order)],
                status= data['Trạng thái']['{}' .format(numerical_order)],
                comments=data['Ghi chú']['{}' .format(numerical_order)],
            )
        )
    return add_data

def create_devices(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_devices(numerical_order, data)
        if add_data == None:
            continue
        else:
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
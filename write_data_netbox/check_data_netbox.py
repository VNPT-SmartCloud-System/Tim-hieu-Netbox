import pynetbox
import config
import create_sites
import create_rack_groups
import create_racks
import create_rack_roles
netbox = pynetbox.api(url=config.URL_NB, token=config.TOKEN_NB)

def check_manufacs(manufact_name):
    manufact_info = netbox.dcim.manufacturers.get(name="{}" .format(manufact_name))
    manufact_id = manufact_info['id']
    return manufact_id

def check_sites(site_name):
    site_info = netbox.dcim.sites.get(name="{}" .format(site_name))
    if site_info == None:
        create_sites.create_site_main()
        site_info1 = netbox.dcim.sites.get(name="{}" .format(site_name))
        site_id = site_info1['id']
    else:
        site_id = site_info['id']
    return site_id

def check_regions(region_name):
    region_info = netbox.dcim.regions.get(name="{}" .format(region_name))
    region_id = region_info['id']
    return region_id

def check_racks(rack_name):
    rack_info = netbox.dcim.racks.get(name="{}" .format(rack_name))
    if rack_info == None:
        create_racks.create_rack_main()
        rack_info1 = netbox.dcim.racks.get(name="{}" .format(rack_name))
        rack_id = rack_info1['id']
    else:
        rack_id = rack_info['id']
    return rack_id

def check_rack_roles(role_name):
    rack_role_info = netbox.dcim.rack_roles.get(name="{}" .format(role_name))
    if rack_role_info == None:
        create_rack_roles.create_rack_role_main()
        rack_role_info1=netbox.dcim.rack_roles.get(name="{}" .format(role_name))
        rack_role_id = rack_role_info1['id']
    else:
        rack_role_id = rack_role_info['id']
    return rack_role_id

def check_rack_group(group_name):
    rack_group_info = netbox.dcim.rack_groups.get(name="{}" .format(group_name))
    if rack_group_info == None:
        create_rack_groups.create_rack_group_main()
        rack_group_info1 = netbox.dcim.sites.get(name="{}" .format(group_name))
        rack_group_id = rack_group_info1['id']
    else:
        rack_group_id = rack_group_info['id']
    return rack_group_id

def check_device_types(manufact_id, device_model):
    device_type_info = netbox.dcim.device_types.get(manufacturer_id='{}' .format(manufact_id), model='{}' .format(device_model))
    device_type_id = device_type_info['id']
    return device_type_id

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
        else: 
            print("Vị Trí Đã Có Thiết Bị Được Đặt")
    return position_used

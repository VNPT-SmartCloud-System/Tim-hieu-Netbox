import pynetbox
import config

netbox = pynetbox.api(url=config.URL_NB, token=config.TOKEN_NB)

def check_manufacs(manufact_name):
    """
    Từ thông tin manufacturers trả về thông tin id của manufacturers,
        nếu thông tin manufacturer trống, tạo manufacturer
    """
    import create_manufacturers
    manufact_info = netbox.dcim.manufacturers.get(name="{}" .format(manufact_name))
    if manufact_info == None:
        create_manufacturers.create_manufacs_main()
        manufact_info1 = netbox.dcim.manufacturers.get(name="{}" .format(manufact_name))
        manufact_id = manufact_info1['id']
    else:
        manufact_id = manufact_info['id']
    return manufact_id

def check_tenants(tenant_name):
    """
    Từ thông tin tenants trả về thông tin id của tenants,
        nếu thông tin tenants trống, tạo tenants
    """
    from create_tenancy import create_tenants_main
    tenant_info = netbox.tenancy.tenants.get(name="{}" .format(tenant_name))
    if tenant_info == None:
        create_tenants_main()
        tenant_info1 = netbox.tenancy.tenants.get(name="{}" .format(tenant_name))
        tenant_id = tenant_info1['id']
    else:
        tenant_id = tenant_info['id']
    return tenant_id

def check_sites(site_name):
    """
    Từ thông tin sites trả về thông tin id của sites,
        nếu thông tin sites trống, tạo sites
    """
    import create_sites
    site_info = netbox.dcim.sites.get(name="{}" .format(site_name))
    if site_info == None:
        create_sites.create_site_main()
        site_info1 = netbox.dcim.sites.get(name="{}" .format(site_name))
        site_id = site_info1['id']
    else:
        site_id = site_info['id']
    return site_id

def check_regions(region_name):
    """
    Từ thông tin regions trả về thông tin id của regions,
        nếu thông tin regions trống, tạo regions
    """
    from create_regions import create_region_main
    region_info = netbox.dcim.regions.get(name="{}" .format(region_name))
    if region_info == None:
        create_region_main()
        region_info1 = netbox.dcim.regions.get(name="{}" .format(region_name))
        region_id = region_info1['id']
    else:
        region_id = region_info['id']
    return region_id

def check_racks(rack_name):
    """
    Từ thông tin racks trả về thông tin id của racks,
        nếu thông tin racks trống, tạo racks
    """
    import create_racks
    rack_info = netbox.dcim.racks.get(name="{}" .format(rack_name))
    if rack_info == None:
        create_racks.create_rack_main()
        rack_info1 = netbox.dcim.racks.get(name="{}" .format(rack_name))
        rack_id = rack_info1['id']
    else:
        rack_id = rack_info['id']
    return rack_id

def check_rack_roles(role_name):
    """
    Từ thông tin Rack roles trả về thông tin id của Rack roles,
        nếu thông tin Rack roles trống, tạo Rack roles
    """
    import create_rack_roles
    rack_role_info = netbox.dcim.rack_roles.get(name="{}" .format(role_name))
    if rack_role_info == None:
        create_rack_roles.create_rack_role_main()
        rack_role_info1=netbox.dcim.rack_roles.get(name="{}" .format(role_name))
        rack_role_id = rack_role_info1['id']
    else:
        rack_role_id = rack_role_info['id']
    return rack_role_id

def check_rack_group(group_name, site):
    """
    Từ thông tin Rack group trả về thông tin id của Rack group,
        nếu thông tin Rack group trống, tạo Rack group
    """
    from create_rack_groups import create_rack_group_main
    rack_group_info = netbox.dcim.rack_groups.get(name="{}" .format(group_name), site_id= site)
    if rack_group_info == None:
        create_rack_group_main()
        rack_group_info1 = netbox.dcim.rack_groups.get(name="{}" .format(group_name), site_id= site)
        rack_group_id = rack_group_info1['id']
    else:
        rack_group_id = rack_group_info['id']
    return rack_group_id

def check_device_types(manufact_id, device_model):
    """
    Từ thông tin Device type trả về thông tin id của Device type,
        nếu thông tin Device type trống, tạo Device type
    """
    import create_device_types
    import create_interface_tpl
    device_type_info = netbox.dcim.device_types.get(manufacturer_id='{}' .format(manufact_id), model='{}' .format(device_model))
    if device_type_info == None:
        create_device_types.create_device_type_main()
        create_interface_tpl.create_inf_template_main()
        device_type_info1 = netbox.dcim.device_types.get(manufacturer_id='{}' .format(manufact_id), model='{}' .format(device_model))
        device_type_id = device_type_info1['id']
    else:
        device_type_id = device_type_info['id']
    return device_type_id

def check_device_roles(role_name):
    """
    Từ thông tin Device role trả về thông tin id của Device role,
        nếu thông tin Device role trống, tạo Device role
    """
    import create_device_roles
    device_role_info = netbox.dcim.device_roles.get(name="{}" .format(role_name))
    if device_role_info == None:
        create_device_roles.create_device_role_main()
        device_role_info1 = netbox.dcim.device_roles.get(name="{}" .format(role_name))
        device_role_id = device_role_info1['id']
    else:
        device_role_id = device_role_info['id']
    return device_role_id

def check_platforms(name):
    """
    Từ thông tin platforms trả về thông tin id của platforms,
        nếu thông tin platforms trống, tạo platforms
    """
    import create_platforms
    platform_info = netbox.dcim.platforms.get(name="{}" .format(name))
    if platform_info == None:
        create_platforms.create_platforms_main()
        platform_info1 = netbox.dcim.platforms.get(name="{}" .format(name))
        platform_id = platform_info1['id']
    else:
        platform_id = platform_info['id']
    return platform_id

def check_position_racks(rack_id):
    """
    Kiểm tra vị trí còn trống trên tủ rack
    """
    device_used = []
    check_device_in_racks = netbox.dcim.devices.filter(rack_id='{}' .format(rack_id))
    for device in check_device_in_racks:
        # Lấy ra các device đang đặt trên rack và lưu vào device_used
        if device not in device_used:
            device_used.append(device)
    position_used = []
    for deivce_name in device_used:
        # Lấy ra các vị trí u đã sử dụng và lưu vào position_used
        device_info = netbox.dcim.devices.get(name='{}' .format(deivce_name))
        position = device_info['position']
        manufact_id = device_info['device_type']['manufacturer']['id']
        device_model = device_info['device_type']['model']
        device_type_info = netbox.dcim.device_types.get(manufacturer_id='{}' .format(manufact_id), model='{}' .format(device_model))
        u_height = device_type_info['u_height']
        if ((position not in position_used) and ((position+u_height-1) not in position_used)): 
            position_used.extend(range (position, position+u_height))
        else:
            print("Vị Trí {} Đã Có Thiết Bị Được Đặt" .format(position))
    return position_used

def check_vlan_group(vgroup_name):
    """
    Từ thông tin vlan group trả về thông tin id của vlan group,
        nếu thông tin vlan group trống, tạo vlan group
    """
    import create_vlan_groups
    vlan_group_info = netbox.ipam.vlan_groups.get(name="{}" .format(vgroup_name))
    if vlan_group_info == None:
        create_vlan_groups.create_vlan_group_main()
        vlan_group_info1 = netbox.ipam.vlan_groups.get(name="{}" .format(vgroup_name))
        vlan_group_id = vlan_group_info1['id']
    else:
        vlan_group_id = vlan_group_info['id']
    return vlan_group_id

def check_vlan(vlan_name, site_id):
    """
    Từ thông tin vlan trả về thông tin id của vlan,
        nếu thông tin vlantrống, tạo vlan
    """
    import create_vlans
    vlan_info = netbox.ipam.vlans.get(name="{}" .format(vlan_name), site_id = "{}" .format(site_id))
    if vlan_info == None:
        create_vlans.create_vlan_main()
        vlan_info1 = netbox.ipam.vlans.get(name="{}" .format(vlan_name), site_id = "{}" .format(site_id))
        vlan_id = vlan_info1['id']
    else:
        vlan_id = vlan_info['id']
    return vlan_id

def check_rir(rir_name):
    """
    Từ thông tin rir trả về thông tin id của rir,
        nếu thông tin rir trống, tạo rir
    """
    import create_rirs
    rir_info = netbox.ipam.rirs.get(name="{}" .format(rir_name))
    if rir_info == None:
        create_rirs.create_rir_main()
        rir_info1 = netbox.ipam.rirs.get(name="{}" .format(rir_name))
        rir_id = rir_info1['id']
    else:
        rir_id = rir_info['id']
    return rir_id

def check_prefix_role(role_name):
    """
    Từ thông tin prefix role trả về thông tin id của prefix role,
        nếu thông tin prefix role trống, tạo prefix role
    """
    import create_prefixe_roles
    prefix_role_info = netbox.ipam.roles.get(name="{}" .format(role_name))
    if prefix_role_info == None:
        create_prefixe_roles.create_prefix_role_main()
        prefix_role_info1 = netbox.ipam.roles.get(name="{}" .format(role_name))
        role_id = prefix_role_info1['id']
    else:
        role_id = prefix_role_info['id']
    return role_id

def check_interface(device_name, inf_name):
    """
    Từ thông tin interface trên device trả về thông tin id của interface
    """
    try:
        interface_info = netbox.dcim.interfaces.get(device='{}' .format(device_name), name='{}' .format(inf_name))
        interface_id = interface_info['id']
        return interface_id
    except Exception as ex:
        print(ex)
import pynetbox
from check_data_netbox import check_sites, check_rack_group, check_rack_roles, netbox
from get_data_json import get_racks, get_key_data

def get_data_rack(numerical_order, data):
    site_name = data['site']['{}' .format(numerical_order)]
    site_id = check_sites(site_name)
    group_name = data['group']['{}' .format(numerical_order)]
    rack_group_id = check_rack_group(group_name)
    rack_role = data['role']['{}' .format(numerical_order)]
    rack_role_id = check_rack_roles(rack_role)
    add_data = list()
    add_data.append(
        dict (
            name= data['rack_name']['{}' .format(numerical_order)],
            site= site_id,
            group= rack_group_id,
            status= data['status']['{}' .format(numerical_order)],
            role= rack_role_id,
            serial= data['serial']['{}' .format(numerical_order)],
            asset_tag= data['asset_tag']['{}' .format(numerical_order)],
            type= data['type']['{}' .format(numerical_order)],
            width= data['width']['{}' .format(numerical_order)],
            outer_width= data['outer_width']['{}' .format(numerical_order)],
            outer_depth= data['outer_depth']['{}' .format(numerical_order)],
            outer_unit= data['outer_unit']['{}' .format(numerical_order)],
            comments= data['comments']['{}' .format(numerical_order)],
            u_height= data['u_height']['{}' .format(numerical_order)],
        )
    )
    return add_data

def create_rack(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_rack(numerical_order, data)
        try: 
            netbox.dcim.racks.create(add_data)
        except pynetbox.RequestError as e:
            print(e.error)
    return

def create_rack_main():
    data = get_racks()
    key_data = get_key_data(data)
    create_rack(key_data, data)
    return
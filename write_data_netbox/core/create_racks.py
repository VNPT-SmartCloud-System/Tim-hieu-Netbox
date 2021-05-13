import pynetbox
from check_data_netbox import check_sites, check_rack_group, check_rack_roles, netbox
from convert_csv_to_json import get_json_data_dcim, get_key_data

def get_data_rack(numerical_order, data):
    site_name = data['site']['{}' .format(numerical_order)]
    site_id = check_sites(site_name)
    group_name = data['rack_group']['{}' .format(numerical_order)]
    rack_group_id = check_rack_group(group_name)
    rack_role = data['rack_role']['{}' .format(numerical_order)]
    rack_role_id = check_rack_roles(rack_role)
    add_data = list()
    add_data.append(
        dict (
            name= data['rack_name']['{}' .format(numerical_order)],
            site= site_id,
            group= rack_group_id,
            role= rack_role_id,
            u_height= data['rack_u_height']['{}' .format(numerical_order)],
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
    data = get_json_data_dcim()
    key_data = get_key_data(data)
    create_rack(key_data, data)
    return
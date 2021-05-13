import pynetbox
from convert_csv_to_json import get_json_data_ipam, get_key_data
from check_data_netbox import check_sites, check_vlan, check_prefix_role, netbox

def get_data_prefix(numerical_order, data):
    site_name= data['site']['{}' .format(numerical_order)]
    site_id = check_sites(site_name)
    vlan_name= data['vlan_name']['{}' .format(numerical_order)]
    vlan_id = check_vlan(vlan_name)
    role_name = data['role']['{}' .format(numerical_order)]
    role_id = check_prefix_role(role_name)
    add_data = list()
    add_data.append(
        dict (
            prefix= data['prefix']['{}' .format(numerical_order)],
            site= site_id,
            vlan= vlan_id,
            status= data['status']['{}' .format(numerical_order)],
            role= role_id,
        )
    )
    return add_data

def create_prefix(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_prefix(numerical_order, data)
        try: 
            netbox.ipam.prefixes.create(add_data)
        except pynetbox.RequestError as e:
            print(e.error)
    return

def create_prefix_main():
    data = get_json_data_ipam()
    key_data = get_key_data(data)
    create_prefix(key_data, data)
    return
import pynetbox
from convert_csv_to_json import get_json_data_ipam, get_key_data
from check_data_netbox import check_sites, netbox

def get_data_vlan_group(numerical_order, data):
    site_name=data['site']['{}' .format(numerical_order)]
    site_id = check_sites(site_name)
    add_data = list()
    add_data.append(
        dict (
            name= data['vlan_group']['{}' .format(numerical_order)],
            slug= data['vlan_group_slug']['{}' .format(numerical_order)],
            site= site_id,
        )
    )
    return add_data

def create_vlan_group(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_vlan_group(numerical_order, data)
        try:
            netbox.ipam.vlan_groups.create(add_data)
        except pynetbox.RequestError as e:
            print(e.error)
    return

def create_vlan_group_main():
    data = get_json_data_ipam()
    key_data = get_key_data(data)
    create_vlan_group(key_data, data)
    return
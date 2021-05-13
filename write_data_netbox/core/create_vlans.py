import pynetbox
from convert_csv_to_json import get_json_data_ipam, get_key_data
from check_data_netbox import check_sites, check_vlan_group, netbox

def get_data_vlan(numerical_order, data):
    site_name=data['site']['{}' .format(numerical_order)]
    site_id = check_sites(site_name)
    group_name =data['vlan_group']['{}' .format(numerical_order)]
    group_id = check_vlan_group(group_name)
    add_data = list()
    add_data.append(
        dict (
            name= data['vlan_name']['{}' .format(numerical_order)],
            group= group_id,
            site= site_id,
            vid= data['vlan']['{}' .format(numerical_order)],
            status = data['status']['{}' .format(numerical_order)],
        )
    )
    return add_data

def create_vlan(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_vlan(numerical_order, data)
        try: 
            netbox.ipam.vlans.create(add_data)
        except pynetbox.RequestError as e:
            print(e.error)
    return

def create_vlan_main():
    data = get_json_data_ipam()
    key_data = get_key_data(data)
    create_vlan(key_data, data)
    return
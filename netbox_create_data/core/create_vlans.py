import pynetbox
from get_data_json import get_vlans, get_key_data
from check_data_netbox import check_sites, check_vlan_group, check_prefix_role, netbox

def get_data_vlan(numerical_order, data):
    site_name=data['Tên DC']['{}' .format(numerical_order)]
    vlan_id = data['Vlan id']['{}' .format(numerical_order)]
    vlan_name = data['VLAN']['{}' .format(numerical_order)]
    if vlan_id == None or vlan_name == None:
        add_data = None
    else:
        site_id = check_sites(site_name)
        # group_name =data['vlan_group']['{}' .format(numerical_order)]
        # group_id = check_vlan_group(group_name)
        # role_name = data['role']['{}' .format(numerical_order)]
        # role_id = check_prefix_role(role_name)
        add_data = list()
        add_data.append(
            dict (
                site= site_id,
                # group= group_id,
                vid= vlan_id,
                name= vlan_name,
                status = 'active',
                # role = role_id,
            )
        )
    return add_data

def create_vlan(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_vlan(numerical_order, data)
        if add_data == None:
            continue
        else:
            try: 
                netbox.ipam.vlans.create(add_data)
            except pynetbox.RequestError as e:
                print(e.error)
    return

def create_vlan_main():
    data = get_vlans()
    key_data = get_key_data(data)
    create_vlan(key_data, data)
    return
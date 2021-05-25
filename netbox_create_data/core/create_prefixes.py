import pynetbox
from get_data_json import get_vlans, get_key_data
from check_data_netbox import check_sites, check_vlan, check_prefix_role, netbox

def get_data_prefix(numerical_order, data):
    site_name= data['Tên DC']['{}' .format(numerical_order)]
    prefix_vlan = data['Prefix']['{}' .format(numerical_order)]
    vlan_name= data['VLAN']['{}' .format(numerical_order)]
    if prefix_vlan == None or vlan_name == None:
        add_data = None
    else:
        prefix_inf = netbox.ipam.prefixes.get(prefix='{}' .format(prefix_vlan))
        if prefix_inf == None:
            site_id = check_sites(site_name)
            vlan_id = check_vlan(vlan_name, site_id)
            # role_name = data['role']['{}' .format(numerical_order)]
            # role_id = check_prefix_role(role_name)
            add_data = list()
            add_data.append(
                dict (
                    prefix= prefix_vlan,
                    site= site_id,
                    vlan= vlan_id,
                    status= 'active',
                    # role= role_id,
                    is_pool = 'false',
                )
            )
        else:
            add_data = None
    return add_data

def create_prefix(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_prefix(numerical_order, data)
        if add_data == None:
            continue
        else:
            try:
                netbox.ipam.prefixes.create(add_data)
            except pynetbox.RequestError as e:
                print(e.error)
    return

def create_prefix_main():
    from create_aggregates import create_aggregates_main
    create_aggregates_main()
    data = get_vlans()
    key_data = get_key_data(data)
    create_prefix(key_data, data)
    return
# create_prefix_main()
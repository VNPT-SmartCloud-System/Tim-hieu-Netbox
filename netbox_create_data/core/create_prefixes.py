import pynetbox
import contextlib
from get_data_json import get_vlans, get_key_data
from check_data_netbox import check_sites, check_vlan, check_prefix_role, netbox

def get_data_prefix(numerical_order, data):
    site_name= data['Tên DC']['{}' .format(numerical_order)]
    prefix_vlan = data['Prefix']['{}' .format(numerical_order)]
    vlan_name= data['VLAN']['{}' .format(numerical_order)]
    if prefix_vlan == None or vlan_name == None:
        add_data = None
        vlan_id = None
    else:
        prefix_inf = netbox.ipam.prefixes.get(prefix='{}' .format(prefix_vlan))
        try:
            site_id = check_sites(site_name)
            vlan_id = check_vlan(vlan_name, site_id)
        except:
            line_in_excel = int(numerical_order) + 2
            print("[TẠO PREFIX] - dòng {}: add prefixes false" .format(line_in_excel))
            print("Tên DC: {} hoặc Tên vlan: {} sai" .format(site_name, vlan_name))
        if prefix_inf == None:
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
    return add_data, vlan_id

def create_prefix(key_data, data):
    for numerical_order in key_data:
        add_data, vlan_id = get_data_prefix(numerical_order, data)
        if add_data == None or vlan_id == None:
            # line_in_excel = int(numerical_order) + 2
            # print("[TẠO PREFIX] - dòng {}: add prefixes false" .format(line_in_excel))
            continue
        else:
            try:
                with open('/var/log/logrunning.log', 'w') as f:
                    with contextlib.redirect_stdout(f):
                        netbox.ipam.prefixes.create(add_data)
                line_in_excel = int(numerical_order) + 2
                print("[TẠO PREFIX] - dòng {}: add prefixes success" .format(line_in_excel))
            except pynetbox.RequestError as e:
                with open('/var/log/logrunning.log', 'w') as f:
                    with contextlib.redirect_stdout(f):
                        print(e.error)
    return

def create_prefix_main():
    from create_aggregates import create_aggregates_main
    create_aggregates_main()
    data = get_vlans()
    key_data = get_key_data(data)
    try:
        create_prefix(key_data, data)
        print("Tạo prefix thành công")
    except:
        print("Tạo prefix lỗi")
    return
# create_prefix_main()
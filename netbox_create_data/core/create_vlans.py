import pynetbox
import contextlib
from get_data_json import get_vlans, get_key_data
from check_data_netbox import check_sites, check_vlan_group, check_prefix_role, netbox

def get_data_vlan(numerical_order, data):
    site_name=data['Tên DC']['{}' .format(numerical_order)]
    vlan_id = data['Vlan id']['{}' .format(numerical_order)]
    vlan_name = data['VLAN']['{}' .format(numerical_order)]
    if vlan_id == None or vlan_name == None:
        add_data = None
    else:
        try:
            site_id = check_sites(site_name)
        except:
            line_in_excel = int(numerical_order) + 2
            print("[TẠO VLAN] - dòng {}, add vlan false" .format(line_in_excel))
            print("Lỗi tên DC: {}" .format(site_name))
        vlan_inf = netbox.ipam.vlans.get(name="{}" .format(vlan_name), site_id = "{}" .format(site_id))
        # group_name =data['vlan_group']['{}' .format(numerical_order)]
        # group_id = check_vlan_group(group_name)
        # role_name = data['role']['{}' .format(numerical_order)]
        # role_id = check_prefix_role(role_name)
        if vlan_inf == None:
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
        else:
            add_data = None
    return add_data

def create_vlan(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_vlan(numerical_order, data)
        if add_data == None:
            # line_in_excel = int(numerical_order) + 2
            # print("[TẠO VLAN] - dòng {} add vlan false" .format(line_in_excel))
            continue
        else:
            try:
                with open('/var/log/logrunning.log', 'w') as f:
                    with contextlib.redirect_stdout(f):
                        netbox.ipam.vlans.create(add_data)
                line_in_excel = int(numerical_order) + 2
                print("[TẠO VLAN] - dòng {}, add vlan success" .format(line_in_excel))
            except pynetbox.RequestError as e:
                with open('/var/log/logrunning.log', 'w') as f:
                    with contextlib.redirect_stdout(f):
                        print(e.error)
    return

def create_vlan_main():
    data = get_vlans()
    key_data = get_key_data(data)
    try:
        create_vlan(key_data, data)
        print("Tạo vlan thành công")
    except:
        print("Lỗi khi tạo vlan")
    return
# create_vlan_main()
import pynetbox
import contextlib
from slugify import slugify
from get_data_json import get_vlans, get_key_data
from check_data_netbox import check_sites, netbox

def get_data_vlan_group(numerical_order, data):
    site_name=data['site']['{}' .format(numerical_order)]
    site_id = check_sites(site_name)
    group_name = data['vlan_group']['{}' .format(numerical_order)]
    convert_slug = slugify(group_name)
    slug = convert_slug.lower()
    add_data = list()
    add_data.append(
        dict (
            name= group_name,
            slug= slug,
            site= site_id,
        )
    )
    return add_data

def create_vlan_group(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_vlan_group(numerical_order, data)
        try:
            with open('/var/log/logrunning.log', 'w') as f:
                with contextlib.redirect_stdout(f):
                    netbox.ipam.vlan_groups.create(add_data)
            line_in_excel = int(numerical_order) + 2
            print("[TẠO VLAN GROUP] - dòng {} add vlan group success" .format(line_in_excel))
        except pynetbox.RequestError as e:
                with open('/var/log/logrunning.log', 'w') as f:
                    with contextlib.redirect_stdout(f):
                        print(e.error)
        # print(add_data)
    return

def create_vlan_group_main():
    data = get_vlans()
    key_data = get_key_data(data)
    try:
        create_vlan_group(key_data, data)
        print("Tạo vlan group thành công")
    except:
        print("Lỗi khi tạo vlan group")
    return
# create_vlan_group_main()
import pynetbox
from slugify import slugify
import contextlib
from check_data_netbox import check_sites, netbox
from get_data_json import get_racks, get_key_data

def get_data_group(numerical_order, data):
    site_name=data['site']['{}' .format(numerical_order)]
    try:
        site_id = check_sites(site_name)
    except:
        line_in_excel = int(numerical_order) + 2
        print("[TẠO RACK GROUP] - dòng {}: add rack_groups false" .format(line_in_excel))
        print("Site name: {} lỗi" .format(site_name))
    group_name = data['group']['{}' .format(numerical_order)]
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

def create_rack_group(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_group(numerical_order, data)
        try:
            with open('/var/log/logrunning.log', 'w') as f:
                with contextlib.redirect_stdout(f):
                    netbox.dcim.rack_groups.create(add_data)
            line_in_excel = int(numerical_order) + 2
            print("[TẠO RACK GROUP] - dòng {}: add rack_groups success" .format(line_in_excel))
        except pynetbox.RequestError as e:
                with open('/var/log/logrunning.log', 'w') as f:
                    with contextlib.redirect_stdout(f):
                        print(e.error)
        # print(add_data)
    return

def create_rack_group_main():
    data = get_racks()
    key_data = get_key_data(data)
    try:
        create_rack_group(key_data, data)
        print("Tạo rack group thành công")
    except:
        print("Lỗi tạo rack group")
    return
# create_rack_group_main()
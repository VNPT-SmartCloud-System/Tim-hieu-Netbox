import pynetbox
import contextlib
from slugify import slugify
from check_data_netbox import netbox
from get_data_json import get_regions_sites, get_key_data

def get_data_region(numerical_order, data):
    region_name = data['Vùng']['{}' .format(numerical_order)]
    if region_name == None:
        add_data = None
    else:
        convert_slug = slugify(region_name)
        slug = convert_slug.lower()
        add_data = list()
        add_data.append(
            dict (
                name= region_name,
                slug= slug,
                # parent= region_id,
            )
        )
    return add_data

def create_region(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_region(numerical_order, data)
        if add_data == None:
            # line_in_excel = int(numerical_order) + 2
            # print("[TẠO REGION] - dòng {}: add regions false" .format(line_in_excel))
            continue
        else:
            try:
                with open('/var/log/logrunning.log', 'w') as f:
                    with contextlib.redirect_stdout(f):
                        netbox.dcim.regions.create(add_data)
                line_in_excel = int(numerical_order) + 2
                print("[TẠO REGION] - dòng {}: add regions success" .format(line_in_excel))
            except pynetbox.RequestError as e:
                with open('/var/log/logrunning.log', 'w') as f:
                    with contextlib.redirect_stdout(f):
                        print(e.error)
            # print(add_data)
    return

def create_region_main():
    data = get_regions_sites()
    key_data = get_key_data(data)
    try:
        create_region(key_data, data)
        print("Tạo region thành công")
    except:
        print("Lỗi tạo regions")
    return

# create_region_main()

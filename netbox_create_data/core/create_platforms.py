import pynetbox
import contextlib
from slugify import slugify
from check_data_netbox import netbox
from get_data_json import get_platform, get_key_data

def get_platforms(numerical_order, data):
    platform_name = data['Tên']['{}' .format(numerical_order)]
    if platform_name == None:
        add_data = None
    else:
        convert_slug = slugify(platform_name)
        slug = convert_slug.lower()
        add_data = list()
        add_data.append(
            dict (
                name= platform_name,
                slug= slug,
            )
        )
    return add_data

def create_platforms(key_data, data):
    for numerical_order in key_data:
        add_data = get_platforms(numerical_order, data)
        if add_data == None:
            # line_in_excel = int(numerical_order) + 2
            # print("[TẠO PLATFORM] - dòng {}: add platforms false" .format(line_in_excel))
            continue
        else:
            try:
                with open('/var/log/logrunning.log', 'w') as f:
                    with contextlib.redirect_stdout(f):
                        netbox.dcim.platforms.create(add_data)
                line_in_excel = int(numerical_order) + 2
                print("[TẠO PLATFORM] - dòng {}: add platforms success" .format(line_in_excel))
            except pynetbox.RequestError as e:
                with open('/var/log/logrunning.log', 'w') as f:
                    with contextlib.redirect_stdout(f):
                        print(e.error)
            # print(add_data)
    return

def create_platforms_main():
    data = get_platform()
    key_data = get_key_data(data)
    try:
        create_platforms(key_data, data)
        print("Tạo platform thành công")
    except:
        print("Tạo platform lỗi")
    return
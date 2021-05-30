import pynetbox
from slugify import slugify
import contextlib
from check_data_netbox import netbox
from get_data_json import get_device_types, get_key_data

def get_data_manufacs(numerical_order, data):
    manufact_name = data['Nhà sản xuất']['{}' .format(numerical_order)]
    if manufact_name == None:
        add_data = None
    else:
        convert_slug = slugify(manufact_name)
        slug = convert_slug.lower()
        add_data = list()
        add_data.append(
            dict (
                name= manufact_name,
                slug= slug,
            )
        )
    return add_data

def create_manufacs(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_manufacs(numerical_order, data)
        if add_data == None:
            # line_in_excel = int(numerical_order) + 2
            # print("[TẠO MANUFACTURER] - dòng {}: add manufacturers false" .format(line_in_excel))
            continue
        else:
            try:
                with open('/var/log/logrunning.log', 'w') as f:
                    with contextlib.redirect_stdout(f):
                        netbox.dcim.manufacturers.create(add_data)
                line_in_excel = int(numerical_order) + 2
                print("[TẠO MANUFACTURER] - dòng {}: add manufacturers success" .format(line_in_excel))
            except pynetbox.RequestError as e:
                with open('/var/log/logrunning.log', 'w') as f:
                    with contextlib.redirect_stdout(f):
                        print(e.error)
            # print(add_data)
    return

def create_manufacs_main():
    data = get_device_types()
    key_data = get_key_data(data)
    try:
        create_manufacs(key_data, data)
        print("Tạo manufacturer thành công")
    except:
        print("Tạo manufacture lỗi")
    return
# create_manufacs_main()
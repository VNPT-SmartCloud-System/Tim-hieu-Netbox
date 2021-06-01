import pynetbox
from slugify import slugify
from check_data_netbox import netbox
from get_data_json import get_device_roles, get_key_data
import contextlib

def get_data_device_role(numerical_order, data):
    role_name = data['Tên vai trò']['{}' .format(numerical_order)]
    if role_name == None:
        add_data = None
    else:
        convert_slug = slugify(role_name)
        slug = convert_slug.lower()
        add_data = list()
        add_data.append(
            dict (
                name= role_name,
                slug= slug,
                vm_role= data['vm_role']['{}' .format(numerical_order)],
            )
        )
    return add_data

def create_device_role(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_device_role(numerical_order, data)
        if add_data == None:
            # line_in_excel = int(numerical_order) + 2
            # print("[TẠO DEVICE ROLE] - dòng {}: add device_roles false" .format(line_in_excel))
            continue
        else:
            try:
                with open('/var/log/logrunning.log', 'w') as f:
                    with contextlib.redirect_stdout(f):
                        netbox.dcim.device_roles.create(add_data)
                line_in_excel = int(numerical_order) + 2
                print("[TẠO DEVICE ROLE] - dòng {}: add device_roles success" .format(line_in_excel))
            except pynetbox.RequestError as e:
                with open('/var/log/logrunning.log', 'w') as f:
                    with contextlib.redirect_stdout(f):
                        print(e.error)
            # print(add_data)
    return

def create_device_role_main():
    data = get_device_roles()
    key_data = get_key_data(data)
    try:
        create_device_role(key_data, data)
        print("Tạo device role thành công")
    except:
        print("Tạo device role không thành công")
    return
# create_device_role_main()
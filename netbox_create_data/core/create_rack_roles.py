import pynetbox
import contextlib
from slugify import slugify
from check_data_netbox import netbox
from get_data_json import get_racks, get_key_data

def get_data_rack_role(numerical_order, data):
    role_name = data['Vai trò của rack']['{}' .format(numerical_order)]
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
            )
        )
    return add_data

def create_rack_role(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_rack_role(numerical_order, data)
        if add_data == None:
            # line_in_excel = int(numerical_order) + 2
            # print("[TẠO RACK ROLE] - dòng {}: add rack_roles false" .format(line_in_excel))
            continue
        else:
            try:
                with open('/var/log/logrunning.log', 'w') as f:
                    with contextlib.redirect_stdout(f):
                        netbox.dcim.rack_roles.create(add_data)
                line_in_excel = int(numerical_order) + 2
                print("[TẠO RACK ROLE] - dòng {}: add rack_roles success" .format(line_in_excel))
            except pynetbox.RequestError as e:
                with open('/var/log/logrunning.log', 'w') as f:
                    with contextlib.redirect_stdout(f):
                        print(e.error)
            # print(add_data)
    return

def create_rack_role_main():
    data = get_racks()
    key_data = get_key_data(data)
    try:
        create_rack_role(key_data, data)
        print("Tạo rack role thành công")
    except:
        print("Lỗi tạo rack role")
    return
# create_rack_role_main()
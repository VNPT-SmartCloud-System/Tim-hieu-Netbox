import pynetbox
import contextlib
from slugify import slugify
from get_data_json import get_prefixes, get_key_data
from check_data_netbox import netbox

def get_data_role(numerical_order, data):
    role_name = data['role']['{}' .format(numerical_order)]
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

def create_prefix_role(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_role(numerical_order, data)
        try:
            with open('/var/log/logrunning.log', 'w') as f:
                with contextlib.redirect_stdout(f):
                    netbox.ipam.roles.create(add_data)
            line_in_excel = int(numerical_order) + 2
            print("[TẠO PREFIX ROLE] - dòng {}: add roles success" .format(line_in_excel))
        except pynetbox.RequestError as e:
            with open('/var/log/logrunning.log', 'w') as f:
                with contextlib.redirect_stdout(f):
                    print(e.error)
        # print(add_data)
    return

def create_prefix_role_main():
    data = get_prefixes()
    key_data = get_key_data(data)
    try:
        create_prefix_role(key_data, data)
        print("Tạo prefix role thành công")
    except:
        print("Tạo prefix role lỗi")
    return
# create_prefix_role_main()
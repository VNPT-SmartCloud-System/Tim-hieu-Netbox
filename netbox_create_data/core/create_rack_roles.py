import pynetbox
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
            continue
        else:
            try: 
                netbox.dcim.rack_roles.create(add_data)
            except pynetbox.RequestError as e:
                print(e.error)
            # print(add_data)
    return

def create_rack_role_main():
    data = get_racks()
    key_data = get_key_data(data)
    create_rack_role(key_data, data)
    return
# create_rack_role_main()
import pynetbox
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
            netbox.ipam.roles.create(add_data)
        except pynetbox.RequestError as e:
            print(e.error)
        # print(add_data)
    return

def create_prefix_role_main():
    data = get_prefixes()
    key_data = get_key_data(data)
    create_prefix_role(key_data, data)
    return
# create_prefix_role_main()
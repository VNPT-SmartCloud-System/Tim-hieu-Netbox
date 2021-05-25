import pynetbox
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
            continue
        else:
            try: 
                netbox.dcim.platforms.create(add_data)
            except pynetbox.RequestError as e:
                print(e.error)
            # print(add_data)
    return

def create_platforms_main():
    data = get_platform()
    key_data = get_key_data(data)
    create_platforms(key_data, data)
    return
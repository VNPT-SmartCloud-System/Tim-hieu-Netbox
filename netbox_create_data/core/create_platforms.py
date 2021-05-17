import pynetbox
from check_data_netbox import netbox
from get_data_json import get_devices, get_key_data

def get_platforms(numerical_order, data):
    add_data = list()
    add_data.append(
        dict (
            name= data['platform']['{}' .format(numerical_order)],
            slug= data['platform_slug']['{}' .format(numerical_order)],
        )
    )
    return add_data

def create_platforms(key_data, data):
    for numerical_order in key_data:
        add_data = get_platforms(numerical_order, data)
        try: 
            netbox.dcim.platforms.create(add_data)
        except pynetbox.RequestError as e:
            print(e.error)
        # print(add_data)
    return

def create_platforms_main():
    data = get_devices()
    key_data = get_key_data(data)
    create_platforms(key_data, data)
    return
# create_platforms_main()
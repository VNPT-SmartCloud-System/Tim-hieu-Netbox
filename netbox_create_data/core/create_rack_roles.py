import pynetbox
from check_data_netbox import netbox
from get_data_json import get_racks, get_key_data

def get_data_rack_role(numerical_order, data):
    add_data = list()
    add_data.append(
        dict (
            name= data['role']['{}' .format(numerical_order)],
            slug= data['role_slug']['{}' .format(numerical_order)],
        )
    )
    return add_data

def create_rack_role(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_rack_role(numerical_order, data)
        try: 
            netbox.dcim.rack_roles.create(add_data)
        except pynetbox.RequestError as e:
            print(e.error)
    return

def create_rack_role_main():
    data = get_racks()
    key_data = get_key_data(data)
    create_rack_role(key_data, data)
    return
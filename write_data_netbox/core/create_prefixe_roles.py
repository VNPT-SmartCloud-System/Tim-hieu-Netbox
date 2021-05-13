import pynetbox
from convert_csv_to_json import get_json_data_ipam, get_key_data
from check_data_netbox import netbox

def get_data_role(numerical_order, data):
    add_data = list()
    add_data.append(
        dict (
            name= data['role']['{}' .format(numerical_order)],
            slug= data['role_slug']['{}' .format(numerical_order)],
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
    return

def create_prefix_role_main():
    data = get_json_data_ipam()
    key_data = get_key_data(data)
    create_prefix_role(key_data, data)
    return
import pynetbox
from check_data_netbox import netbox
from convert_csv_to_json import get_json_data_dcim, get_key_data

def get_data_rack_role(numerical_order, data):
    add_data = list()
    add_data.append(
        dict (
            name= data['rack_role']['{}' .format(numerical_order)],
            slug= data['rack_role_slug']['{}' .format(numerical_order)],
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
    data = get_json_data_dcim()
    key_data = get_key_data(data)
    create_rack_role(key_data, data)
    return
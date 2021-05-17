import pynetbox
from get_data_json import get_aggregates, get_key_data
from check_data_netbox import netbox

def get_data_rir(numerical_order, data):
    add_data = list()
    add_data.append(
        dict (
            name= data['rir']['{}' .format(numerical_order)],
            slug= data['rir_slug']['{}' .format(numerical_order)],
            is_private= data['is_private']['{}' .format(numerical_order)],
        )
    )
    return add_data

def create_rir(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_rir(numerical_order, data)
        try:
            netbox.ipam.rirs.create(add_data)
        except pynetbox.RequestError as e:
            print(e.error)
        # print(add_data)
    return

def create_rir_main():
    data = get_aggregates()
    key_data = get_key_data(data)
    create_rir(key_data, data)
    return
# create_rir_main()
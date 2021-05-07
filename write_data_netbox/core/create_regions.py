import pynetbox
import check_data_netbox
import create_devices

def get_data_region(numerical_order, data):
    add_data = list()
    add_data.append(
        dict (
            name= data['region']['{}' .format(numerical_order)],
            slug= data['region_slug']['{}' .format(numerical_order)],
        )
    )
    return add_data

def create_region(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_region(numerical_order, data)
        try:
            check_data_netbox.netbox.dcim.regions.create(add_data)
        except pynetbox.RequestError as e:
            print(e.error)
    return

def create_region_main():
    data = create_devices.get_json_data()
    key_data = create_devices.get_key_data(data)
    create_region(key_data, data)
    return
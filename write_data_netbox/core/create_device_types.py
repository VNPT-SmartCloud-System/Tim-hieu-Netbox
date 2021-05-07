import pynetbox
import check_data_netbox
import create_devices

def get_data_device_type(numerical_order, data):
    manufacturer=data['manufacturer']['{}' .format(numerical_order)]
    manufact_id= check_data_netbox.check_manufacs(manufacturer)
    add_data = list()
    add_data.append(
        dict (
            manufacturer= manufact_id,
            model= data['device_type']['{}' .format(numerical_order)],
            slug= data['device_type_slug']['{}' .format(numerical_order)],
            u_height= data['device_type_u_height']['{}' .format(numerical_order)],
        )
    )
    return add_data

def create_device_type(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_device_type(numerical_order, data)
        try:
            check_data_netbox.netbox.dcim.device_types.create(add_data)
        except pynetbox.RequestError as e:
            print(e.error)
    return

def create_device_type_main():
    data = create_devices.get_json_data()
    key_data = create_devices.get_key_data(data)
    create_device_type(key_data, data)
    return
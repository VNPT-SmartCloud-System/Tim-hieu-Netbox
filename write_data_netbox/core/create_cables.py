import pynetbox
from convert_csv_to_json import get_data_cables, get_key_data
from check_data_netbox import check_interface, netbox

def get_data_cable(numerical_order, data):
    device_name_a = data['device_name_a']['{}' .format(numerical_order)]
    inf_name_a = data['name_interface_a']['{}' .format(numerical_order)]
    device_name_b = data['device_name_b']['{}' .format(numerical_order)]
    inf_name_b = data['name_interface_b']['{}' .format(numerical_order)]
    interface_id_a = check_interface(device_name_a, inf_name_a)
    interface_id_b = check_interface(device_name_b, inf_name_b)
    device_a_type = data['device_a_type']['{}' .format(numerical_order)]
    device_b_type = data['device_b_type']['{}' .format(numerical_order)]
    add_data = list()
    add_data.append(
        dict (
            termination_a_type= device_a_type,
            termination_a_id= interface_id_a ,
            termination_b_type= device_b_type,
            termination_b_id= interface_id_b,
            type= data['type']['{}' .format(numerical_order)],
            status= data['status']['{}' .format(numerical_order)],
            label= data['label']['{}' .format(numerical_order)],
            length= data['length']['{}' .format(numerical_order)],
            length_unit= data['length_unit']['{}' .format(numerical_order)],
        )
    )
    return add_data

def create_cables(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_cable(numerical_order, data)
        try:
            netbox.dcim.cables.create(add_data)
        except pynetbox.RequestError as e:
            print(e.error)
    return add_data

def create_cable_main():
    data = get_data_cables()
    key_data = get_key_data(data)
    create_cables(key_data, data)
    return
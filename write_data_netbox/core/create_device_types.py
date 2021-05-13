import pynetbox
from check_data_netbox import check_manufacs, netbox
from convert_csv_to_json import get_json_data_dcim, get_key_data, get_data_templates

def get_data_device_type(numerical_order, data):
    manufacturer=data['manufacturer']['{}' .format(numerical_order)]
    manufact_id= check_manufacs(manufacturer)
    device_type = data['device_type']['{}' .format(numerical_order)]
    add_data = list()
    add_data.append(
        dict (
            manufacturer= manufact_id,
            model= device_type,
            slug= data['device_type_slug']['{}' .format(numerical_order)],
            part_number= data['part_number']['{}' .format(numerical_order)],
            u_height= data['device_type_u_height']['{}' .format(numerical_order)],
        )
    )
    return add_data, device_type

def create_device_type(key_data, data):
    for numerical_order in key_data:
        add_data, device_type = get_data_device_type(numerical_order, data)
        data_tpl = get_data_templates() # Lấy dữ liệu trong template
        key_tpl = get_key_data(data_tpl)
        for key in key_tpl:
            if data_tpl['device_type']['{}' .format(key)] == device_type:   # Nếu device type cũng có trong template -> cho phép tạo device type
                try:
                    netbox.dcim.device_types.create(add_data)
                except pynetbox.RequestError as e:
                    print(e.error)
            else:
                print("Device type {} not available interface template" .format(device_type))
    return

def create_device_type_main():
    data = get_json_data_dcim()
    key_data = get_key_data(data)
    create_device_type(key_data, data)
    return
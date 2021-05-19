import pynetbox
from slugify import slugify
from check_data_netbox import check_manufacs, netbox
from get_data_json import get_device_types, get_key_data, get_inf_tpls

def get_data_device_type(numerical_order, data):
    manufacturer=data['manufacturer']['{}' .format(numerical_order)]
    manufact_id= check_manufacs(manufacturer)
    device_type = data['model']['{}' .format(numerical_order)]
    convert_slug = slugify(device_type)
    slug = convert_slug.lower()
    add_data = list()
    add_data.append(
        dict (
            manufacturer= manufact_id,
            model= device_type,
            slug= slug,
            part_number= data['part_number']['{}' .format(numerical_order)],
            is_full_depth= data['is_full_depth']['{}' .format(numerical_order)],
            u_height= data['u_height']['{}' .format(numerical_order)],
            subdevice_role= data['subdevice_role']['{}' .format(numerical_order)],
        )
    )
    return add_data, device_type

def create_device_type(key_data, data):
    for numerical_order in key_data:
        add_data, device_type = get_data_device_type(numerical_order, data)
        data_tpl = get_inf_tpls() # Lấy dữ liệu trong template
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
    data = get_device_types()
    key_data = get_key_data(data)
    create_device_type(key_data, data)
    return
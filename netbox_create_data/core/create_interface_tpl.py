from check_data_netbox import check_device_types, check_manufacs, netbox
from get_data_json import get_inf_tpls, get_key_data
import pynetbox

def get_inf_template(numerical_order, data):
    manufacturer=data['manufacturer']['{}' .format(numerical_order)]
    manufact_id= check_manufacs(manufacturer)
    device_type=data['device_type']['{}' .format(numerical_order)]
    device_type_id= check_device_types(manufact_id, device_type)
    interface_type= data['interface_type']['{}' .format(numerical_order)]
    count_inf = data['count_interface']['{}' .format(numerical_order)]
    types= data['type']['{}' .format(numerical_order)]
    mgmt_only = data['mgmt_only']['{}' .format(numerical_order)]
    return device_type_id, interface_type, count_inf, types, mgmt_only

def create_inf_template(key_data, data):
    for numerical_order in key_data:
        device_type_id, interface_type, count_inf, types, mgmt_only = get_inf_template(numerical_order, data)
        inf = 0
        while inf < count_inf:
            inf = inf+1
            name = "{} {}" . format(interface_type, inf)
            add_data = list()
            add_data.append(
                dict (
                    device_type= device_type_id,
                    name= name,
                    type= types,
                    mgmt_only= mgmt_only,
                )
            )
            try:
                netbox.dcim.interface_templates.create(add_data)
            except pynetbox.RequestError as e:
                print(e.error)
    return

def create_inf_template_main():
    data = get_inf_tpls()
    key_data = get_key_data(data)
    create_inf_template(key_data, data)
    return
import pynetbox
from get_data_vm import get_vm_info, get_key_data
from check_data_vm import check_vm, netbox

def get_data_service(numerical_order, data):
    vm_name = data['VM name']['{}' .format(numerical_order)]
    vm_id = check_vm(vm_name)
    service_name = data['Service']['{}' .format(numerical_order)]
    ports= data['Port']['{}' .format(numerical_order)]
    if service_name == None:
        add_data = None
    else:
        ports = [int(ports)]
        add_data = list()
        add_data.append(
            dict (
                virtual_machine= vm_id,
                name= service_name,
                ports= ports,
                protocol= data['Protocol']['{}' .format(numerical_order)],
            )
        )
    return add_data

def create_service(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_service(numerical_order, data)
        if add_data == None:
            continue
        else:
            try:
                netbox.ipam.services.create(add_data)
            except pynetbox.RequestError as e:
                print(e.error)
            # print(add_data)
    return

def create_service_main():
    data = get_vm_info()
    key_data = get_key_data(data)
    create_service(key_data, data)
    return
import pynetbox
from check_data_vm import check_vm, netbox
from get_data_vm import get_vm, get_key_data

def get_data_vm_itf(numerical_order, data):
    vm_name = data['VM name']['{}' .format(numerical_order)]
    vm_id = check_vm(vm_name)
    if vm_name == None:
        add_data = None
    else:
        add_data = list()
        add_data.append(
            dict (
                virtual_machine= vm_id,
                name= data['Interface']['{}' .format(numerical_order)],
            )
        )
    return add_data

def create_vm_itf(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_vm_itf(numerical_order, data)
        if add_data == None:
            continue
        else:
            try:
                netbox.virtualization.interfaces.create(add_data)
            except pynetbox.RequestError as e:
                print(e.error)
            # print(add_data)
    return

def create_vm_itf_main():
    data = get_vm()
    key_data = get_key_data(data)
    create_vm_itf(key_data, data)
    return
# create_vm_itf_main()
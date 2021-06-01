import pynetbox
from get_data_vm import get_vm, get_key_data
from check_data_vm import check_interface, check_tenants, netbox

def get_data_ip(numerical_order, data):
    vm_name = data['VM name']['{}' .format(numerical_order)]
    inf_name = data['Interface']['{}' .format(numerical_order)]
    inf_id = check_interface(vm_name, str(inf_name))
    ip = data['IP']['{}' .format(numerical_order)]
    prefix = data['Subnet']['{}' .format(numerical_order)]
    tenant_name = data['Tenant']['{}' .format(numerical_order)]
    tenant_id = check_tenants(tenant_name)
    if ip == 'no':
        add_data = None
    else:
        ip = ip+"/{}" .format(int(prefix))
        add_data = list()
        add_data.append(
            dict (
                address= ip,
                assigned_object_type= 'virtualization.vminterface',
                assigned_object_id= inf_id,
                tenant= tenant_id,
                status= 'active',
            )
        )
    return add_data

def create_ipaddr(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_ip(numerical_order, data)
        if add_data == None:
            continue
        else:
            try:
                netbox.ipam.ip_addresses.create(add_data)
            except pynetbox.RequestError as e:
                print(e.error)
            # print(add_data)
    return

def create_ipaddr_main():
    data = get_vm()
    key_data = get_key_data(data)
    create_ipaddr(key_data, data)
    return
# create_ipaddr_main()
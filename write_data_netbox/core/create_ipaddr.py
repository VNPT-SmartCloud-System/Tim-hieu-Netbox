import pynetbox
from convert_csv_to_json import get_data_ipaddr, get_key_data
from check_data_netbox import check_interface, netbox

def get_data_ip(numerical_order, data):
    device_name = data['device_name']['{}' .format(numerical_order)]
    inf_name = data['interface_name']['{}' .format(numerical_order)]
    inf_id = check_interface(device_name, inf_name)
    ip = data['ip_address']['{}' .format(numerical_order)]
    prefix = data['prefix']['{}' .format(numerical_order)]
    ip_addr = ip+"/{}" .format(prefix)
    add_data = list()
    add_data.append(
        dict (
            address= ip_addr,
            assigned_object_type= data['assigned_object_type']['{}' .format(numerical_order)],
            assigned_object_id= inf_id,
            vrf= data['vrf']['{}' .format(numerical_order)],
            tenant= data['tenant']['{}' .format(numerical_order)],
            status= data['status']['{}' .format(numerical_order)],
            role= data['role']['{}' .format(numerical_order)],
            dns_name= data['dns_name']['{}' .format(numerical_order)],
            description= data['description']['{}' .format(numerical_order)],
        )
    )
    return add_data

def create_ipaddr(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_ip(numerical_order, data)
        # print(add_data)
        try:
            netbox.ipam.ip_addresses.create(add_data)
        except pynetbox.RequestError as e:
            print(e.error)
    return

def create_ipaddr_main():
    data = get_data_ipaddr()
    key_data = get_key_data(data)
    create_ipaddr(key_data, data)
    return
create_ipaddr_main()
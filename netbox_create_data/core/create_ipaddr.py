import pynetbox
import re
from get_data_json import get_cables, get_key_data
from check_data_netbox import check_interface,check_tenants, netbox

def get_data_ip(numerical_order, data):
    device_name = data['Tên thiết bị']['{}' .format(numerical_order)]
    inf_name = data['Interface']['{}' .format(numerical_order)]
    Bonding = data['Bonding']['{}' .format(numerical_order)]
    bond_id = check_interface(device_name, Bonding)
    inf_id = check_interface(device_name, inf_name)
    ip = data['IP address']['{}' .format(numerical_order)]
    prefix = data['Subnet']['{}' .format(numerical_order)]
    tenant_name = data['Người sở hữu']['{}' .format(numerical_order)]
    tenant_id = check_tenants(tenant_name)
    if ip == None:
        ip_addr = "0.0.0.0/24"
    else:
        ip_addr = ip+"/{}" .format(prefix)
    Bond = re.search("Bond*", str(Bonding))
    if Bond:
        add_data = list()
        add_data.append(
            dict (
                address= ip_addr,
                assigned_object_type= 'dcim.interface',
                assigned_object_id= bond_id,
                tenant= tenant_id,
                status= 'active',
                # role= data['role']['{}' .format(numerical_order)],
                # dns_name= data['dns_name']['{}' .format(numerical_order)],
                # description= data['description']['{}' .format(numerical_order)],
            )
        )
    elif inf_name == 'no':
        add_data = None
    else:
        add_data = list()
        add_data.append(
            dict (
                address= ip_addr,
                assigned_object_type= 'dcim.interface',
                assigned_object_id= inf_id,
                tenant= tenant_id,
                status= 'active',
                # role= data['role']['{}' .format(numerical_order)],
                # dns_name= data['dns_name']['{}' .format(numerical_order)],
                # description= data['description']['{}' .format(numerical_order)],
            )
        )
    return add_data

def create_ipaddr(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_ip(numerical_order, data)
        if add_data == None:
            continue
        else:
            # try:
            #     netbox.ipam.ip_addresses.create(add_data)
            # except pynetbox.RequestError as e:
            #     print(e.error)
            print(add_data)
    return

def create_ipaddr_main():
    data = get_cables()
    print(data)
    key_data = get_key_data(data)
    create_ipaddr(key_data, data)
    return
create_ipaddr_main()
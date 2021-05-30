import pynetbox
import re
import contextlib
from get_data_json import get_cables, get_key_data
from check_data_netbox import check_interface,check_tenants, netbox

def get_data_ip(numerical_order, data):
    device_name = data['Tên thiết bị']['{}' .format(numerical_order)]
    inf_name = data['Interface']['{}' .format(numerical_order)]
    Bonding = data['Bonding']['{}' .format(numerical_order)]
    ip = data['IP address']['{}' .format(numerical_order)]
    prefix = data['Subnet']['{}' .format(numerical_order)]
    tenant_name = data['Người sở hữu']['{}' .format(numerical_order)]
    if tenant_name == None:
        tenant_id = None
    else:
        try:
            tenant_id = check_tenants(tenant_name)
        except:
            line_in_excel = int(numerical_order) + 2
            print("[TẠO IP ADDRESS] - dòng {}: add ip_addresses false" .format(line_in_excel))
            print("Lỗi tên người sở hữu: {}" .format(tenant_name))
    if ip == 'no':
        ip_addr = None
    else:
        ip_addr = ip+"/{}" .format(int(prefix))
    bond = re.search("Bond*", str(Bonding))
    if bond:
        try:
            bond_id = check_interface(device_name, Bonding)
        except:
            line_in_excel = int(numerical_order) + 2
            print("[TẠO IP ADDRESS] - dòng {}: add ip_addresses false" .format(line_in_excel))
            print("Tên thiết bị: {} hoặc bonding: {} sai" .format(device_name, Bonding))
        info_ip = netbox.ipam.ip_addresses.get(address='{}' .format(ip_addr), device='{}' .format(device_name))
        if info_ip == None:
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
        else:
            add_data = None
    elif inf_name == 'no':
        add_data = None
    else:
        try:
            inf_id = check_interface(device_name, str(inf_name))
        except:
            line_in_excel = int(numerical_order) + 2
            print("[TẠO IP ADDRESS] - dòng {}: add ip_addresses false" .format(line_in_excel))
            print("Tên thiết bị: {} hoặc Interface: {} sai" .format(device_name, str(inf_name)))
        info_ip = netbox.ipam.ip_addresses.get(address='{}' .format(ip_addr), device='{}' .format(device_name))
        if info_ip == None:
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
        else:
            add_data = None
    return add_data, ip_addr

def create_ipaddr(key_data, data):
    for numerical_order in key_data:
        add_data, ip_addr = get_data_ip(numerical_order, data)
        if add_data == None or ip_addr == None:
            # line_in_excel = int(numerical_order) + 2
            # print("[TẠO IP ADDRESS] - dòng {}: add ip_addresses false" .format(line_in_excel))
            continue
        else:
            try:
                with open('/var/log/logrunning.log', 'w') as f:
                    with contextlib.redirect_stdout(f):
                        netbox.ipam.ip_addresses.create(add_data)
                line_in_excel = int(numerical_order) + 2
                print("[TẠO IP ADDRESS] - dòng {}: add ip_addresses success" .format(line_in_excel))
            except pynetbox.RequestError as e:
                with open('/var/log/logrunning.log', 'w') as f:
                    with contextlib.redirect_stdout(f):
                        print(e.error)
            # print(add_data)
    return

def create_ipaddr_main():
    data = get_cables()
    key_data = get_key_data(data)
    try:
        create_ipaddr(key_data, data)
        print("Tạo ip và gán cho thiết bị thành công")
    except:
        print("Lỗi khi tạo ip và gán cho thiết bị")
    return
# create_ipaddr_main()
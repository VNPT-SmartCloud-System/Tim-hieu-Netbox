from os import rename
import pynetbox
from check_data_vm import check_tenants, check_cluster, check_platforms, netbox
from get_data_vm import get_vm_info, get_key_data

def get_data_vm(numerical_order, data):
    name= data['VM name']['{}' .format(numerical_order)]
    # tenant_name = data['Tenant']['{}' .format(numerical_order)]
    # tenant_id = check_tenants(tenant_name)
    status = data['Status']['{}' .format(numerical_order)]
    cluster_name = data['Cluster name']['{}' .format(numerical_order)]
    cluster_id = check_cluster(cluster_name)
    Platform = data['Platform']['{}' .format(numerical_order)]
    platform_id = check_platforms(Platform)
    ram_gb = data['Ram']['{}' .format(numerical_order)]
    ram_mb = int(ram_gb) * 1024
    if name == None:
        add_data = None
    else:
        add_data = list()
        add_data.append(
            dict (
                name= name,
                status= status,
                cluster= cluster_id,
                # tenant= tenant_id,
                platform= platform_id,
                vcpus = data['Cpu']['{}' .format(numerical_order)],
                memory = ram_mb,
                disk = data['Disk']['{}' .format(numerical_order)],
            )
        )
    return add_data

def create_vm(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_vm(numerical_order, data)
        if add_data == None:
            continue
        else:
            try:
                netbox.virtualization.virtual_machines.create(add_data)
            except pynetbox.RequestError as e:
                print(e.error)
            # print(add_data)
    return

def create_vm_main():
    from add_service_vm import create_service_main
    data = get_vm_info()
    key_data = get_key_data(data)
    create_vm(key_data, data)
    create_service_main()
    return
import pynetbox
from check_data_vm import check_cluster_type, check_sites, check_tenants, netbox
from get_data_vm import get_cluster, get_key_data

def get_data_cluster(numerical_order, data):
    type_name = data['Type']['{}' .format(numerical_order)]
    name= data['Tên']['{}' .format(numerical_order)]
    type_id = check_cluster_type(type_name)
    site_name = data['Site']['{}' .format(numerical_order)]
    site_id = check_sites(site_name)
    tenant_name = data['Tenant']['{}' .format(numerical_order)]
    tenant_id = check_tenants(tenant_name)
    if type_name == None or name == None:
        add_data = None
    else:
        add_data = list()
        add_data.append(
            dict (
                name= name,
                type= type_id,
                site= site_id,
                tenant= tenant_id,
            )
        )
    return add_data

def create_cluster(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_cluster(numerical_order, data)
        if add_data == None:
            continue
        else:
            try:
                netbox.virtualization.clusters.create(add_data)
            except pynetbox.RequestError as e:
                print(e.error)
            # print(add_data)
    return

def create_cluster_main():
    data = get_cluster()
    key_data = get_key_data(data)
    create_cluster(key_data, data)
    return
# create_cluster_main()
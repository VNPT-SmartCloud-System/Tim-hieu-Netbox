import pynetbox
import config

netbox = pynetbox.api(url=config.URL_NB, token=config.TOKEN_NB)

def check_sites(site_name):
    """
    Từ thông tin sites trả về thông tin id của sites
    """
    site_info = netbox.dcim.sites.get(name="{}" .format(site_name))
    site_id = site_info['id']
    return site_id

def check_tenants(tenant_name):
    """
    Từ thông tin tenants trả về thông tin id của tenants
    """
    tenant_info = netbox.tenancy.tenants.get(name="{}" .format(tenant_name))
    tenant_id = tenant_info['id']
    return tenant_id

def check_platforms(name):
    """
    Từ thông tin platforms trả về thông tin id của platforms
    """
    platform_info = netbox.dcim.platforms.get(name="{}" .format(name))
    platform_id = platform_info['id']
    return platform_id

def check_cluster_type(type_name):
    from create_cluster_types import create_cluster_type_main
    type_info = netbox.virtualization.cluster_types.get(name="{}" .format(type_name))
    if type_info == None:
        create_cluster_type_main()
        type_info1 = netbox.virtualization.cluster_types.get(name="{}" .format(type_name))
        type_id = type_info1['id']
    else:
        type_id = type_info['id']
    return type_id

def check_vm(vm_name):
    from create_vm import create_vm_main
    vm_info = netbox.virtualization.virtual_machines.get(name="{}" .format(vm_name))
    if vm_info == None:
        create_vm_main()
        vm_info1 = netbox.virtualization.virtual_machines.get(name="{}" .format(vm_name))
        vm_id = vm_info1['id']
    else:
        vm_id = vm_info['id']
    return vm_id

def check_cluster(cluster_name):
    from create_clusters import create_cluster_main
    cluster_info = netbox.virtualization.clusters.get(name="{}" .format(cluster_name))
    if cluster_info == None:
        create_cluster_main()
        cluster_info1 = netbox.virtualization.clusters.get(name="{}" .format(cluster_name))
        cluster_id = cluster_info1['id']
    else:
        cluster_id = cluster_info['id']
    return cluster_id

def check_interface(vm_name, inf_name):
    """
    Từ thông tin interface trên device trả về thông tin id của interface
    """
    try:
        interface_info = netbox.virtualization.interfaces.get(virtual_machine='{}' .format(vm_name), name='{}' .format(inf_name))
        interface_id = interface_info['id']
        return interface_id
    except Exception as ex:
        print(ex)
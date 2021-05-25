import pynetbox
from slugify import slugify
from check_data_netbox import check_regions, check_tenants, netbox
from get_data_json import get_regions_sites, get_key_data

def get_data_site(numerical_order, data):
    region_name=data['Vùng']['{}' .format(numerical_order)]
    tenant_name = data['Người sở hữu']['{}' .format(numerical_order)]
    site_name = data['Tên DC']['{}' .format(numerical_order)]
    if site_name == None or region_name == None:
        add_data = None
    else:
        region_id= check_regions(region_name)
        if tenant_name == None:
            tenant_id = None
        else:
            tenant_id = check_tenants(tenant_name)
        convert_slug = slugify(site_name)
        slug = convert_slug.lower()
        add_data = list()
        add_data.append(
            dict (
                name= site_name,
                slug= slug,
                status= 'active',
                region= region_id,
                tenant = tenant_id,
                # asn= data['asn']['{}' .format(numerical_order)],
                time_zone= data['time_zone']['{}' .format(numerical_order)],
                physical_address= data['Địa chỉ DC']['{}' .format(numerical_order)],
                contact_phone= data['Số điện thoại']['{}' .format(numerical_order)],
                contact_email= data['Email']['{}' .format(numerical_order)],
            )
        )
    return add_data

def create_sites(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_site(numerical_order, data)
        if add_data == None:
            continue
        else:
            try:
                netbox.dcim.sites.create(add_data)
            except pynetbox.RequestError as e:
                print(e.error)
            # print(add_data)
    return

def create_site_main():
    data = get_regions_sites()
    key_data = get_key_data(data)
    create_sites(key_data, data)
    return
# create_site_main()
import pynetbox
from slugify import slugify
from get_data_json import get_regions_sites, get_key_data
from check_data_netbox import netbox

def get_data_tenant(numerical_order, data):
    teanant_name =data['Người sở hữu']['{}' .format(numerical_order)]
    if teanant_name == None:
        add_data = None
    else:
        convert_slug = slugify(teanant_name)
        slug = convert_slug.lower()
        add_data = list()
        add_data.append(
            dict (
                name= teanant_name,
                slug= slug,
            )
        )
    return add_data

def create_tenants(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_tenant(numerical_order, data)
        if add_data == None:
            continue
        else:
            try:
                netbox.tenancy.tenants.create(add_data)
            except pynetbox.RequestError as e:
                print(e.error)
    return

def create_tenants_main():
    data = get_regions_sites()
    key_data = get_key_data(data)
    create_tenants(key_data, data)
    return
# create_site_main()

import pynetbox
from slugify import slugify
from check_data_netbox import check_regions, netbox
from get_data_json import get_regions_sites, get_key_data

def get_data_site(numerical_order, data):
    region_name=data['region']['{}' .format(numerical_order)]
    region_id= check_regions(region_name)
    site_name = data['name']['{}' .format(numerical_order)]
    convert_slug = slugify(site_name)
    slug = convert_slug.lower()
    add_data = list()
    add_data.append(
        dict (
            name= site_name,
            slug= slug,
            status= data['status']['{}' .format(numerical_order)],
            region= region_id,
            asn= data['asn']['{}' .format(numerical_order)],
            time_zone= data['time_zone']['{}' .format(numerical_order)],
            physical_address= data['physical_address']['{}' .format(numerical_order)],
            contact_phone= data['contact_phone']['{}' .format(numerical_order)],
            contact_email= data['contact_email']['{}' .format(numerical_order)],
        )
    )
    return add_data

def create_sites(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_site(numerical_order, data)
        try:
            netbox.dcim.sites.create(add_data)
        except pynetbox.RequestError as e:
            print(e.error)
    return

def create_site_main():
    data = get_regions_sites()
    key_data = get_key_data(data)
    create_sites(key_data, data)
    return
# create_site_main()
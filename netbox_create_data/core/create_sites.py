import pynetbox
from check_data_netbox import check_regions, netbox
from get_data_json import get_sites, get_key_data

def get_data_site(numerical_order, data):
    region_name=data['region']['{}' .format(numerical_order)]
    print("site: ",region_name)
    region_id= check_regions(region_name)
    add_data = list()
    add_data.append(
        dict (
            name= data['name']['{}' .format(numerical_order)],
            slug= data['slug']['{}' .format(numerical_order)],
            status= data['status']['{}' .format(numerical_order)],
            region= region_id,
            facility= data['facility']['{}' .format(numerical_order)],
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
    data = get_sites()
    key_data = get_key_data(data)
    create_sites(key_data, data)
    return
# create_site_main()
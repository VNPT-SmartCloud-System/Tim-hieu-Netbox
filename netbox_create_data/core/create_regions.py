import pynetbox
from slugify import slugify
from check_data_netbox import netbox
from get_data_json import get_regions_sites, get_key_data

def get_data_region(numerical_order, data):
    region_name = data['Vùng']['{}' .format(numerical_order)]
    if region_name == None:
        add_data = None
    else:
        convert_slug = slugify(region_name)
        slug = convert_slug.lower()
        add_data = list()
        add_data.append(
            dict (
                name= region_name,
                slug= slug,
                # parent= region_id,
            )
        )
    return add_data

def create_region(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_region(numerical_order, data)
        if add_data == None:
            continue
        else:
            try:
                netbox.dcim.regions.create(add_data)
            except pynetbox.RequestError as e:
                print(e.error)
            # print(add_data)
    return

def create_region_main():
    data = get_regions_sites()
    key_data = get_key_data(data)
    create_region(key_data, data)
    return

# create_region_main()

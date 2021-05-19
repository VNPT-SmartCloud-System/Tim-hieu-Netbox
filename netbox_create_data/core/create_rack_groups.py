import pynetbox
from slugify import slugify
from check_data_netbox import check_sites, netbox
from get_data_json import get_racks, get_key_data

def get_data_group(numerical_order, data):
    site_name=data['site']['{}' .format(numerical_order)]
    site_id = check_sites(site_name)
    group_name = data['group']['{}' .format(numerical_order)]
    convert_slug = slugify(group_name)
    slug = convert_slug.lower()
    add_data = list()
    add_data.append(
        dict (
            name= group_name,
            slug= slug,
            site= site_id,
        )
    )
    return add_data

def create_rack_group(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_group(numerical_order, data)
        try: 
            netbox.dcim.rack_groups.create(add_data)
        except pynetbox.RequestError as e:
            print(e.error)
        # print(add_data)
    return

def create_rack_group_main():
    data = get_racks()
    key_data = get_key_data(data)
    create_rack_group(key_data, data)
    return
# create_rack_group_main()
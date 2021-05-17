import pynetbox
from check_data_netbox import check_regions, netbox
from get_data_json import get_regions, get_key_data

def get_data_region(numerical_order, data):
    # region_name=data['parent']['{}' .format(numerical_order)]
    # region_id= check_regions(region_name)
    add_data = list()
    add_data.append(
        dict (
            name= data['region']['{}' .format(numerical_order)],
            slug= data['slug']['{}' .format(numerical_order)],
            # parent= region_id,
        )
    )
    return add_data

def create_region(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_region(numerical_order, data)
        try:
            netbox.dcim.regions.create(add_data)
        except pynetbox.RequestError as e:
            print(e.error)
        # print(add_data)
    return

def create_region_main():
    data = get_regions()
    key_data = get_key_data(data)
    create_region(key_data, data)
    return

# create_region_main()

import pynetbox
import check_data_netbox
import create_devices

def get_data_group(numerical_order, data):
    site_name=data['site']['{}' .format(numerical_order)]
    site_id = check_data_netbox.check_sites(site_name)
    add_data = list()
    add_data.append(
        dict (
            name= data['rack_group']['{}' .format(numerical_order)],
            slug= data['rack_group_slug']['{}' .format(numerical_order)],
            site= site_id,
        )
    )
    return add_data

def create_rack_group(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_group(numerical_order, data)
        try: 
            check_data_netbox.netbox.dcim.rack_groups.create(add_data)
        except pynetbox.RequestError as e:
            print(e.error)
    return

def create_rack_group_main():
    data = create_devices.get_json_data()
    key_data = create_devices.get_key_data(data)
    create_rack_group(key_data, data)
    return

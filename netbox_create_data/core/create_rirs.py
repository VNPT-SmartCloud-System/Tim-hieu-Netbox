import pynetbox
from slugify import slugify
from get_data_json import get_aggregates, get_key_data
from check_data_netbox import netbox

def get_data_rir(numerical_order, data):
    rir_name = data['Cơ quan đăng ký internet khu vực']['{}' .format(numerical_order)]
    if rir_name == None:
        add_data = None
    else:
        convert_slug = slugify(rir_name)
        slug = convert_slug.lower()
        add_data = list()
        add_data.append(
            dict (
                name= rir_name,
                slug= slug,
                is_private= data['Dải địa chỉ này là private']['{}' .format(numerical_order)],
            )
        )
    return add_data

def create_rir(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_rir(numerical_order, data)
        if add_data == None:
            continue
        else:
            try:
                netbox.ipam.rirs.create(add_data)
            except pynetbox.RequestError as e:
                print(e.error)
            # print(add_data)
    return

def create_rir_main():
    data = get_aggregates()
    key_data = get_key_data(data)
    create_rir(key_data, data)
    return
# create_rir_main()
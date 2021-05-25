import pynetbox
from slugify import slugify
from check_data_vm import netbox
from get_data_vm import get_cluster_type, get_key_data

def get_data_cluster_type(numerical_order, data):
    type_name = data['Tên']['{}' .format(numerical_order)]
    if type_name == None:
        add_data = None
    else:
        convert_slug = slugify(type_name)
        slug = convert_slug.lower()
        add_data = list()
        add_data.append(
            dict (
                name= type_name,
                slug= slug,
            )
        )
    return add_data

def create_cluster_type(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_cluster_type(numerical_order, data)
        if add_data == None:
            continue
        else:
            try:
                netbox.virtualization.cluster_types.create(add_data)
            except pynetbox.RequestError as e:
                print(e.error)
            # print(add_data)
    return

def create_cluster_type_main():
    data = get_cluster_type()
    key_data = get_key_data(data)
    create_cluster_type(key_data, data)
    return
# create_cluster_type_main()
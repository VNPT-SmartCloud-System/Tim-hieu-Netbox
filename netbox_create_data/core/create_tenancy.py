import pynetbox
from slugify import slugify
import contextlib
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
            # line_in_excel = int(numerical_order) + 2
            # print("[TẠO TENANT] - dòng {} add tenant false" .format(line_in_excel))
            continue
        else:
            try:
                with open('/var/log/logrunning.log', 'w') as f:
                    with contextlib.redirect_stdout(f):
                        netbox.tenancy.tenants.create(add_data)
                line_in_excel = int(numerical_order) + 2
                print("[TẠO TENANT] - dòng {} add tenants success" .format(line_in_excel))
            except pynetbox.RequestError as e:
                with open('/var/log/logrunning.log', 'w') as f:
                    with contextlib.redirect_stdout(f):
                        print(e.error)
    return

def create_tenants_main():
    data = get_regions_sites()
    key_data = get_key_data(data)
    try:
        create_tenants(key_data, data)
        print("Tạo tenant thành công")
    except:
        print("Lỗi khi tạo tenant")
    return
# create_site_main()

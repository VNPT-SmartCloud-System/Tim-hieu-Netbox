import pynetbox
from slugify import slugify
import contextlib
from check_data_netbox import check_regions, check_tenants, netbox
from get_data_json import get_regions_sites, get_key_data

def get_data_site(numerical_order, data):
    region_name=data['Vùng']['{}' .format(numerical_order)]
    tenant_name = data['Người sở hữu']['{}' .format(numerical_order)]
    site_name = data['Tên DC']['{}' .format(numerical_order)]
    if site_name == None or region_name == None:
        add_data = None
    else:
        try:
            region_id= check_regions(region_name)
        except:
            line_in_excel = int(numerical_order) + 2
            print("[TẠO SITE] - dòng {} add site false" .format(line_in_excel))
            print("Lỗi tên regions: {}" .format(region_name))
        if tenant_name == None:
            tenant_id = None
        else:
            try:
                tenant_id = check_tenants(tenant_name)
            except:
                line_in_excel = int(numerical_order) + 2
                print("[TẠO SITE] - dòng {} add site false" .format(line_in_excel))
                print("Lỗi tên người sở hữu: {}" .format(tenant_name))
        convert_slug = slugify(site_name)
        slug = convert_slug.lower()
        add_data = list()
        add_data.append(
            dict (
                name= site_name,
                slug= slug,
                status= 'active',
                region= region_id,
                tenant = tenant_id,
                # asn= data['asn']['{}' .format(numerical_order)],
                time_zone= data['time_zone']['{}' .format(numerical_order)],
                physical_address= data['Địa chỉ DC']['{}' .format(numerical_order)],
                contact_phone= data['Số điện thoại']['{}' .format(numerical_order)],
                contact_email= data['Email']['{}' .format(numerical_order)],
            )
        )
    return add_data

def create_sites(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_site(numerical_order, data)
        if add_data == None:
            # line_in_excel = int(numerical_order) + 2
            # print("[TẠO SITE] - dòng {} add site false" .format(line_in_excel))
            continue
        else:
            try:
                with open('/var/log/logrunning.log', 'w') as f:
                    with contextlib.redirect_stdout(f):
                        netbox.dcim.sites.create(add_data)
                line_in_excel = int(numerical_order) + 2
                print("[TẠO SITE] - dòng {} add site success" .format(line_in_excel))
            except pynetbox.RequestError as e:
                with open('/var/log/logrunning.log', 'w') as f:
                    with contextlib.redirect_stdout(f):
                        print(e.error)
            # print(add_data)
    return

def create_site_main():
    data = get_regions_sites()
    key_data = get_key_data(data)
    try:
        create_sites(key_data, data)
        print("Tạo site thành công")
    except:
        print("Lỗi khi tạo site")
    return
# create_site_main()
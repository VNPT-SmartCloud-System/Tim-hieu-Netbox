import pynetbox
import contextlib
from check_data_netbox import check_sites, check_rack_group, check_rack_roles, check_tenants, netbox
from get_data_json import get_racks, get_key_data

def get_data_rack(numerical_order, data):
    site_name = data['Tên DC']['{}' .format(numerical_order)]
    rack_role = data['Vai trò của rack']['{}' .format(numerical_order)]
    rack_name = data['Tên rack']['{}' .format(numerical_order)]
    if rack_name == None or site_name == None:
        add_data = None
    else:
        # group_name = data['Nhóm rack']['{}' .format(numerical_order)]
        # rack_group_id = check_rack_group(group_name, site_id)
        try:
            rack_role_id = check_rack_roles(rack_role)
        except:
            line_in_excel = int(numerical_order) + 2
            print("[TẠO RACK] - dòng {}: add racks false" .format(line_in_excel))
            print("rack role: {} lỗi" .format(rack_role))
        try:
            site_id = check_sites(site_name)
        except:
            line_in_excel = int(numerical_order) + 2
            print("[TẠO RACK] - dòng {}: add racks false" .format(line_in_excel))
            print("Tên DC: {} lỗi" .format(site_name))
        tenant_name = data['Người sở hữu']['{}' .format(numerical_order)]
        if tenant_name == None:
            tenant_id = None
        else:
            try:
                tenant_id = check_tenants(tenant_name)
            except:
                line_in_excel = int(numerical_order) + 2
                print("[TẠO RACK] - dòng {}: add racks false" .format(line_in_excel))
                print("tên Người sở hữu: {} lỗi" .format(tenant_name))
        add_data = list()
        add_data.append(
            dict (
                name= rack_name,
                site= site_id,
                # group= rack_group_id,
                tenant = tenant_id,
                status= data['Trạng thái']['{}' .format(numerical_order)],
                role= rack_role_id,
                serial= data['serial']['{}' .format(numerical_order)],
                asset_tag= data['Mã tài sản']['{}' .format(numerical_order)],
                type= data['Kiểu của rack']['{}' .format(numerical_order)],
                width= data['Chiều rộng']['{}' .format(numerical_order)],
                outer_width= data['Chiều rộng bên ngoài']['{}' .format(numerical_order)],
                outer_depth= data['Chiều sâu bên ngoài']['{}' .format(numerical_order)],
                outer_unit= data['Đơn vị']['{}' .format(numerical_order)],
                # comments= data['Ghi chú']['{}' .format(numerical_order)],
                u_height= data['Số U của rack']['{}' .format(numerical_order)],
            )
        )
    return add_data

def create_rack(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_rack(numerical_order, data)
        if add_data == None:
            # line_in_excel = int(numerical_order) + 2
            # print("[TẠO RACK] - dòng {}: add racks false" .format(line_in_excel))
            continue
        else:
            try:
                with open('/var/log/logrunning.log', 'w') as f:
                    with contextlib.redirect_stdout(f):
                        netbox.dcim.racks.create(add_data)
                line_in_excel = int(numerical_order) + 2
                print("[TẠO RACK] - dòng {}: add racks success" .format(line_in_excel))
            except pynetbox.RequestError as e:
                with open('/var/log/logrunning.log', 'w') as f:
                    with contextlib.redirect_stdout(f):
                        print(e.error)
            # print(add_data)
    return

def create_rack_main():
    data = get_racks()
    key_data = get_key_data(data)
    try:
        create_rack(key_data, data)
        print("Tạo rack thành công")
    except:
        print("Tạo rack không thành công")
    return
# create_rack_main()
from datetime import date
import pynetbox
import contextlib
from get_data_json import get_aggregates, get_key_data
from check_data_netbox import check_rir, check_tenants, netbox

today = date.today()
today = today.strftime("%Y-%m-%d")

def get_data_aggregates(numerical_order, data):
    rir_name = data['Cơ quan đăng ký internet khu vực']['{}' .format(numerical_order)]
    if rir_name == None:
        add_data = None
        rir_id = None
    else:
        try:
            rir_id = check_rir(str(rir_name))
        except:
            line_in_excel = int(numerical_order) + 2
            print("[TẠO AGGREGATE] - dòng {}: add aggregates false" .format(line_in_excel))
            print("Lỗi khi tạo aggregate, Cơ quan đăng ký internet khu vực không được để trống")
            rir_id = None
        tenant_name = data['Người sở hữu']['{}' .format(numerical_order)]
        if tenant_name == None:
            tenant_id = None
        else:
            try:
                tenant_id = check_tenants(tenant_name)
            except:
                line_in_excel = int(numerical_order) + 2
                print("[TẠO AGGREGATE] - dòng {}: add aggregates false" .format(line_in_excel))
                print("Lỗi tên người sở hữu: {}" .format(tenant_name))
        add_data = list()
        add_data.append(
            dict (
                prefix= data['Prefix']['{}' .format(numerical_order)],
                tenant = tenant_id,
                rir= rir_id,
                date_added= str(today),
            )
        )
    return add_data, rir_id

def create_aggregates(key_data, data):
    for numerical_order in key_data:
        add_data, rir_id = get_data_aggregates(numerical_order, data)
        if add_data == None or rir_id == None:
            # line_in_excel = int(numerical_order) + 2
            # print("[TẠO AGGREGATE] - dòng {}: add aggregates false" .format(line_in_excel))
            continue
        else:
            try:
                with open('/var/log/logrunning.log', 'w') as f:
                    with contextlib.redirect_stdout(f):
                        netbox.ipam.aggregates.create(add_data)
                line_in_excel = int(numerical_order) + 2
                print("[TẠO AGGREGATE] - dòng {}: add aggregates success" .format(line_in_excel))
            except pynetbox.RequestError as e:
                with open('/var/log/logrunning.log', 'w') as f:
                    with contextlib.redirect_stdout(f):
                        print(e.error)
            # print(add_data)
    return

def create_aggregates_main():
    data = get_aggregates()
    key_data = get_key_data(data)
    try:
        create_aggregates(key_data, data)
        print("Tạo Aggregates thành công")
    except:
        print("Tạo Aggregates bị lỗi")
    return
# create_aggregates_main()
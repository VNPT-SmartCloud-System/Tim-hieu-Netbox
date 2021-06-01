import pynetbox
from get_data_json import get_cables, get_key_data
from check_data_netbox import check_interface, netbox
import contextlib

def get_data_cable(numerical_order, data):
    device_name_a = data['Tên thiết bị']['{}' .format(numerical_order)]
    inf_name_a = data['Interface']['{}' .format(numerical_order)]
    device_name_b = data['Thiết bị kết nối']['{}' .format(numerical_order)]
    inf_name_b = data['Cổng đích']['{}' .format(numerical_order)]
    if device_name_a == None or str(inf_name_a) == 'no':
        add_data = None
    else:
        try:
            interface_id_a = check_interface(device_name_a, str(inf_name_a))
            interface_id_b = check_interface(device_name_b, str(inf_name_b))
        except:
            line_in_excel = int(numerical_order) + 2
            print("[TẠO CABLE] - dòng {}: add cables false" .format(line_in_excel))
            print("Lỗi khi tạo kết nối giữa các thiết bị")
            print("Interface: {} hoặc Cổng đích: {} sai, Tên thiết bị: {} hoặc Thiết bị kết nối: {} sai" .format(inf_name_a, inf_name_b, device_name_a, device_name_b))
        else:
            add_data = list()
            add_data.append(
                dict (
                    termination_a_type= "dcim.interface",
                    termination_a_id= interface_id_a,
                    termination_b_type= "dcim.interface",
                    termination_b_id= interface_id_b,
                    type= data['Loại cáp']['{}' .format(numerical_order)],
                    status= 'connected',
                    length= data['Độ dài cáp']['{}' .format(numerical_order)],
                    length_unit= 'm',
                )
            )
    return add_data

def create_cables(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_cable(numerical_order, data)
        if add_data == None:
            # line_in_excel = int(numerical_order) + 2
            # print("[TẠO CABLE] - dòng {}: add cables false" .format(line_in_excel))
            continue
        else:
            try:
                with open('/var/log/logrunning.log', 'w') as f:
                    with contextlib.redirect_stdout(f):
                        netbox.dcim.cables.create(add_data)
                line_in_excel = int(numerical_order) + 2
                print("[TẠO CABLE] - dòng {}: add cables success" .format(line_in_excel))
            except pynetbox.RequestError as e:
                with open('/var/log/logrunning.log', 'w') as f:
                    with contextlib.redirect_stdout(f):
                        print(e.error)
            # print(add_data)
    return

def create_cable_main():
    data = get_cables()
    key_data = get_key_data(data)
    try:
        create_cables(key_data, data)
        print("Tạo kết nối giữa các thiết bị thành công")
    except:
        print("Lỗi khi tạo kết nối giữa các thiết bị")
    return
# create_cable_main()
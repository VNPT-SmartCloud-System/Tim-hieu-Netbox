# import pynetbox
import re
from get_data_json import get_cables, get_key_data
from check_data_netbox import check_interface, netbox

def get_inf_template(numerical_order, data):
    """
    Lấy dữ liệu trong file cable, nếu device được cấu hình bonding thì trả về bond_id,
        nếu không cấu hình bonding thì bond_id là None
    """
    Bonding = data['Bonding']['{}' .format(numerical_order)]
    device_name_a = data['Tên thiết bị']['{}' .format(numerical_order)]
    inf_name_a = data['Interface']['{}' .format(numerical_order)]
    Bond_switch = data['sw bond']['{}' .format(numerical_order)]
    device_name_b = data['Thiết bị kết nối']['{}' .format(numerical_order)]
    inf_name_b = data['Cổng đích']['{}' .format(numerical_order)]
    bond = re.search("Bond*", str(Bonding))
    sw_bond = re.search("Po*", str(Bond_switch))
    if bond and sw_bond:
        bond_id_a = check_interface(device_name_a, Bonding)
        bond_id_b = check_interface(device_name_b, Bond_switch)
    else:
        bond_id_a = None
        bond_id_b = None
    return bond_id_a, bond_id_b, inf_name_a, device_name_a, inf_name_b, device_name_b

def update_inf_lag_parent(key_data, data):
    """
    Kiểm tra, nếu bond_id là None thì bỏ qua, nếu không None thì tiếp tục xử lý
    """
    for numerical_order in key_data:
        bond_id_a, bond_id_b, inf_name_a, device_name_a, inf_name_b, device_name_b = get_inf_template(numerical_order, data)
        if bond_id_a == None or bond_id_b == None:
            continue
        else:
            # bond_id không None, thực hiện update Bonding là parent của interface
            try:
                interface_info = netbox.dcim.interfaces.get(device='{}' .format(device_name_a), name='{}' .format(inf_name_a))
                interface_info.update({"lag": "{}" .format(bond_id_a)})
                interface_info1 = netbox.dcim.interfaces.get(device='{}' .format(device_name_b), name='{}' .format(inf_name_b))
                interface_info1.update({"lag": "{}" .format(bond_id_b)})
            except Exception as ex:
                print(ex)
    return

def update_lag_main():
    data = get_cables()
    key_data = get_key_data(data)
    update_inf_lag_parent(key_data, data)
    return
# update_lag_main()
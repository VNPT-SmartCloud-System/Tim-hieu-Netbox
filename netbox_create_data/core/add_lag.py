# import pynetbox
import re
from get_data_json import get_cables, get_key_data
from check_data_netbox import check_interface, netbox

def get_inf_template(numerical_order, data):
    Bonding = data['Bonding']['{}' .format(numerical_order)]
    device_name_a = data['Tên thiết bị']['{}' .format(numerical_order)]
    inf_name_a = data['Interface']['{}' .format(numerical_order)]
    bond = re.search("Bond*", str(Bonding))
    if bond:
        bond_id = check_interface(device_name_a, Bonding)
    else:
        bond_id = None
    return bond_id, inf_name_a, device_name_a

def update_inf_lag_parent(key_data, data):
    for numerical_order in key_data:
        bond_id, inf_name_a, device_name_a = get_inf_template(numerical_order, data)
        if bond_id == None:
            continue
        else:
            try:
                interface_info = netbox.dcim.interfaces.get(device='{}' .format(device_name_a), name='{}' .format(inf_name_a))
                interface_info.update({"lag": "{}" .format(bond_id)})
            except Exception as ex:
                print(ex)
    return

def update_lag_main():
    data = get_cables()
    key_data = get_key_data(data)
    update_inf_lag_parent(key_data, data)
    return
# update_lag_main()
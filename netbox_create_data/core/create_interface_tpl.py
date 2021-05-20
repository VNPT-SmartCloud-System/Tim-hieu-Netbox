from check_data_netbox import check_device_types, check_manufacs, netbox
from get_data_json import get_inf_tpls, get_key_data
import pynetbox

def get_inf_template(numerical_order, data):
    manufacturer=data['Nhà sản xuất']['{}' .format(numerical_order)]
    device_type=data['Kiểu thiết bị']['{}' .format(numerical_order)]
    if manufacturer == None or device_type == None:
        device_type_id = None
        interface_type = None
        count_inf = None
        types = None
        mgmt_only = None
    else:
        manufact_id= check_manufacs(manufacturer)
        device_type_id= check_device_types(manufact_id, device_type)
        interface_type= data['Loại interface']['{}' .format(numerical_order)]
        count_inf = data['Số interface']['{}' .format(numerical_order)]
        types= data['Kiểu interface']['{}' .format(numerical_order)]
        mgmt_only = data['manage_only']['{}' .format(numerical_order)]
    return device_type_id, interface_type, count_inf, types, mgmt_only, manufacturer

def create_inf_template(key_data, data):
    for numerical_order in key_data:
        device_type_id, interface_type, count_inf, types, mgmt_only, manufacturer = get_inf_template(numerical_order, data)
        if device_type_id == None:
            continue
        else:
            if type(count_inf) == int:
                inf = 0
                while inf < count_inf:
                    inf = inf+1
                    name = "{} {}" . format(interface_type, inf)
                    add_data = list()
                    add_data.append(
                        dict (
                            device_type= device_type_id,
                            name= name,
                            type= types,
                            mgmt_only= mgmt_only,
                        )
                    )
                    try:
                        netbox.dcim.interface_templates.create(add_data)
                    except pynetbox.RequestError as e:
                        print(e.error)
                    # print(add_data)
            else:
                if len(count_inf) == 5:
                    inf_num1 = count_inf[0:4]
                    inf_num = count_inf[4:]
                elif len(count_inf) == 6:
                    try:
                        inf_num1 = count_inf[0:4]
                        inf_num = int(count_inf[4:])
                    except:
                        inf_num1 = count_inf[0:5]
                        inf_num = int(count_inf[5:])
                elif len(count_inf) == 7:
                    try:
                        inf_num1 = count_inf[0:5]
                        inf_num = int(count_inf[5:])
                    except:
                        inf_num1 = count_inf[0:6]
                        inf_num = int(count_inf[6:])
                elif len(count_inf) == 8:
                    try:
                        inf_num1 = count_inf[0:6]
                        inf_num = int(count_inf[6:])
                    except:
                        inf_num1 = count_inf[0:7]
                        inf_num = int(count_inf[7:])
                elif len(count_inf) == 9:
                    try:
                        inf_num1 = count_inf[0:7]
                        inf_num = int(count_inf[7:])
                    except:
                        inf_num1 = count_inf[0:8]
                        inf_num = count_inf[8:]
                if manufacturer == "Juniper":
                    inf_num = int(inf_num) + 1
                else:
                    inf_num = inf_num
                inf = 0
                while inf < int(inf_num):
                    if manufacturer == "Juniper":
                        name = "{}{}{}" . format(interface_type, inf_num1, inf)
                        inf = inf + 1
                        add_data = list()
                        add_data.append(
                            dict (
                                device_type= device_type_id,
                                name= name,
                                type= types,
                                mgmt_only= mgmt_only,
                            )
                        )
                        try:
                            netbox.dcim.interface_templates.create(add_data)
                        except pynetbox.RequestError as e:
                            print(e.error)
                        # print(add_data)
                    else:
                        inf = inf+ 1
                        name = "{}{}{}" . format(interface_type, inf_num1, inf)
                        add_data = list()
                        add_data.append(
                            dict (
                                device_type= device_type_id,
                                name= name,
                                type= types,
                                mgmt_only= mgmt_only,
                            )
                        )
                        try:
                            netbox.dcim.interface_templates.create(add_data)
                        except pynetbox.RequestError as e:
                            print(e.error)
    return

def create_inf_template_main():
    data = get_inf_tpls()
    key_data = get_key_data(data)
    create_inf_template(key_data, data)
    return
# create_inf_template_main()
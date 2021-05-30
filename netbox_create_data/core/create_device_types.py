import pynetbox
from slugify import slugify
import contextlib
from check_data_netbox import check_manufacs, netbox
from get_data_json import get_device_types, get_key_data, get_inf_tpls

def get_data_device_type(numerical_order, data):
    manufacturer=data['Nhà sản xuất']['{}' .format(numerical_order)]
    device_type = data['Kiểu thiết bị']['{}' .format(numerical_order)]
    if device_type == None:
        add_data = None
        manufact_id = None
    else:
        try:
            manufact_id= check_manufacs(manufacturer)
        except:
            line_in_excel = int(numerical_order) + 2
            print("[TẠO DEVICE TYPE] - dòng {}: add device_types false" .format(line_in_excel))
            print("Lỗi khi tạo device type, Nhà sản xuất không được để trống")
            manufact_id = None
        convert_slug = slugify(device_type)
        slug = convert_slug.lower()
        add_data = list()
        add_data.append(
            dict (
                manufacturer= manufact_id,
                model= device_type,
                slug= slug,
                # part_number= data['part_number']['{}' .format(numerical_order)],
                is_full_depth= data['is_full_depth']['{}' .format(numerical_order)],
                u_height= data['Số u chiếm dụng']['{}' .format(numerical_order)],
                subdevice_role= data['subdevice_role']['{}' .format(numerical_order)],
            )
        )
    return add_data, manufact_id

def create_device_type(key_data, data):
    for numerical_order in key_data:
        add_data, manufact_id = get_data_device_type(numerical_order, data)
        if add_data == None or manufact_id == None:
            # line_in_excel = int(numerical_order) + 2
            # print("[TẠO DEVICE TYPE] - dòng {}: add device_types false" .format(line_in_excel))
            continue
        else:
            try:
                with open('/var/log/logrunning.log', 'w') as f:
                    with contextlib.redirect_stdout(f):
                        netbox.dcim.device_types.create(add_data)
                line_in_excel = int(numerical_order) + 2
                print("[TẠO DEVICE TYPE] - dòng {}: add device_types success" .format(line_in_excel))
            except pynetbox.RequestError as e:
                with open('/var/log/logrunning.log', 'w') as f:
                    with contextlib.redirect_stdout(f):
                        print(e.error)
    return

def create_device_type_main():
    from create_interface_tpl import create_inf_template_main
    from create_platforms import create_platforms_main
    data = get_device_types()
    key_data = get_key_data(data)
    try:
        create_device_type(key_data, data)
        print("Tạo device type thành công")
    except:
        print("Tạo device type không thành công")
    create_inf_template_main()
    create_platforms_main()
    return
import pynetbox
from slugify import slugify
import contextlib
from get_data_json import get_aggregates, get_key_data
from check_data_netbox import netbox

def get_data_rir(numerical_order, data):
    rir_name = data['Cơ quan đăng ký internet khu vực']['{}' .format(numerical_order)]
    if rir_name == None:
        add_data = None
    else:
        convert_slug = slugify(rir_name)
        slug = convert_slug.lower()
        add_data = list()
        add_data.append(
            dict (
                name= rir_name,
                slug= slug,
                is_private= data['Dải địa chỉ này là private']['{}' .format(numerical_order)],
            )
        )
    return add_data

def create_rir(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_rir(numerical_order, data)
        if add_data == None:
            # line_in_excel = int(numerical_order) + 2
            # print("[TẠO RIR] - dòng {}: add rir false" .format(line_in_excel))
            continue
        else:
            try:
                with open('/var/log/logrunning.log', 'w') as f:
                    with contextlib.redirect_stdout(f):
                        netbox.ipam.rirs.create(add_data)
                line_in_excel = int(numerical_order) + 2
                print("[TẠO RIR] - dòng {}: add rir success" .format(line_in_excel))
            except pynetbox.RequestError as e:
                with open('/var/log/logrunning.log', 'w') as f:
                    with contextlib.redirect_stdout(f):
                        print(e.error)
            # print(add_data)
    return

def create_rir_main():
    data = get_aggregates()
    key_data = get_key_data(data)
    try:
        create_rir(key_data, data)
        print("Tạo rir thành công")
    except:
        print("Lỗi tạo rir")
    return
# create_rir_main()
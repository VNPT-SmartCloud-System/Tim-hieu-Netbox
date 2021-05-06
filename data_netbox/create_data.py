import pynetbox
import re
from convert_csv_to_json import convert_data
import config
import check_data_netbox

file_csv = config.PWD_FILE_CSV
file_json = config.PWD_FILE_JSON
netbox = pynetbox.api(url=config.URL_NB, token=config.TOKEN_NB)

try:
    data = convert_data(file_csv, file_json)
except:
    print("No data")

key_data = []
for key, value in data.items():
    for stt in value:
        stt = int(stt)
        if stt not in key_data: 
            key_data.append(stt)
# return key_data

for stt in key_data:
    device_type=data['device_type']['{}' .format(stt)]
    device_role=data['device_role']['{}' .format(stt)]
    site=data['site']['{}' .format(stt)]
    rack=data['rack_name']['{}' .format(stt)]
    manufacturer=data['manufacturer']['{}' .format(stt)]

    manufact_id= check_data_netbox.check_manufacs(manufacturer)
    device_type_id= check_data_netbox.check_device_types(manufact_id, device_type)
    site_id = check_data_netbox.check_sites(site)
    rack_id = check_data_netbox.check_racks(rack)
    role_id = check_data_netbox.check_device_roles(device_role)
    add_data = list()
    add_data.append(
        dict (
            name= data['name']['{}' .format(stt)],
            device_type= device_type_id,
            device_role= role_id,
            serial= data['serial']['{}' .format(stt)],
            site= site_id,
            rack= rack_id,
            position= data['position']['{}' .format(stt)],
            face= 'front',
            comments=data['comments']['{}' .format(stt)],
        )
    )
    try: 
        netbox.dcim.devices.create(add_data)
    except pynetbox.RequestError as e:
        print(e.error)


    
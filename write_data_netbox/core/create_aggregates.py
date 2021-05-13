from datetime import date
import pynetbox
from convert_csv_to_json import get_json_data_ipam, get_key_data
from check_data_netbox import check_rir, netbox

today = date.today()
today = today.strftime("%Y-%m-%d")

def get_data_aggregates(numerical_order, data):
    rir_name = data['rir_name']['{}' .format(numerical_order)]
    rir_id = check_rir(rir_name)
    add_data = list()
    add_data.append(
        dict (
            prefix= data['aggregates_prefix']['{}' .format(numerical_order)],
            rir= rir_id,
            date_added= str(today),
        )
    )
    return add_data

def create_aggregates(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_aggregates(numerical_order, data)
        try: 
            netbox.ipam.aggregates.create(add_data)
        except pynetbox.RequestError as e:
            print(e.error)
    return

def create_aggregates_main():
    data = get_json_data_ipam()
    key_data = get_key_data(data)
    create_aggregates(key_data, data)
    return
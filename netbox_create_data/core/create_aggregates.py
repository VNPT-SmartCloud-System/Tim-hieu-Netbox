from datetime import date
import pynetbox
from get_data_json import get_aggregates, get_key_data
from check_data_netbox import check_rir, netbox

today = date.today()
today = today.strftime("%Y-%m-%d")

def get_data_aggregates(numerical_order, data):
    rir_name = data['rir']['{}' .format(numerical_order)]
    rir_id = check_rir(rir_name)
    add_data = list()
    add_data.append(
        dict (
            prefix= data['prefix']['{}' .format(numerical_order)],
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
        # print(add_data)
    return

def create_aggregates_main():
    data = get_aggregates()
    key_data = get_key_data(data)
    create_aggregates(key_data, data)
    return
# create_aggregates_main()
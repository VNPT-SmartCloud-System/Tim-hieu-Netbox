import config
import json

vm_json = config.VM_JSON
vm_info_json = config.VM_INFO_JSON
cluster_type_json = config.CLUSTER_TYPE
cluster_json = config.CLUSTER

def get_cluster_type():
    from convert_data_vm import convert_cluster_type
    convert_cluster_type()
    with open('{}' .format(cluster_type_json)) as json_file:
        cluster_type_data = json.load(json_file)
    return cluster_type_data

def get_cluster():
    from convert_data_vm import convert_cluster
    convert_cluster()
    with open('{}' .format(cluster_json)) as json_file:
        cluster_data = json.load(json_file)
    return cluster_data

def get_vm_info():
    from convert_data_vm import convert_vm_info
    convert_vm_info()
    with open('{}' .format(vm_info_json)) as json_file:
        vm_info_data = json.load(json_file)
    return vm_info_data

def get_vm():
    from convert_data_vm import convert_vm
    convert_vm()
    with open('{}' .format(vm_json)) as json_file:
        vm_data = json.load(json_file)
    return vm_data

def get_key_data(data):
    key_data = []
    for key, value in data.items():
        for stt in value:
            stt = int(stt)
            if stt not in key_data: 
                key_data.append(stt)
    return key_data
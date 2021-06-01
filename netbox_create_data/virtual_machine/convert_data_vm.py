'''Module này chứa các funtion để convert thông tin các sheet trong file excel thành json
sau đó lưu vào các file json đã tạo trước đó.
'''
import pandas as ps
import config

# Lấy file excel và các file json từ config
netbox_excel_data = config.NETBOX_INFO_EXCEL
vm_json = config.VM_JSON
vm_info_json = config.VM_INFO_JSON
cluster_type_json = config.CLUSTER_TYPE
cluster_json = config.CLUSTER

# Lấy thông tin tên sheet
vm = config.vm
vm_info = config.vm_info
cluster_type = config.cluster_type
clusters = config.clusters

def convert_cluster_type():
    try:
        excel_data_df = ps.read_excel('{}' .format(netbox_excel_data),
                                      sheet_name='{}' .format(cluster_type),
                                      engine='openpyxl')
        excel_data_df.to_json('{}' .format(cluster_type_json))
    except Exception as ex:
        print(ex)
    return

def convert_cluster():
    try:
        excel_data_df = ps.read_excel('{}' .format(netbox_excel_data),
                                      sheet_name='{}' .format(clusters),
                                      engine='openpyxl')
        excel_data_df.to_json('{}' .format(cluster_json))
    except Exception as ex:
        print(ex)
    return

def convert_vm():
    try:
        excel_data_df = ps.read_excel('{}' .format(netbox_excel_data),
                                      sheet_name='{}' .format(vm),
                                      engine='openpyxl')
        excel_data_df = excel_data_df.fillna(method='ffill', axis=0)
        excel_data_df.to_json('{}' .format(vm_json))
    except Exception as ex:
        print(ex)
    return

def convert_vm_info():
    try:
        excel_data_df = ps.read_excel('{}' .format(netbox_excel_data),
                                      sheet_name='{}' .format(vm_info),
                                      engine='openpyxl')
        excel_data_df.to_json('{}' .format(vm_info_json))
    except Exception as ex:
        print(ex)
    return
# convert_vm()
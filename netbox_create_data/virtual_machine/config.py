"""
Cấu hình truy cập netbox
"""
# Đường dẫn truy cập netbox
URL_NB ="http://10.10.35.191:8000"
# Token của tài khoản admin netbox
TOKEN_NB ="e9694713f6472ad070ddc17d980530f44ea1b670"

"""
Cấu hình đường dẫn excel và các file json
"""
# Đường dẫn file excel
NETBOX_INFO_EXCEL = '../file_data/netbox_info.xlsx'
# VM 
VM_JSON = '../file_data/vm.json'
# Thong tin chi tiet của vm
VM_INFO_JSON = '../file_data/vm_info.json'
# Thong tin cluster
CLUSTER_TYPE = '../file_data/cluster_type.json'
CLUSTER = '../file_data/cluster.json'

"""
Cấu hình tên sheet trong excel
"""

# Sheet chứa thông tin vm
vm = "VM"
# Sheet chứa thông tin chi tiêt hơn của vm như ram,disk,cpu,...
vm_info = "Thong tin chi tiet VM"
# Sheet chứa thông tin tên cluster type
cluster_type = "Cluster_type"
# Sheet chứa thông tin cluster
clusters = "Clusters"

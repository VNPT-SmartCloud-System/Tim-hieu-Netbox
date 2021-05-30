"""
Cấu hình đường dẫn excel và các file json
"""
# Đường dẫn file excel
NETBOX_INFO_EXCEL = './uploads/netbox_info.xlsx'
# Đường dẫn file json chứa thông tin region và site
REGION_SITE_JSON = '../file_data/regions_sites.json'
# Đường dẫn file json chứa thông tin racks
RACK_JSON = '../file_data/racks.json'
# Đường dẫn file json chứa thông tin device type 
DEVICE_TYPES_JSON = '../file_data/device_types.json'
# Đường dẫn file json chứa thông tin device role
DEIVE_ROLE_JSON = '../file_data/device_roles.json'
# Đường dẫn file json chứa thông tin devices
DEVICES_JSON = '../file_data/devices.json'
# Đường dẫn file json chứa thông tin vlans
VLANS_JSON = '../file_data/vlans.json'
# Đường dẫn file json chứa thông tin aggregates
AGGREGATES_JSON = '../file_data/aggregates.json'
# Đường dẫn file json chứa thông tin interface template
INTERFACE_TPL = '../file_data/interface_templates.json'
# Đường dẫn file json chứa thông tin về cable
CABLE_CONNECT = '../file_data/cable_connections.json'
# hệ điều hành 
PLATFORM = '../file_data/platforms.json'

"""
Cấu hình tên sheet trong excel
"""
# Sheet chứa thông tin region và site
regions_sites = "Region va Site"
# Sheet chứa thông tin racks
racks = "racks"
# Sheet chứa thông tin device type
device_types = "Kieu thiet bi"
# Sheet chứa thông tin các template của interface
inf_template = "interface_templates"
# Sheet chứa thông tin deivce role
device_roles = "Vai tro thiet bi"
# Sheet chứa thông tin device
devices = "Thiet bi"
# Sheet chứa thông tin aggregates
aggregates= "Aggregates"
# Sheet chứa thông tin vlan 
vlans = "vlans"
# Sheet chứa thông tin các kết nối, địa chỉ ip
cable_ip = "Thong tin IP"
# Sheet chứa thông tin về hệ điều hành
platform = "Platform"

"""
Cấu hình truy cập netbox
"""
# Đường dẫn truy cập netbox
URL_NB =
# Token của tài khoản admin netbox
TOKEN_NB =
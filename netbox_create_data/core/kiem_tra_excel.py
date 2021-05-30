from get_data_json import get_regions_sites,get_racks, get_devices, get_cables, get_device_types, get_key_data
import config

# Lấy thông tin về tên sheet
regions_sites = config.regions_sites
racks = config.racks
device_types = config.device_types
devices = config.devices
cable_ip = config.cable_ip

def check_site_duplicate():
    print("\n+======== KIỂM TRA SITE BỊ TRÙNG ========+\n")
    data_site = get_regions_sites()
    key_data = get_key_data(data_site)
    list_site = []
    list_site_duplicate = []
    for key in key_data:
        site_name = data_site['Tên DC']['{}' .format(key)]
        if site_name == None:
            continue
        elif site_name not in list_site:
            list_site.append(site_name)
        elif site_name in list_site:
            list_site_duplicate.append(site_name)
    if not list_site_duplicate:
        print("Không có Site nào trùng trong sheet")
    else:
        print("Các Site bị trùng là: ", list_site_duplicate)
        print("Kiểm tra sheet: ", regions_sites)
    return

def check_rack_duplicate():
    print("\n+======== KIỂM TRA RACK BỊ TRÙNG ========+\n")
    data_rack = get_racks()
    key_data = get_key_data(data_rack)
    list_rack = []
    list_rack_duplicate = []
    for key in key_data:
        rack_name = data_rack['Tên rack']['{}' .format(key)]
        if rack_name == None:
            continue
        elif rack_name not in list_rack:
            list_rack.append(rack_name)
        elif rack_name in list_rack:
            list_rack_duplicate.append(rack_name)
    if not list_rack_duplicate:
        print("Không có Rack nào trùng trong sheet")
    else:
        print("Các Rack bị trùng là: ", list_rack_duplicate)
        print("Kiểm tra sheet: ", racks)
    return

def check_device_duplicate():
    print("\n+======= KIỂM TRA DEVICE BỊ TRÙNG =======+\n")
    data_device = get_devices()
    key_data = get_key_data(data_device)
    list_device = []
    list_device_duplicate = []
    for key in key_data:
        deivce_name = data_device['Tên thiết bị']['{}' .format(key)]
        if deivce_name == None:
            continue
        elif deivce_name not in list_device:
            list_device.append(deivce_name)
        elif deivce_name in list_device:
            list_device_duplicate.append(deivce_name)
    if not list_device_duplicate:
        print("Không có Device nào trùng trong sheet")
    else:
        print("Các Device bị trùng là: ", list_device_duplicate)
        print("Kiểm tra sheet: ", devices)
    return

def check_dvtype_duplicate():
    print("\n+==== KIỂM TRA DEVICE TYPE BỊ TRÙNG =====+\n")
    data_dvtype = get_device_types()
    key_data = get_key_data(data_dvtype)
    list_dvtype = []
    list_dvtype_duplicate = []
    for key in key_data:
        dvtype_name = data_dvtype['Kiểu thiết bị']['{}' .format(key)]
        if dvtype_name == None:
            continue
        elif dvtype_name not in list_dvtype:
            list_dvtype.append(dvtype_name)
        elif dvtype_name in list_dvtype:
            list_dvtype_duplicate.append(dvtype_name)
    if not list_dvtype_duplicate:
        print("Không có Device Type nào trùng trong sheet")
    else:
        print("Các Device Type bị trùng là: ", list_dvtype_duplicate)
        print("Kiểm tra sheet: ", device_types)
    return

def check_ip_duplicate():
    print("\n+===== KIỂM TRA IP ADDRESS BỊ TRÙNG =====+\n")
    data_ip = get_cables()
    key_data = get_key_data(data_ip)
    list_ip = []
    list_ip_duplicate = []
    for key in key_data:
        ip_addr = data_ip['IP address']['{}' .format(key)]
        if ip_addr == None:
            continue
        elif ip_addr == 'no':
            continue
        elif ip_addr not in list_ip:
            list_ip.append(ip_addr)
        elif ip_addr in list_ip:
            list_ip_duplicate.append(ip_addr)
    if not list_ip_duplicate:
        print("Không có IP nào trùng trong sheet")
    else:
        print("Các IP bị trùng là: ", list_ip_duplicate)
        print("Kiểm tra sheet: ", cable_ip)
    return

def main():
    check_site_duplicate()
    check_rack_duplicate()
    check_device_duplicate()
    check_dvtype_duplicate()
    check_ip_duplicate()
    return
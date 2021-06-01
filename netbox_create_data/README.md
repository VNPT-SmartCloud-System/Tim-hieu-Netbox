# Cập nhật thông tin lên NetBox

# Chuẩn bị môi trường

```sh
yum install git -y
yum groupinstall "Development Tools" -y
yum install https://centos7.iuscommunity.org/ius-release.rpm -y
yum update -y
yum install python-devel -y
yum install python36-devel -y
yum install python36 -y
yum install python-pip -y
yum install python36u-pip -y
pip3.6 install virtualenv==16.7.9
```

# Clone source code

```
git clone https://github.com/hungviet99/Tim-hieu-Netbox.git
```

# Di chuyển source code

```
mv <path>/netbox_create_data /opt
```

# Tạo env

```sh
cd /opt/netbox_create_data/core
virtualenv env -p python3.6
source env/bin/activate
```

# Install requirement

```sh
pip install -r requirements.txt
```

# Edit file config

- Sửa đường dẫn tới trang netbox
```
sed -i 's/URL_NB =/URL_NB = "http:\/\/<netbox_domain_or_ip>"/' /opt/netbox_create_data/core/config.py
```

- Thêm token netbox
```
sed -i 's/TOKEN_NB =/TOKEN_NB = "933f6df395h3b23bdd103k582nf93l450d64b4d260"/' /opt/netbox_create_data/core/config.py
```

# Tạo systemd

```
vi /etc/systemd/system/update-netbox.service
```

Truyền vào file nội dung như sau:

```
[Unit]
Description=Update Netbox
After=network.target

[Service]
PermissionsStartOnly=True
User=root
Group=root
WorkingDirectory=/opt/netbox_create_data/core
ExecStart=/opt/netbox_create_data/core/env/bin/python /opt/netbox_create_data/core/application.py --serve-in-foreground

[Install]
WantedBy=multi-user.target
```

# Khởi động dịch vụ

```
systemctl daemon-reload
systemctl start update-netbox.service
systemctl enable update-netbox.service --now
systemctl status update-netbox.service
```

# Truy cập web

Sử dụng trình duyệt truy cập vào url `http://<ip_or_domain>:5001/` và tiến hành update dữ liệu cho netbox

![](../images/webupload.png)
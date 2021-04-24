# deploy netbox-docker with swarm

Repo này chứa các thành phần cần thiết để xây dựng 1 cụm cluster cho Netbox chạy trên docker container. 

## Quickstart

Để bắt đầu thiết lập, trước tiên cần có 1 cụm docker swarm từ 2 node trở lên. Sau đó hãy tiến hành làm theo các bước sau: 

- Trên mỗi node hãy thực hiện như sau: 

```
cd /opt
git clone https://github.com/hungviet99/Tim-hieu-Netbox.git
```

- Sau đó đứng ở node master và triển khai netbox: 

```
cd /opt/Tim-hieu-Netbox/netbox-docker
```
```
echo "ALLOWED_HOSTS=<DOMAIN_NAME_NETBOX> <IP_NODE_1>" >> /opt/Tim-hieu-Netbox/netbox-docker/netbox1.env
echo "ALLOWED_HOSTS=<DOMAIN_NAME_NETBOX> <IP_NODE_2>" >> /opt/Tim-hieu-Netbox/netbox-docker/netbox2.env
echo "ALLOWED_HOSTS=<DOMAIN_NAME_NETBOX> <IP_NODE_3>" >> /opt/Tim-hieu-Netbox/netbox-docker/netbox3.env
```
> Thay <DOMAIN_NAME_NETBOX> <IP_NODE_1,2,3> bằng tên domain dùng cho netbox và IP tương ứng của từng node. 

```
tee docker-compose.override.yml <<EOF
version: '3.4'
services:
  netbox:
    ports:
      - 8000:8080
  netbox1:
    ports:
      - 8001:8080
  netbox2:
    ports:
      - 8002:8080
EOF
docker stack deploy -c docker-compose.yml -c docker-compose.override.yml netbox
```

**Lưu ý:** Ta có các file để cấu hình domain trong thư mục `/opt/Tim-hieu-Netbox/netbox-docker/nginx-cert`. Nên cần phải sửa địa chỉ IP của từng host và tên domain sẽ sử dụng cho netbox tại đây. 

Ta có 3 file domain là `domain1`, `domain2`, `domain3`. Ta lần lượt sửa tên domain sẽ sử dụng cho netbox như sau: 

**Node1**

```
sed -i 's/    server_name netbox.com;/    server_name <DOMAIN_NAME_NETBOX>;/g' /opt/Tim-hieu-Netbox/netbox-docker/nginx-cert/domain1.conf
```
```
sed -i 's/        proxy_pass http://10.10.35.191:8000;/        proxy_pass http://<IP_NODE_1>:8000;/g' /opt/Tim-hieu-Netbox/netbox-docker/nginx-cert/domain1.conf
```

**Node2**

```
sed -i 's/    server_name netbox.com;/    server_name <DOMAIN_NAME_NETBOX>;/g' /opt/Tim-hieu-Netbox/netbox-docker/nginx-cert/domain2.conf
```
```
sed -i 's/        proxy_pass http://10.10.35.192:8001;/        proxy_pass http://<IP_NODE_2>:8001;/g' /opt/Tim-hieu-Netbox/netbox-docker/nginx-cert/domain2.conf
```

**Node3**

```
sed -i 's/    server_name netbox.com;/    server_name <DOMAIN_NAME_NETBOX>;/g' /opt/Tim-hieu-Netbox/netbox-docker/nginx-cert/domain3.conf
```
```
sed -i 's/        proxy_pass http://10.10.10.193:8002;/        proxy_pass http://<IP_NODE_3>:8002;/g' /opt/Tim-hieu-Netbox/netbox-docker/nginx-cert/domain3.conf
```

- Sau khi sửa cấu hình domain, tiếp theo tiến hành copy file config domain. 

**Node1**

```
cp /opt/Tim-hieu-Netbox/netbox-docker/nginx-cert/domain1.conf /var/lib/docker/volumes/netbox_etc-nginx/_data/conf.d/<DOMAIN_NAME>.conf
```

**Node2**

```
cp /opt/Tim-hieu-Netbox/netbox-docker/nginx-cert/domain2.conf /var/lib/docker/volumes/netbox_etc-nginx/_data/conf.d/<DOMAIN_NAME>.conf
```

**Node3**

```
cp /opt/Tim-hieu-Netbox/netbox-docker/nginx-cert/domain3.conf /var/lib/docker/volumes/netbox_etc-nginx/_data/conf.d/<DOMAIN_NAME>.conf
```

- Thực hiện chuyển thư mục ssl phòng khi cần sử dụng ssl. 

```
mv /opt/Tim-hieu-Netbox/netbox-docker/nginx-cert/ssl /var/lib/docker/volumes/netbox_etc-nginx/_data/
```

- Khởi động lại service

```
docker service update netbox_nginx-revserse1
docker service update netbox_nginx-revserse2
docker service update netbox_nginx-revserse3
```

Sau 1 vài phút toàn bộ ứng dụng được triển khai sẽ khả dụng. Mở trình duyệt và truy cập vào url `http://<DOMAIN_NAME_NETBOX>:8000/` để vào trang chủ netbox. Có thể đăng nhập ở góc bên phải với thông tin đăng nhập mặc định là: 

* Username: **admin**
* Password: **admin**
* API Token: **0123456789abcdef0123456789abcdef01234567**

## Dependencies

`Docker` và `docker-compose` phải đáp ứng các yêu cầu sau:

* Phiên bản thấp nhất của `Docker` là `19.03`.
* Phiên bản thấp nhất của `docker-compose` là `1.28.0`.

Để kiểm tra phiên bản đã cài đặt hãy làm như sau: `docker --version` và `docker-compose --version`.

## About

Reference from [Netbox Docker](https://github.com/netbox-community/netbox-docker)
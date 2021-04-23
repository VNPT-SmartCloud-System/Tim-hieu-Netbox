# deploy netbox-docker with swarm

Repo này chứa các thành phần cần thiết để xây dựng 1 cụm cluster cho Netbox chạy trên docker container. 

## Quickstart

Để bắt đầu thiết lập, trước tiên cần có 1 cụm docker swarm gồm 3 node trở lên. Sau đó hãy tiến hành làm theo các bước sau: 

Trên mỗi node hãy thực hiện như sau: 

```
cd /opt
git clone https://github.com/hungviet99/Tim-hieu-Netbox.git
```

Sau đó đứng ở node master và triển khai netbox: 

```
cd /opt/Tim-hieu-Netbox/netbox-docker
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
docker-compose pull
docker stack deploy -c docker-compose.yml -c docker-compose.override.yml netbox
```

Sau 1 vài phút toàn bộ ứng dụng được triển khai sẽ khả dụng. Mở trình duyệt và truy cập vào url `http://0.0.0.0:8000/` để vào trang chủ netbox. Có thể đăng nhập ở góc bên phải với thông tin đăng nhập mặc định là: 

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
# Install python 3.6 and dependencies

```sh
yum groupinstall "Development Tools" -y
yum install https://centos7.iuscommunity.org/ius-release.rpm -y
yum install python-devel -y
yum install python36-devel -y
yum install python36 -y
yum install python-pip -y
yum install python36u-pip -y
pip3.6 install virtualenv==16.7.9
```

# Move source into /opt

```sh
mv <path>/netbox_alert_modified /opt
```

# Create venv

```sh
cd /opt/netbox_alert_modified
virtualenv env -p python3.6
source env/bin/activate
```

# Install requirement

```sh
pip install -r requirements.txt
```

# Open file config

```sh
vi /opt/netbox_alert_modified/config.py
```

# Edit parameter

```sh
SLACK_TOKEN
SLACK_CHANNEL
TELEGRAM_TOKEN
TELEGRAM_CHAT_ID
```

# Create Systemd

```sh
vi /etc/systemd/system/webhook-netbox.service
```

# With

```sh
[Unit]
Description=Webhook Netbox
After=network.target

[Service]
PermissionsStartOnly=True
User=root
Group=root
ExecStart=/opt/netbox_alert_modified/env/bin/python /opt/netbox_alert_modified/webhook.py --serve-in-foreground

[Install]
WantedBy=multi-user.target
```

# Start

```sh
systemctl daemon-reload
systemctl start webhook-netbox
systemctl status webhook-netbox
```

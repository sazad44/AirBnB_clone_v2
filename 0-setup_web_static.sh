#!/usr/bin/env bash
# Shell script to set up server for deployment
apt-get -y install nginx
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
echo "TEST TEST TEST" | tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
cat > default <<EOF
server {
    listen 80 default_server;
    index index.html index.htm index;

    location / {
        alias /data/web_static;
}
    location /hbnb_static {
        alias /data/web_static/current;
   }
}
EOF
mv default /etc/nginx/sites-available/default
sudo service nginx restart

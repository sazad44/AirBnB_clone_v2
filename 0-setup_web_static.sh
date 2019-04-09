#!/usr/bin/env bash
sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test
sudo touch /data/web_static/releases/test/index.html
sudo mkdir -p /data/web_static/shared
echo "some content" | sudo tee -a /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/current /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "33i \
        location /hbnb_static {\n\
                alias data/web_static/current/hbnb_static;\n\
                index index.html;\n\
        }" /etc/nginx/sites-available/default;
sudo service nginx restart

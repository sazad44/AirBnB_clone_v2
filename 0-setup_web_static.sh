#!/usr/bin/env bash
#Set Up NGINX server to return a page that contains string

apt-get -y install nginx
mkdir -p /data/www
echo "Holberton School for the win!" > index.html
echo "Ceci n'est pas une page it's a 404!" > 404.html
cp index.html /data/www/
cp 404.html /data/www/
cat > default <<EOF
server {
    listen 80 default_server;
    root /data/www;
    error_page 404 /404.html;
    location / {
        index index.html index.html;
    }
    location /hbnb_static {
        alias /data/web_static/current;
    }
    location = /404.html {
        internal;
    }
    location /redirect_me {
       return 301 https://google.com;
    }
}
EOF
cp default /etc/nginx/sites-available/default
sudo service nginx restart

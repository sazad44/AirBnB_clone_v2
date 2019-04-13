$doc_root="/data/www"

exec { 'apt-get update':
  command => '/usr/bin/apt-get update'
}

package { 'nginx':
  ensure => 'installed',
  required => Exec['apt-get update']
}

file { $doc_root:
  ensure => 'directory'
}

file { '$doc_root/index.html':
  ensure => 'present',
  content => 'Holberton School for the win!',
  require => File[$doc_root]
}

file { '$doc_root/404.html':
  ensure => 'present',
  content => 'Ceci n\'est pas une page it\'s a 404!'
  require => File[$doc_root]
}

file { '/etc/nginx/sites-available/default':
  ensure => 'present',
  content => 'server {
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
}'
    require => File[/etc/nginx/sites-available]
}

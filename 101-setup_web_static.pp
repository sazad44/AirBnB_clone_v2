exec { 'apt-get update':
  command => '/usr/bin/apt-get update'
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['apt-get update']
}

file { ['/data', '/data/www', '/data/web_static', '/data/web_static/releases', '/data/web_static/shared', '/data/web_static/releases/test']:
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu'
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => 'Holberton School for the win!',
  require => File['/data/web_static/releases/test']
}

file { '/data/www/404.html':
  ensure  => 'present',
  content => 'Ceci n\'est pas une page it\'s a 404!',
  require => File[ '/data/www' ]
}

$cont="server {
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
}"

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $cont
}

file { '/data/web_static/current':
    ensure => 'link',
    target => '/data/web_static/releases/test/'
}

exec { 'restart nginx':
    path    => [ '/bin/', '/usr/bin/', '/sbin/', '/usr/sbin/' ],
    command => 'service nginx restart'
}

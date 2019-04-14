# Configures server for nginx and serving content at resource path hbnb_static

exec { 'apt-get update':
  command => '/usr/bin/apt-get update'
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['apt-get update']
}

file { [ '/data', '/data/web_static' ]:
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu'
}

file { ['/data/web_static/releases', '/data/web_static/shared', '/data/web_static/releases/test']:
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['/data/web_static']
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => 'Holberton School for the win!\r\n',
  require => File['/data/web_static/releases/test'],
  owner => 'ubuntu',
  group => 'ubuntu'
}

file { '/data/web_static/404.html':
  ensure  => 'present',
  content => 'Ceci n\'est pas une page it\'s a 404!',
  require => File[ '/data/web_static' ]
}

$cont="server {
    listen 80 default_server;
    root /data/web_static;
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
  target => '/data/web_static/releases/test/',
  owner  => 'ubuntu',
  group  => 'ubuntu'
}

exec { 'restart nginx':
  path    => [ '/bin/', '/usr/bin/', '/sbin/', '/usr/sbin/' ],
  command => 'service nginx restart'
}

exec { 'rm':
  command => 'rm -rf /data/www /data/web_static/current/test',
  path => '/bin/'
}

# install and configure an Nginx server using Puppet instead of Bash.
exec { 'server configuration':
	command  => 'apt-get -y update; apt-get -y install nginx; echo "Hello World!" > /var/www/html/index.nginx-debian.html; sed -i "/listen 80 default_server;/a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;/" /etc/nginx/sites-available/default; service nginx start',
	provider => shell,
}

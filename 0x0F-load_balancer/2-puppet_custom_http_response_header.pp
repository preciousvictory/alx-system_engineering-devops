#utomate the task of creating a custom HTTP header response
exec { 'server configuration':
	command  => 'sudo apt-get -y update; sudo apt-get -y install nginx; ufw allow 'Nginx HTTP'; echo 'Hello World!' > /var/www/html/index.nginx-debian.html; sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default; sudo service nginx start',
	provider => shell,
}

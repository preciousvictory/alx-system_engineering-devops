# change the word phpp to php
exec { 'change of word':
	command => 'sed -i 's/phpp/php/g' /var/www/html/wp-settings.php',
	provider => shell,
	path    => '/bin';
}

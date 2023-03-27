#using Puppet to make changes to our configuration file
file {'~/.ssh/config':
	ensure => present,
	path   => '/etc/ssh/ssh_config'
}

exec { 'change ~/.ssh/config':
	command  => 'eciho "PasswordAuthentication no\nIdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
	provider => 'shell',
	path     => '/bin/'
}

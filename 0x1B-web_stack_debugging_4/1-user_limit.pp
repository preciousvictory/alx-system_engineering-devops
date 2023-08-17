# login with the holberton user and open a file without any error message
exec { 'Change soft limit':
  command => 'sudo sed -i "/holberton soft/s/4/10000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
  provider => shell,
}

exec { 'Change hard limit':
  command => 'sudo sed -i "/holberton hard/s/5/100000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
  provider => shell,
}

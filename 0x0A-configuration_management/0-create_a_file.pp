# Using Puppet, create a file in /tmp
file {'/tmp/school':
  path    => '/tmp/school',
  content => 'I love Puppet',
  group   => 'www-data',
  owner   => 'www-data',
  mode    => '0744',
}

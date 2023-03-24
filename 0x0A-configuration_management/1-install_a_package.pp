#Using Puppet, install flask from pip33
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}

# Puppet file to set up client SSH configuration file to connect to a server without typing pw.
file_line { 'replace passwordAuthentication':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  replace => true,
  line    => 'PasswordAuthentication no',
  match   => 'PasswordAuthentication yes', 
} 

file_line { 'add the private key ~/.ssh/holberton':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton',
}

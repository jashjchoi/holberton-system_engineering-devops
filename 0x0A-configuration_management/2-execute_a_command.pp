# Using Puppet, create a manifest that kills a process killmenow
exec { 'pkill killmenow':
  command => '/usr/bin/pkill -f /killmenow'
}

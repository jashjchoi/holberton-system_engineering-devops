# Using Puppet, create a manifest that kills a process killmenow
exec { 'killmenow':
  command => 'pkill killmenow',
  provider => shell,
}

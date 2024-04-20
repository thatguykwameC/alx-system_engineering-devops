# This manifest kills the process 'killmenow'

exec {'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin',
}

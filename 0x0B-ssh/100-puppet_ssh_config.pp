# This manifest sets up your SSH, so it connects to a server without a password.

include stdlib
file_line {'change private key':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school'
}
file_line {'no password':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}

# this manifest fixes a misconfiguration that caused server
# error 500 when running strace on a WordPress site

exec { 'fixed-phpp':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin';
}

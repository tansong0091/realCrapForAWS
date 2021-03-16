#!/bin/sh

#/usr/local/apache2/bin/httpd -f /usr/local/apache2/conf/httpd.conf -k start
#when using apachectl it take environment varianles in /usr/local/apache2/bin/envvars but when using httpd start directly it will not use env in envvars
HOST=`hostname`
echo "export HOSTNAME=$HOST" >>/usr/local/apache2/bin/envvars
/usr/local/apache2/bin/apachectl start



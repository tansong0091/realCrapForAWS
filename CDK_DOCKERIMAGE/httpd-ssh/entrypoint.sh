#!/bin/sh

#/usr/local/apache2/bin/httpd -f /usr/local/apache2/conf/httpd.conf -k start
#when using apachectl it take environment varianles in /usr/local/apache2/bin/envvars but when using httpd start directly it will not use env in envvars
HOST=`hostname`
echo "export HOSTNAME=$HOST" >>/usr/local/apache2/bin/envvars
/usr/local/apache2/bin/apachectl start

#tail -f /dev/null

#if [ -z "$SSH_PUBLIC_KEY" ]; then
#  echo "Need your SSH public key as the SSH_PUBLIC_KEY env variable."
#  exit 1
#fi

# Create a folder to store user's SSH keys if it does not exist.
USER_SSH_KEYS_FOLDER=~/.ssh
[ ! -d "$USER_SSH_KEYS_FOLDER" ] && mkdir -p $USER_SSH_KEYS_FOLDER && chmod 700  $USER_SSH_KEYS_FOLDER && echo $SSH_PUBLIC_KEY > ${USER_SSH_KEYS_FOLDER}/authorized_keys

# Copy contents from the `SSH_PUBLIC_KEY` environment variable
# to the `${USER_SSH_KEYS_FOLDER}/authorized_keys` file.
# The environment variable must be set when the container starts.

# Clear the `SSH_PUBLIC_KEY` environment variable.
unset SSH_PUBLIC_KEY

# Start the SSH daemon.
/usr/sbin/sshd -D


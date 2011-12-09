#!/bin/bash
#This script replaces the root password with the one (whole shadow line) in the /etc/cluster/conf/roothash
#If this is not available, it sets an empty root password for the node
umask 0777
if [ -f /mnt/conf/roothash ] ; then
 cat /mnt/conf/roothash >/tmp/newshadow
else
 echo "root:!:15033:0:99999:7:::" > /tmp/newshadow
fi
umask 0022

tail -n +2 /etc/shadow >> /tmp/newshadow

cp /tmp/newshadow /etc/shadow
rm -f /tmp/newshadow

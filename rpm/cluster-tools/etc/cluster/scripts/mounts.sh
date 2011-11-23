#!/bin/bash
. /mnt/conf/cluster.conf
#echo "10.2.1.5:/home /home nfs4 defaults 0 0 " >> /etc/fstab

#ln -s /home/export /export

# Fix idmapd configuration
sed -i /etc/idmapd.conf -e "s/#Domain\ =\ local.domain.edu/Domain\ =\ $CLUSTERNAME/"

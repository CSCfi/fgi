#!/bin/bash
source /mnt/conf/cluster.conf
cp /mnt/conf/ntp.conf-clusternode /etc/ntp.conf
if [ "x$CLUSTERNAME" != "x" ] ; then
 sed -i /etc/ntp.conf -e "s/name\ =\ \"unspecified\"/name\ =\ \"$CLUSTERNAME\"/" -e "s/LOGINNODEIP/$LOGINNODEIP/" -e "s/INSTALLNODEIP/$INSTALLNODEIP/"
fi


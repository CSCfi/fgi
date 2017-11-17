#!/bin/bash
source /mnt/conf/cluster.conf
cp /mnt/conf/gmond.conf-clusternode /etc/ganglia/gmond.conf
if [ "x$CLUSTERNAME" != "x" ] ; then
 sed -i /etc/ganglia/gmond.conf -e "s/name\ =\ \"unspecified\"/name\ =\ \"$CLUSTERNAME\"/" -e "s/LOGINNODEIP/$LOGINNODEIP/" -e "s/INSTALLNODEIP/$INSTALLNODEIP/"
fi

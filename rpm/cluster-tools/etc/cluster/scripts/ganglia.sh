#!/bin/bash
source /mnt/conf/cluster.conf
if [ "x$CLUSTERNAME" != "x" ] ; then
 sed -i /etc/ganglia/gmond.conf -e "s/name\ =\ \"unspecified\"/name\ =\ \"$CLUSTERNAME\"/"
fi


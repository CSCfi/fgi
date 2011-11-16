#!/bin/bash

NODE_CONF_FILE=/etc/cluster/conf/cluster.conf

if [ ! -f $NODE_CONF_FILE  ] ; then
 echo "Cluster configuration not found under $NODE_CONF_FILE. Exiting" >&2
 exit 1
fi
. "$NODE_CONF_FILE"

if [ "x$CLUSTERNAME" == "x" ] ; then
 echo "\$CLUSTERNAME does not seem to be set in cluster.conf. Exiting" >&2
 exit 1
fi
nodestart=`echo $CLUSTERNAME | cut -b1-2`

if [ "x$SUBNET" == "x" ] ; then
 echo "\$SUBNET does not seem to be set in cluster.conf. Exiting" >&2
 exit 1
fi
ipstart=`echo $SUBNET | cut -f 1-2 -d "."`

if [ ! -e "macs" ] ; then
 echo "Error, file 'macs' which contains the names and macs of nodes was not found" >&2
 exit 1
fi

while read node ; do 
 nodenum=`echo $node |cut -f 1 -d " " | cut -b 3-10`
 nodemac=`echo $node |cut -f 2 -d " "`
 mkdir -p /tmp/cluster/conf/nodes/$nodestart$nodenum
 $ipstart.100.$nodenum > /tmp/cluster/nodes/$nodestart$nodenum/eth0-ip
 echo $nodemac > /tmp/cluster/nodes/$nodestart$nodenum/eth0-mac
done < macs

echo "Node configs created under /tmp/cluster/nodes"
echo "Please check that they seem ok, and copy them to"
echo "/etc/cluster/nodes/"

#!/bin/bash
source /mnt/conf/cluster.conf
MYIPEND=`cat /mnt/nodes/$hostname/eth0-ip` |grep -o "[0-9]*\,[0-9*]$"
IBSUBNETSTART=`echo $IB_SUBNET |grep -o "^[0-9]*\.[0-9]*"`

cat  > /etc/sysconfig/network-scripts/ifcfg-ib0 <<EOF
DEVICE="ib0"
NM_CONTROLLED="yes"
BOOTPROTO="static"
BROADCAST="$IBSUBNETSTART.255.255"
IPADDR="$IBSUBNETSTART.$MYIPEND"
NETMASK="255.255.0.0"
ONBOOT="yes"
EOF


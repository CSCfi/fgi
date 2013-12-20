#!/bin/bash
source /mnt/conf/cluster.conf

if [ "$USE_IB" == "yes" ]; then 

MYIPEND=`cat /mnt/nodes/$HOSTNAME/eth0-ip |grep -o "[0-9]*\.[0-9]*$"`
IBSUBNETSTART=`echo $IB_SUBNET |grep -o "^[0-9]*\.[0-9]*"`

cat  > /etc/sysconfig/network-scripts/ifcfg-ib0 <<EOF
DEVICE="ib0"
NM_CONTROLLED="yes"
BOOTPROTO="static"
BROADCAST="$IBSUBNETSTART.255.255"
IPADDR="$IBSUBNETSTART.$MYIPEND"
NETMASK="255.255.0.0"
PREFIX=16
ONBOOT="yes"
EOF

fi

cp /mnt/conf/90-rdma.rules /etc/udev/rules.d/


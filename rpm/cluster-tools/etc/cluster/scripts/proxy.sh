#!/bin/bash
source /mnt/conf/cluster.conf

echo "proxy=http://$LOGINNODEIP:3128/" >> /etc/yum.conf

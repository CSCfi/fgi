#!/bin/bash
source /mnt/conf/cluster.conf

echo "proxy=http://$LOGINNODEIP:3128/" >> /etc/yum.conf
sed -i -e "s/PROXY=DIRECT/PROXY=http:\/\/$LOGINNODEIP:3128/" /etc/cvmfs/default.local
echo "http_proxy = http://$LOGINNODEIP:3128/" >> /etc/fetch-crl.conf

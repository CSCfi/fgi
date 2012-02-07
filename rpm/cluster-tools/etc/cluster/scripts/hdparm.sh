#!/bin/bash
#Turn on write cache for those who have two sata drives

md1=`cat /proc/mdstat 2>/dev/null |grep md1`

echo $md1 | grep raid0  &>/dev/null
if [ $? -ne 0 ] ; then
 exit
fi

echo $md1 | grep sda  &>/dev/null
if [ $? -ne 0 ] ; then
 exit
fi

echo $md1 | grep sdb  &>/dev/null
if [ $? -ne 0 ] ; then
 exit
fi

echo "hdparm -W 1 /dev/sda" >> /etc/rc.local
echo "hdparm -W 1 /dev/sdb" >> /etc/rc.local

#!/bin/bash
NVIDIACHECK=`lspci -d 10de:`
if [ ! -z "$NVIDIACHECK" ]; then
 ln -s `awk '{ if ($2 == "/") print $1; }' /etc/fstab` /dev/root
 yum -y install kmod-nvidia
 echo "chmod 0666 /dev/nvidia*" >> /etc/rc.d/rc.local
fi


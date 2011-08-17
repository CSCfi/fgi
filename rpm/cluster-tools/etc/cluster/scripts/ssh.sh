#!/bin/bash
cp /mnt/nodes/$HOSTNAME/ssh/* /etc/ssh/

mkdir -p /root/.ssh
chmod 700 /root/.ssh
cp /mnt/conf/authorized_keys /root/.ssh/

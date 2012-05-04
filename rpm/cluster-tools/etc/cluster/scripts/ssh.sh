#!/bin/bash
cp /mnt/nodes/$HOSTNAME/ssh/* /etc/ssh/
chmod 600 /etc/ssh/ssh_host_{r,d}sa_key

mkdir -p /root/.ssh
chmod 700 /root/.ssh
cp /mnt/conf/authorized_keys /root/.ssh/

#!/bin/bash
sed -i "s/enabled=1/enabled=0/" /etc/yum.repos.d/sl.repo
sed -i "s/enabled=1/enabled=0/" /etc/yum.repos.d/sl-updates.repo
cp /mnt/repos/*.repo /etc/yum.repos.d


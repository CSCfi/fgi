#!/bin/bash
cp /mnt/conf/munge.key /etc/munge/
chown munge:munge /etc/munge/munge.key

cp /mnt/conf/slurm.conf /etc/slurm/

# Copy optional topology.conf file
if [ -f /mnt/conf/topology.conf ] ; then
 cp /mnt/conf/topology.conf /etc/slurm/
fi
if [ -f /mnt/conf/cgroup.conf ] ; then
 cp /mnt/conf/cgroup.conf /etc/slurm/
fi

if [ -f /mnt/conf/gres.conf ]; then
 cp /mnt/conf/gres.conf /etc/slurm/
fi
if [ -f /mnt/nodes/$HOSTNAME/gres.conf ]; then
 cp /mnt/nodes/$HOSTNAME/gres.conf /etc/slurm
fi

chkconfig slurm on
chkconfig munge on

cat << EOF > /etc/pam.d/slurm
auth     required  pam_localuser.so
account  required  pam_unix.so
session  required  pam_limits.so
EOF



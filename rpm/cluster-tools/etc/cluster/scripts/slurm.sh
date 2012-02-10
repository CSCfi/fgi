#!/bin/bash
cp /mnt/conf/munge.key /etc/munge/
chown munge:munge /etc/munge/munge.key

cp /mnt/conf/slurm.conf /etc/slurm/

chkconfig slurm on

cat << EOF > /etc/pam.d/slurm
auth     required  pam_localuser.so
account  required  pam_unix.so
session  required  pam_limits.so
EOF



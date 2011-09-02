#!/bin/bash
cp /mnt/conf/munge.key /etc/munge/
chown munge:munge /etc/munge/munge.key

cp /mnt/conf/slurm.conf /etc/slurm/

chkconfig slurm on

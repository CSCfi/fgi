#!/bin/bash
source /mnt/conf/cluster.conf

if [ -f /mnt/conf/cvmfs_default.local ]; then
	cp /mnt/conf/cvmfs_default.local /etc/cvmfs/default.local
fi


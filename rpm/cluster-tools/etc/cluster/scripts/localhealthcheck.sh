#!/bin/bash
if [ -d /mnt/conf/healthcheck ]; then
	mkdir /etc/slurm/healthcheck
	cp /mnt/conf/healthcheck/* /etc/slurm/healthcheck
fi


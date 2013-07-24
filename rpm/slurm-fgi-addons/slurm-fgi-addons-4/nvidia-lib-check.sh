#!/bin/bash

HOSTNAME=`hostname -s`

# Check if the nvidia library has been updated, if so drain+reboot

if [ -c /dev/nvidiactl ]; then 
	if [ -x /usr/bin/nvidia-smi ]; then 
		/usr/bin/nvidia-smi > /dev/null
		if [ $? -eq 255 ]; then
			scontrol update nodename=$HOSTNAME state=drain reason=reboot
		fi
	fi
fi  

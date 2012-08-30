#!/bin/bash
FOO=`grep 6\.3 /etc/redhat-release`
if [ "$?" -eq 0 ]; then 
	mv /etc/request-key.d/id_resolver.conf /etc/request-key.d/id_resolver.conf-fgi
fi


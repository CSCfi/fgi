#!/bin/bash
sed -i /etc/sysconfig/cpuspeed -e 's/^GOVERNOR.*/GOVERNOR="performance"/'

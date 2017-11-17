#!/bin/bash

if [ ! -e "$HOME/burnin/linpack" ] ; then
 echo "Can't find the directory \"$HOME/burnin/linpack\". Please follow the instructions for running the burn in tests" >&2
 exit
fi

id |grep root &>/dev/null

if [ $? -eq 0 ] ; then
 echo "You shouldn't be running this as root, since you probably don't have /root shared to nodes, which means linpack isn't there" >&2 
 exit
fi

for f in `cat /etc/machines` ; do
 sbatch -w $f linpack.sh
done

#!/bin/bash
MYDIR=`dirname $0`
for file in $MYDIR/install/scripts/* ; do 
 $file 
done

#!/bin/bash

for f in `cat /etc/machines` ; do
 if [ "x$FIRST" == "x" ] ; then
  FIRST=$f
 else
  sbatch -w "$FIRST","$f" iperf.sh "$FIRST"
  FIRST=
 fi
done


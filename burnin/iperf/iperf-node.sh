#!/bin/bash

hn=`hostname`
if [ x"$1" != "x" ] ; then
 if [ $1 == $hn ] ; then
  iperf -s
 else
  iperf -i 30 -t 86400 -c $1-ib
 fi
fi

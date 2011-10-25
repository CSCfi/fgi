#/bin/bash

CURRDIR=`dirname $0`

if [ -e "$CURRDIR"/$HOSTNAME-error ] ; then
 rm "$CURRDIR"/$HOSTNAME-error
fi

if [ -e "$CURRDIR"/$HOSTNAME-success ] ; then
 rm "$CURRDIR"/$HOSTNAME-success
fi

grep ENTER "$CURRDIR"/hponcfg.dat &>/dev/null

if [ $? -eq 0 ] ; then
 echo "It seems that you still have not configured hponcfg.dat" |tee "$CURRDIR"/$HOSTNAME-error
 exit
fi


#get the current ip address, minus the subnet part
addrend=`ifconfig ib0 |grep "inet addr" |cut -f2 -d ":" |cut -f1 -d " "  | cut -f 3-4 -d "."`

if [ x"$addrend" == "x" ] ; then
 echo "For some reason I could not get the IB address (which is used as a base for the iLO address" |tee "$CURRDIR"/$HOSTNAME-error
 echo "Is ib0 up and working?" |tee -a "$CURRDIR"/$HOSTNAME-error
 exit
fi

mkdir /tmp/fwconf

cp -r "$CURRDIR"/conrep* /tmp/fwconf
cp -r "$CURRDIR"/hponcfg.dat /tmp/fwconf

cd /tmp/fwconf

sed -i /tmp/fwconf/hponcfg.dat -e "s/__IP_END__/$addrend/"

hponcfg -r
if [ $? -ne 0 ] ; then
 rm -rf /tmp/fwconf
 echo "Could not reset iLO config" |tee "$CURRDIR"/$HOSTNAME-error
 exit 
fi 

hponcfg -f hponcfg.dat
if [ $? -ne 0 ] ; then
 rm -rf /tmp/fwconf
 echo "Could not configure iLO" |tee "$CURRDIR"/$HOSTNAME-error
 exit 
fi 

./conrep -l -f conrep.dat
if [ $? -ne 0 ] ; then
 rm -rf /tmp/fwconf
 echo "Could not configure BIOS" |tee "$CURRDIR"/$HOSTNAME-error
 exit 
fi 

cd /tmp
rm -rf /tmp/fwconf

echo "Succesfully configured BIOS and iLO, rebooting" |tee "$CURRDIR"/$HOSTNAME-success

reboot

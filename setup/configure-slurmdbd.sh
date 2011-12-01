#!/bin/bash

. /etc/slurm/slurmdbd.conf
. /etc/cluster/conf/cluster.conf

if [ x"$StoragePass" == "x" ] ; then
 echo "StoragePass seems to be empty, please enter a pasword for the slurm DB" >&2
 exit 1
fi

if [ "$StoragePass" == "ENTERPASSWORD" ] ; then
 echo "Please set the slurm DB password in /etc/slurm/slurmdbd.conf before running this script " >&2
 exit 1
fi

if [ "$DbdAddr" == "clustername-install" ] || [ "$DbdHost" == "clustername-install" ] ; then
 echo "Please set the clustername for DbdAddr and DbdHost in /etc/slurm/slurmdbd.conf before running this script" >&2
 exit 1
fi

if [ "$ControlMachine" == "clustername-install" ] ; then
 echo "Please set the ControlMachine variable in /etc/slurm/slurm.conf before running this script" >&2
 exit 1
fi

if [ "$AccountingStorageHost" == "clustername-install" ] ; then
 echo "Please set the AccountingStorageHost  variable in /etc/slurm/slurm.conf before running this script" >&2
 exit 1
fi

if [ "$ClusterName" == "clustername" ] ; then
 echo "Please set the ClusterName variable in /etc/slurm/slurm.conf before running this script" >&2
 exit 1
fi

echo "create database slurm" | mysql -uroot 

if [ $? -ne 0 ] ; then
 echo "Oh no! It seems that the MySQL database could not be created. Please contact tech support at your nearest CSC. Or look into this script file and try to seen what happened." >&2
 exit 1
fi

echo 'grant all privileges on slurm_acct_db.* to "slurm"@"localhost" identified by ' \'"$StoragePass"\' | mysql -uroot
echo 'grant all privileges on slurm_acct_db.* to "slurm"@"'$CLUSTERNAME-install.local'" identified by ' \'"$StoragePass"\' | mysql -uroot

if [ $? -ne 0 ] ; then
 echo "Whoops! The darnest thig happened. The slurm user could not be added to MySQL. The (most likely) friendly (if they had their morning coffee) tech support at CSC could probably help you. If you are a clever one, look into this file and see you you can find the problem." >&2
 exit 1
fi

echo "Starting slurmdbd"
service slurmdbd start

if [ $? -ne 0 ] ; then
 echo "Hello Mr./Ms. Admin. The slurmdbd refused to start for some reason, probably a misconfiguration. /var/log/slurm/slurmdbd.log might tell you why." >&2
 echo "I assume this is an easy thing to fix, and by the time you read this you might have fixed this. You can't rerun the file though, since it will fail, so you need to taka a peek into it and see if you couldn't just run the required things manually." >&2
 exit 1
fi

chkconfig slurmdbd on

sacctmgr -i add cluster "$ClusterName"
if [ $? -ne 0 ] ; then
 echo "Even though I tried my best, the sacctmgr command refused to cooperate. Contact CSC and see if they would have the right sledgehammer to convince sacctmgr to work." >&2
fi

echo "DONE!"

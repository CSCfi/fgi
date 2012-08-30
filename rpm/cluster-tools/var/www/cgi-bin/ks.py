#!/usr/bin/python
import sys
import os
import socket
sys.stderr = sys.stdout
print "Content-Type: text/plain"
print

extra_packages = ""
slurm_packages = "slurm\nslurm-munge"
fgi_packages = ""
installnode = "10.1.1.1"
clustername = "fgi"
installurl = ""
elrepourl = ""
securityurl = ""
fgiurl = ""
epelurl = ""
localurl = ""
cvmfsurl = ""
diskconfig = ""
egitrustanchorsrepourl = ""


try:
 clusterconf = open("/etc/cluster/conf/cluster.conf")
 clustersettings = {}
 for line in clusterconf.readlines():
  #for every line, e.g. "key=value", set clusterconf["key"]="value"
  #comment lines will throw an error, skip them
  try:
   clustersettings[line.split("=")[0]] = line.split("=")[1].strip()
  except:
   pass
 
 installnode = clustersettings["INSTALLNODEIP"]
 clustername = clustersettings["CLUSTERNAME"]
 proxy = clustersettings["LOGINNODEIP"]
 installurl = "url --url %s --proxy=http://%s:3128/" % (clustersettings["OS_REPOURL"], proxy)
 securityurl = 'repo --name="Scientific Linux 6 - Security updates" --baseurl=%s --proxy=http://%s:3128/' % (clustersettings["OS_SECURITY_REPOURL"], proxy)
 fgiurl = 'repo --name="FGI" --baseurl=%s --proxy=http://%s:3128/' % (clustersettings["FGI_REPOURL"], proxy)
 epelurl = 'repo --name="epel" --baseurl=%s --proxy=http://%s:3128/' % (clustersettings["EPEL_REPOURL"], proxy)
 elrepourl = 'repo --name="elrepo" --baseurl=http://elrepo.org/linux/elrepo/el6/x86_64/ --proxy=http://%s:3128/' % (proxy)
 egitrustanchorsrepourl = 'repo --name="egi-trustanchors" --baseurl=http://repository.egi.eu/sw/production/cas/1/current/ --proxy=http://%s:3128/' % (proxy)
 if "LOCAL_REPOURL" in clustersettings and len(clustersettings["LOCAL_REPOURL"]) > 0 :
  localurl = 'repo --name="local" --baseurl=%s --proxy=http://%s:3128/' % (clustersettings["LOCAL_REPOURL"], proxy)
 cvmfsurl = 'repo --name=CVMFS_CERN --proxy=http://%s:3128/ --baseurl=http://cvmrepo.web.cern.ch/cvmrepo/yum/cvmfs/x86_64/' % (proxy)
# from the name, e.g. c1-3.local take c1-3, also support hostnames like c1-3-eth.local. if the hostname ends in -eth or -ib, remove those
 hostname = socket.gethostbyaddr(os.environ["REMOTE_ADDR"])[0].split(".")[0]
 if hostname.endswith("-eth") or hostname.endswith("-ib"):
  hostname = hostname.rsplit("-", 1)[0]
 try:
  f = open("/etc/cluster/nodes/" + hostname + "/packages")
  extra_packages = f.read()
  f.close()
 except:
  pass
 try:
  f = open("/etc/cluster/conf/fgi-default-packages")
  fgi_packages = f.read()
  f.close()
 except:
  pass
 try:
  f = open("/etc/cluster/conf/slurm")
  slurm_packages = f.read()
  f.close()
 except:
  pass
 try:
  f = open("/etc/cluster/nodes/" + hostname + "/disk-config")
  diskconfig = f.read()
  f.close()
 except:
  diskconfig = '''bootloader --location=mbr --driveorder=sda,sdb
clearpart --all --drives=sda,sdb
part raid.01 --size=500 --ondisk=sda
part raid.02 --size=500 --ondisk=sdb
part swap --size=20000 --ondisk=sda
part swap --size=20000 --ondisk=sdb
part raid.11 --size=1 --grow --ondisk=sda
part raid.12 --size=1 --grow --ondisk=sdb
raid /boot --level=1 --fstype=ext4 --device=md0 raid.01 raid.02
raid / --level=0 --fstype=ext4 --device=md1 raid.11 raid.12
'''
  
except:
  pass

print '''
install
%s
%s
%s
%s
%s
%s
%s
%s
reboot

lang en_US.UTF-8
keyboard fi
vnc

network --bootproto dhcp
firewall --disabled
selinux --disabled
rootpw --iscrypted $6$BsW1hOkk$WN9RjeVuYVH4FLI8YfW0EtnR4C0pTAxQSTreE8G0/AyXxCe9uYPvHcY9ExxZLY/D1zxVnkYMOCx.h/aUioRyO0
authconfig --enablenis --nisserver %s --nisdomain %s
timezone --utc Europe/Helsinki

services --enabled ypbind,slurm,munge,nscd,ntpd,gmond,rdma,mcelogd,hp-health,fetch-crl-cron,fetch-crl-boot,cgconfig

zerombr
%s

%%pre
rdate -s pulse.fgi.csc.fi
hwclock -w

%%post
modprobe nfs
mount -tnfs %s:/etc/cluster /mnt
for script in /mnt/scripts/*.sh ; do
 "$script"
done
umount /mnt

%%packages
@infiniband
openssh-server
ypbind
nfs-utils
munge
#slurm-munge
#slurm
nscd
pdsh
mcelog
ganglia-gmond
ganglia-gmond-python
openmpi
hponcfg
hp-health
glibc.i686
zlib.i686
libxml2.i686
libgcc.i686
libstdc++.i686
fgi-release6
cvmfs-release
cvmfs-repofiles-fgi
epel-release
elrepo-release
yum-plugin-fastestmirror
libcgroup
-redhat-lsb-graphics
-phonon-backend-gstreamer
-qt-x11
'''  % (installurl, securityurl, fgiurl, epelurl, localurl, cvmfsurl, elrepourl, egitrustanchorsrepourl, installnode, clustername, diskconfig, installnode)
print extra_packages
print fgi_packages

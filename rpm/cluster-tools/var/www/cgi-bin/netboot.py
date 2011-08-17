#!/usr/bin/python
import sys
import os
import socket
sys.stderr = sys.stdout
print "Content-Type: text/plain"
print

try:
  clusterconf = open("/etc/cluster/conf/cluster.conf")
  clustersettings = {}                                
  for line in clusterconf.readlines():                
   #for every line, e.g. "key=value", set clusterconf["key"]="value"
   clustersettings[line.split("=")[0]] = line.split("=")[1].strip() 

  address = clustersettings["INSTALLNODEIP"]
  repourl = clustersettings["OS_REPOURL"]
  hostname = socket.gethostbyaddr(os.environ["REMOTE_ADDR"])[0].split(".")[0]
  os.stat("/etc/cluster/nodes/" + hostname + "/reinstall")
  #boot from network to reinstall
  print "#!ipxe"
  print "kernel " + repourl + "/isolinux/vmlinuz ks=http://" + address + "/cgi-bin/ks.py ksdevice=link"
  print "initrd " + repourl + "/isolinux/initrd.img"
  print "boot"
except:
  # Boot fron hd if we can't find the hostname or if we cen't find a reinstall file for the host
  print "#!ipxe"
  print "sanboot --no-describe --drive 0x80"


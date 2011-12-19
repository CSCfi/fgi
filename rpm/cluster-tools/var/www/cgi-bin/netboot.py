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
   #comment lines will throw an error, skip them
   try:
    clustersettings[line.split("=")[0]] = line.split("=")[1].strip()
   except:
    pass


  address = clustersettings["INSTALLNODEIP"]
  repourl = clustersettings["OS_REPOURL"]
  # from the name, e.g. c1-3.local take c1-3, also support hostnames like c1-3-eth.local. if the hostname ends in -eth or -ib, remove those 
  hostname = socket.gethostbyaddr(os.environ["REMOTE_ADDR"])[0].split(".")[0]
  if hostname.endswith("-eth") or hostname.endswith("-ib"):                                                                                                 
   hostname = hostname.rsplit("-", 1)[0]
  os.stat("/etc/cluster/nodes/" + hostname + "/reinstall")
  #boot from network to reinstall
  if "gPXE" in os.environ["HTTP_USER_AGENT"]:
   print "#!gpxe"
  else:
   print "#!ipxe"
  print "kernel " + repourl + "/isolinux/vmlinuz ks=http://" + address + "/cgi-bin/ks.py ksdevice=bootif BOOTIF=01-${net0/mac} blacklist=nouveau edd=off"
  print "initrd " + repourl + "/isolinux/initrd.img"
  print "boot"
except:
   # Boot fron hd if we can't find the hostname or if we can't find a reinstall file for the host
  if "gPXE" in os.environ["HTTP_USER_AGENT"]:
   print "#!gpxe"
   print "exit"
  else:
   print "#!ipxe"
   print "sanboot --no-describe --drive 0x80"

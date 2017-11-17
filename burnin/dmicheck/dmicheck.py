#!/usr/bin/python
import commands

output = commands.getoutput("/usr/sbin/dmidecode -t 17").split("\n")
memarray = {}
error = 0

for line in output:
 if "Size" in line:
  try:
   mem = int(line.split(":")[1].strip().split(" ")[0])
  except:
   mem= 0
 if "Set" in line:
  try:
   slot = int(line.split(":")[1].strip())
  except:
   print "Error determining memory slots, exiting"
   exit(1)
  memarray[slot] = mem

for mslots in ((1,3,5), (2,4,6), (7,9,11), (8,10,12)):
 if memarray[mslots[0]] == 0:
  if memarray[mslots[1]] != 0 or memarray[mslots[2]] != 0:
   print "memory seems to be strangely configured in slots " + str(mslots[0]) + ", " + str(mslots[1]) + ", " + str(mslots[2])
   error =1
 else:
  if memarray[mslots[1]] == 0 or memarray[mslots[2]] == 0:
   print "memory seems to be strangely configured in slots " + str(mslots[0]) + ", " + str(mslots[1]) + ", " + str(mslots[2])
   error = 1

if error == 0:
 print "Memory configuration seems OK!"
else:
 print "There might be something wrong with the memory config"
 print "Memory slot configuration:"
 for i in range (1, len(memarray)+1):
  print str(i) + ": " + str(memarray[i])


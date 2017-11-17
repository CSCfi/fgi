#!/bin/bash

for f in `cat /etc/machines` ; do
 sbatch -w $f bonnie.sh
done

#!/bin/sh
#SBATCH -N 2
#SBATCH --time 86400
#SBARCH --tasks-per-node=1

srun  -l `pwd`/iperf-node.sh $1

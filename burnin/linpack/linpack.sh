#!/bin/sh
#SBATCH -N 1

cd $HOME/burnin/linpack_10.3.7/benchmarks/linpack/
for i in `seq 15` ; do 
 ./runme_xeon64
done


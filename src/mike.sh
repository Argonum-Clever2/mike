#!/bin/bash
#SBATCH --nodes=1
#SBATCH --job-name=art/allo_kmc
#SBATCH --partition=low,amd,smp01
#SBATCH --ntasks-per-node=1


CURDIR=`pwd`

#python allo.py
./iter
#art_illumina -ss HS25 -i ../ ancestorAC.fasta -p -l 150 -f 10 -m 200 -s 10 -o ancestorAC_

#for line in `ls | grep '.fasta'` ; do name=`echo $line | awk -F '[.]' '{print $1}'`; art_illumina -ss HS25 -i "$line" -p -l 150 -f 10 -m 200 -s 10 -o "fqdir/"$name"_"; done



#for line in `ls fqdir/ | grep ".fq"`; do name=`echo $line | awk -F '[_]' '{print $1}'`; path=`pwd`; echo "$path/fqdir/$line" >> "$name.list"; done

#for line in `ls | grep '.list'`; do kmc -k21 @"$line" "$line" .; done;

#for line in `ls | grep '.kmc_pre'`; do  name=`echo $line | sed 's/\(.*\).kmc_pre/\1/'`; kmc_tools transform $name -ci2 sort . dump -s $name".txt"; done 



#/public/home/wangfang/tmp3/iter
#/public/home/wangfang/tmp3/combine

#CURDIR="/public/home/wangfang/simulate/simulate_b/fqdir/similarity"

#for line in `ls | grep -E 'fqdir/similarity/*.jac'`; do path=`pwd`; echo "$path/$line" >> "$path/filelist"; done

#/public/home/wangfang/tmp3/dist



# mash

#sh program.sh

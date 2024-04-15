# mike
## Requirements

C++ version: C++11

R Language version: 3.2.2 or above but not exceed 4.0

python version: 3.6 or higher

kmc(https://github.com/refresh-bio/KMC.git)

**Attention: if you use C++17, it maybe reports errors.**
**When naming files, please use '_' as separators instead of '.', as using '.' will cause program errors.**

## Installation

If you show error message when installing R package, you can skip the installation of R package and build the tree manually in the last step.

```bash
git clone https://github.com/Argonum-Clever2/mike.git
cd src
make
# install R package
Rscript install.r
```



## Tutorial
### The First Step
You need to install KMC in advance, and add kmc to PATH. Then, run command below. The file will be processed into a kmer file. Or you can input the kmer file directly, just skip the step.

 
```python
# help
python kmc.py --help
# run
python kmc.py -f file1 file2 file3 file4 file5 file6 -d dirpath
```

for example，we have multiple fastq files, and use kmc.py to process into kmer files.
![image](https://github.com/Argonum-Clever2/mike/assets/84487311/7831a5de-58cc-4c51-94b0-e663595f0d25)

`python ../mike-master/src/kmc.py -f /data0/stu_wangfang/tmptmp/E200008917_L01_171_1.fq.gz /data0/stu_wangfang/tmptmp/E200008917_L01_171_2.fq.gz -d /data0/stu_wangfang/tmp -t 10`
![image](https://github.com/Argonum-Clever2/mike/assets/84487311/82033d64-4aa2-49e1-ab28-3c5401f0f06d)
![image](https://github.com/Argonum-Clever2/mike/assets/84487311/f3107bbd-ae47-4662-9c5f-98b063cd6bae)

We will get a kmer file(E200008917_L01_171.txt) in txt file format, the content of the file should be as follows.

![image](https://github.com/Argonum-Clever2/mike/assets/84487311/44769bed-3ef0-47aa-b5f8-7020dfe45702)

If the python kmc.py script gives an error, you can also just run the **kmc** command to process all kmc-acceptable file formats into kmer files.
```bash
# kmc--first step
## single-end sequencing file
kmc -k21 -t10 INPUT.fastq OUTPUT_PREFIX DIRPATH
## paired-end sequencing file--write two sequencing files to a file list(INPUT.fastq.list)
kmc -k21 -t10 @INPUT.fastq.list OUTPUT_PREFIX DIRPATH

# kmc-second step
kmc_tools transform OUTPUT_PREFIX sort . dump -s OUTPUT_PREFIX.txt

```
If your file type is fasta , you need to add the -fm parameter.

`for line in `ls | grep -E "E200008917*"`; do path=`pwd`; echo ${path}/${line} >> list; done`

`kmc -k21 -fq -t10 @list E200008917 .`

`kmc_tools transform E200008917 sort . dump -s E200008917.txt`

![image](https://github.com/Argonum-Clever2/mike/assets/84487311/1e64c62f-56a2-48b4-8d1e-74c0b08225cd)



#### kmer file
the format of a kmer file should like below. Each line consists of a 21-mer string and a number representing the frequency of occurrence of that 21-mer string, separated by a '\t'.

AAAAAAAAAAAAAAAAAAAAA   255
AAAAAAAAAAAAAAAAAAAAC   255
AAAAAAAAAAAAAAAAAAAAG   255
AAAAAAAAAAAAAAAAAAAAT   255
AAAAAAAAAAAAAAAAAAACA   255
AAAAAAAAAAAAAAAAAAACC   255
AAAAAAAAAAAAAAAAAAACG   255

...   ...

#### filelist
The filelist means the file that includes a list of kmer files. The filelist needs to include the absolute path and filename.

ABSOLUTE_PATH/kmer_name_file_1

ABSOLUTE_PATH/kmer_name_file_2

ABSOLUTE_PATH/kmer_name_file_3

...   ...

![image](https://github.com/Argonum-Clever2/mike/assets/84487311/256a0732-3df9-4f66-b5cd-7e35f3be1cf9)


### The Second Step
#### SKETCH

The second step is to process the kmer files in the filelist as sketched files, note that you need to enter the absolute paths

```bash

./mike sketch -t 10 -l ABSOLUTE_PATH/filelist -d DIRPATH

```

First, create a list containing all the kmer files that need to be processed.You will get a file ending with 'jac'.
![image](https://github.com/Argonum-Clever2/mike/assets/84487311/0c6c8d41-1694-42f1-80c9-4ad3563e56b8)
![image](https://github.com/Argonum-Clever2/mike/assets/84487311/3888b31b-85d7-463f-8dda-91e9f454719b)
![image](https://github.com/Argonum-Clever2/mike/assets/84487311/d110d23d-3358-4677-9e26-3c2522710c36)


#### sketched filelist
The sketched file is the file obtained in the previous step, which ends with 'jac'. The **sketched filelist** is the file that includes a list of sketched file.

ABSOLUTE_PATH/sketched_file_1.jac

ABSOLUTE_PATH/sketched_file_2.jac

ABSOLUTE_PATH/sketched_file_3.jac

...   ...


![image](https://github.com/Argonum-Clever2/mike/assets/84487311/0518898d-3afa-4749-ba3a-1c121f4c642d)
![image](https://github.com/Argonum-Clever2/mike/assets/84487311/40acccf1-b9e0-46e0-9e92-1ea13630f786)


### The Third Step

#### the Jaccard coefficient 
compute the pairwise Jaccard coefficient, and then will generate the file named jaccard.txt in destination_path
```bash

./mike compute -l ABSOLUTE_PATH/sketched_filelist -L ABSOLUTE_PATH/sketched_filelist -d DIRPATH

```

#### the evolutionary distance

compute the evolutionary distance，and then will generate the file named dist.txt in destination_path
```bash

./mike dist -l ABSOLUTE_PATH/sketched_filelist -L ABSOLUTE_PATH/sketched_filelist -d DIRPATH

```

### The Final Step

#### construction the phylogenetic tree

using the evulutionary distance (dist.txt) to construct the phylogenetic tree without branch length.
**the file titled dist.txt was generated from the evolutionary distance**
```bash
Rscript draw.r -f dist.txt -o dist.nwk
```

If the final step encounters an error, you can manually construct the phylogenetic tree by opening **RStudio**, download the ape package, and input the file dist.txt.
```R
install.packages("ape")
library(ape)
tree <- read.csv("absolute_path/dist.txt", sep='\t', header = TRUE, row.names = 1)
treedist <- as.dist(tree)
# bionj
tree <- bionj(treedist)
# nj
tree <- nj(treedist)
# output
write.tree(tree, "tree.nwk")

```

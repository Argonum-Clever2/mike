# mike
## Requirements

C++ version: C++11

R Language version: 3.2.2 or above but not exceed 4.0

python version: 3.6 or higher

kmc(https://github.com/refresh-bio/KMC.git)

**Attention: if you use C++17, it maybe reports errors.**

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
### The Fisrt Step
You need to install KMC in advance, and add kmc to PATH. Then, run command below. The file will be processed into a kmer file. Or you can input the kmer file directly, just skip the step.

 
```python
# help
python kmc.py --help
# run
python kmc.py -f file1 file2 file3 file4 file5 file6 -d dirpath
```

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

### The Second Step
#### SKETCH

The second step is to process the kmer files in the filelist as sketched files, note that you need to enter the absolute paths

```bash

./mike sketch -t 10 -l ABSOLUTE_PATH/filelist -d DIRPATH

```
#### sketched filelist
The sketched file is the file obtained in the previous step, which ends with 'jac'. The **sketched filelist** is the file that includes a list of sketched file.

ABSOLUTE_PATH/sketched_file_1.jac

ABSOLUTE_PATH/sketched_file_2.jac

ABSOLUTE_PATH/sketched_file_3.jac

...   ...

### The Third Step

#### the Jaccard coefficient 
compute the jaccard coefficient for pairwire, and then will generate the file named jaccard.txt in destination_path
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

If the final step encounters an error, you can manually construct the phylogenetic tree by opening **RStudio**, downloading the ape package, and inputting the file dist.txt.
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

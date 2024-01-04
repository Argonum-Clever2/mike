# mike
## Requirements

C++ version: C++11

R Language version: 3.2.2 or above but not exceed 4.0

python version: 3.6 or higher

kmc(https://github.com/refresh-bio/KMC.git)

**Attention: if you use C++17, it maybe reports errors.**

## Installation
```bash
git clone https://github.com/Argonum-Clever2/mike.git
cd src
make
Rscript install.r
```

## Tutorial
### the first step
You need to install KMC in advance, and add kmc to PATH. Then, run command below. The file will be processed into a kmer file. Or you can input the kmer file directly, just skip the step.
 
```python
# help
python kmc.py --help
# run
python kmc.py -f file1 file2 file3 file4 file5 file6 -d dirpath
```
 
#### kmer file
the format of a kmer file should like below, it is a string of kmer and the frequency file.

AAAAAAAAAAAAAAAAAAAAA   255

AAAAAAAAAAAAAAAAAAAAC   255

AAAAAAAAAAAAAAAAAAAAG   255

AAAAAAAAAAAAAAAAAAAAT   255

AAAAAAAAAAAAAAAAAAACA   255

AAAAAAAAAAAAAAAAAAACC   255

AAAAAAAAAAAAAAAAAAACG   255

...   ...

#### filelist
filelist means the file that includes a list of kmer files:

absolute_path/kmer_file_1

absolute_path/kmer_file_2

absolute_path/kmer_file_3

...   ...

### the second step
#### SKETCH
sketch the genome skims, and the sketch file is in destination_path.
```bash

./mike sketch -t 10 -l filelist -d destination_path

```
#### sketched filelist
the **sketched filelist** is the file that includes a list of sketched file obtained in the previous step.

the format of sketched file like this:

0       1 

1       35   

2       4  

3       4   

4       10      

...   ...

### the third step

#### the Jaccard coefficient 
compute the jaccard coefficient for pairwire, and then will generate the file named jaccard.txt in destination_path
```bash

./mike compute -l sketched_filelist_1 -L sketched_filelist_2 -d destination_path

```

#### the evolutionary distance

compute the evolutionary distance，and then will generate the file named dist.txt in destination_path
```bash

./mike dist -l sketched_filelist_1 -L sketched_filelist_2 -d destination_path

```

### the final step

#### construction the phylogenetic tree

using the evulutionary distance (dist.txt) to construct the phylogenetic tree without branch length.
**the file titled dist.txt was generated from the evolutionary distance**
```bash
Rscript draw.r -f dist.txt -o dist.nwk
```

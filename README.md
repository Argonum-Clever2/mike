# mike
## Installation
```bash
git clone https://github.com/Argonum-Clever2/mike.git
cd mike/src
# if not use PREFIX, the binary file will copy to mike/bin
make install PREFIX=/path/to/install/mike

```

## Tutorial
### preparation
You need to install seqkit and KMC in advance, and then run command below. The file will be processed into a kmer file.

```python
python3 kmc.py -f file.fastq -d dirpath

```

### jaccard index
to compute jaccard index, two steps are required.
#### the input file 
the input file is kmer file.
#### the first step 
sketch the genome skims, and the sketch file is in destination_path.
```bash
# sketch the genome fasta/fastq
# if you have a list of files
./mike sketch -t 10 -l filelist -d destination_path
# if you just want to process a file
./mike sketch -t 10 -l file -d destination_path
```
#### the second step
compute the jaccard index and distance for pairwire
```bash
# if you have a list of filelist_1 of sketched files and other list of filelist_2 of sketched files
./mike compute -l filelist_1 -L filelist_2 -d destination_path
# if you have a list of filelist_1 of sketched files and a sketched file
./mike compute -l Sketchfilelist_1 -f Sketchfile -d destination_path
# if you have a sketchedfile_1 and other Sketchedfile_2
./mike compute -f Sketchedfile_1 -F Sketchedfile_2
```



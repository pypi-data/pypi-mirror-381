PlasmidFinder
===================

This project documents the PlasmidFinder service

*IMPORTANT*: It must be noted that a webserver implementing the methods is freely available at the [CGE website](http://www.genomicepidemiology.org/) and can be found here:
https://cge.food.dtu.dk/services/PlasmidFinder/.


Documentation
=============

The PlasmidFinder service is a service that identifies plasmids in total or partial sequenced
isolates of bacteria, and it is implemented in the three following python scripts:
1. *\__init\__.py* contains the current version of the service.
2. *\__main\__.py* is the file that runs the service.
3. *functions.py* defines some of the functions called by \__main\__.py.


## Content of the repository
1. *\__init\__.py*, *\__main\__.py* and * function.py*       - the program
2. test     	- this folder contains fsa and fq files for testing purposes. Refer to the file called READ_ME_test_info.md for more information. 
3. tests      - this folder contains pytest 
4. README.md        
5. Dockerfile   - dockerfile for building the plasmidfinder docker container


## Installation #TODO

This service may be run with or without a Docker container. Please refer to the corresponding sections: *1.Installation with Docker* or *2.Installation without Docker*.



### 1. Installation with Docker
TODO (just docker run #name (check resfinder readme))
As mentioned, the Dockerfile is included in the repository and will be downloaded when it is cloned.

Setting up PlasmidFinder program
``` bash
# Go to wanted location for plasmidfinder
cd /path/to/some/dir
# Clone and enter the plasmidfinder directory
git clone https://bitbucket.org/genomicepidemiology/plasmidfinder.git
cd plasmidfinder
```

Build Docker container
```bash
# Build container
docker build -t plasmidfinder .
# Run test
docker run --rm -it \
       --entrypoint=/test/test.sh plasmidfinder
```

#Download and install PlasmidFinder database

```bash
# Go to the directory where you want to store the plasmidfinder database
cd /path/to/some/dir
# Clone database from git repository (develop branch)
git clone https://bitbucket.org/genomicepidemiology/plasmidfinder_db.git
cd plasmidfinder_db
PLASMID_DB=$(pwd)
# Install PlasmidFinder database with executable kma_index program
python3 INSTALL.py 
```

If kma_index has no bin install please install kma_index from the kma repository:
https://bitbucket.org/genomicepidemiology/kma

### 2. Installation without Docker

(we discourga people from cloning, just use pip install and download the database, check Resfinder)

In order to run this program without docker files, the user must first make sure to have all needed dependencies installed in their device. 

In order to run the program without using docker, Python 3.5 (or newer) should be installed along with the following versions of the modules (or newer).

#### Modules
- cgecore 1.5.5
- tabulate 0.7.7

Modules can be installed using the following command. Here, the installation of the module cgecore is used as an example:
```bash
pip3 install cgecore
```
#### KMA and BLAST
Additionally KMA and BLAST version 2.8.1 or newer should be installed.
The newest version of KMA and BLAST can be installed from here:
```url
https://bitbucket.org/genomicepidemiology/kma
```

```url
ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/
```










## Usage

The program can be invoked with the -h option to get help and more information of the service.
Run Docker container:


<!-- ```bash
# Run plasmidfinder container
docker run --rm -it \
       -v $PLASMID_DB:/database \
       -v $(pwd):/workdir \
       plasmidfinder -i [INPUTFILE] -o [OUTDIR] [-d] [-p] [-mp] [-l] [-t]
```

When running the docker file you have to mount 2 directories: 
 1. plasmidfinder_db (PlasmidFinder database) downloaded from bitbucket
 2. An output/input folder from where the input file can be reached and an output files can be saved. 
Here we mount the current working directory (using $pwd) and use this as the output directory, 
the input file should be reachable from this directory as well. The path to the infile and outfile
directories should be relative to the mounted current working directory.

`usage: plasmidfinder.py [-h] -i INFILE [INFILE ...] [-o OUTDIR] [-tmp TMP_DIR] [-mp METHOD_PATH] [-p DB_PATH] [-d DATABASES] [-l MIN_COV] [-t THRESHOLD] [-x]
                        [--speciesinfo_json SPECIESINFO_JSON] [-q]`

`-i INPUTFILE	input file (fasta or fastq) relative to pwd, up to 2 files`

`-o OUTDIR	outpur directory relative to pwd`

`-d DATABASE    set a specific database`

`-p DATABASE_PATH    set path to database, default is /database`

`-mp METHOD_PATH    set path to method (blast or kma)`

`-l MIN_COV    set threshold for minimum coverage`

`-t THRESHOLD set threshold for mininum blast identity`



#add these arguments that are missing -->

### Usage:
` __main__.py [-h] -i INFILE [INFILE ...] [-o OUTDIR] [-tmp TMP_DIR] [-mp METHOD_PATH] [-p DB_PATH] [-d DATABASES] [-l MIN_COV] [-t THRESHOLD] [-x] [--speciesinfo_json SPECIESINFO_JSON] [-q] [-j OUT_JSON]`


### Options:

  `-h, --help            show this help message and exit`

  `-i INFILE, --infile INFILE         FASTA or FASTQ input files relative to pwd, up to two files. (REQUIRED)`

  `-o OUTDIR, --outputPath OUTDIR         Output directory relative to pwd. (RECOMMENDED)`

  `-tmp TMP_DIR, --tmp_dir TMP_DIR        Temporary directory for storage of the results from the external software.`

  `-mp METHOD_PATH, --methodPath METHOD_PATH            Path to the method to use (kma or blastn).`

  `-p DB_PATH, --databasePath DB_PATH            Path to the databases directory.`

  `-d DATABASES, --databases DATABASES           Databases chosen to search in - if nothing is specified, all databases available will be used by default.`

  `-l MIN_COV, --mincov MIN_COV           Minimum coverage: minimum percentage of coverage between a plasmid and uploaded data. All plasmids with a % coverage equal or larger than the selected threshhold will be shown in the output. DEFAULT VALUE= 0.60`

  `-t THRESHOLD, --threshold THRESHOLD           Minimum threshold for identity: the minimum percentage of nucleotides that are identical between the best matching resistance gene in the database and the corresponding sequence in the genome. All genes with a %ID equal or larger than the selected threshold will be shown in the output. DEFAULT VALUE= 0.90.` 

  `-x, --extented_output           Gives extented output with allignment files, template and query hits in fasta and a tab seperated file with gene profile results.`

  
  `-q, --quiet`
  
  `-j OUT_JSON, --json OUT_JSON         Path to the file in the (new) BeOne JSON format. If no argument is provided, the program will output the results to the default name.`  

  `--legacy       Only choose this option if you want the legacy JSON file (PlasmidFinder < 3.0.0)`

### Example

```bash
	python3 ~/my_directory/plasmidfinder_3.0.0/src/plasmidfinder/__main__.py -i my_file_to_analyse.fsa -p /home/people/s232520/NEW_plasmidfinder_db/ -j my_output_file.json

```
### Notes

- If neither -j or --legacy are chosen, the program will output the newer (BeOne) format by default. The file will be written to the current directory with the name "results_<INPUT_FILE_NAME>.json". The extended output option can stil be chosen regardless. 

##  For developers
### a. Using a dependency manager
In order to simplify the installation of this service, the dependencies are managed by PDM. Please refer to this web page for an in-depth explanation of this library and alternative installation methods: https://pdm.fming.dev/latest/ . To install PDM please run the following lines. Note that Python 3.7 or higher is required to run PDM. An alternative to using PDM is provided below. 

In short, the following commands must be run for Linux or Mac:
```bash
curl -sSL https://pdm.fming.dev/install-pdm.py | python3 -w
```
And the following should be run for Windows:

```bash
(Invoke-WebRequest -Uri https://pdm.fming.dev/install-pdm.py -UseBasicParsing).Content | python -
```

### b. Without using a dependency manager
If you do not wish to use the dependency manager, you must keep in mind the following depedencies:

* Python 3.5 (or newer)
* cgecore 1.5.5 (or newer)
* tabulate 0.7.7 (or newer)
* cgelib
* pandas
* biopython 

These can be installed using pip as follows:
```bash
pip3 install cgecore
```
-----------
#### Attention! KMA and BLAST
Additionally KMA and BLAST version 2.8.1 or newer should be installed.
The newest version of KMA and BLAST can be installed from here:
```url
https://bitbucket.org/genomicepidemiology/kma
```

```url
ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/
```
#### Installation of the library and database

Setting up PlasmidFinder program. The following code will download the library in your chosen directory.
```bash
# Go to wanted location for plasmidfinder
cd /path/to/some/dir
# Clone and enter the plasmidfinder directory
git clone https://bitbucket.org/genomicepidemiology/plasmidfinder.git
```

Then, the PlasmidFinder database will be downloaded into your chosen directory.

```bash
# Go to the directory where you want to store the plasmidfinder database
cd /path/to/some/dir
# Clone database from git repository (develop branch)
git clone https://bitbucket.org/genomicepidemiology/plasmidfinder_db.git
cd plasmidfinder_db
PLASMID_DB=$(pwd)
# Install PlasmidFinder database. NOTE that KMA needs to have been installed for the following comand. 
python3 INSTALL.py 
```





Citation
=======

When using the method please cite:

PlasmidFinder and pMLST: in silico detection and typing of plasmids.
Carattoli A, Zankari E, Garcia-Fernandez A, Volby Larsen M, Lund O, Villa L, Aarestrup FM, Hasman H.
Antimicrob. Agents Chemother. 2014. April 28th.
[Epub ahead of print]

References
=======

1. Camacho C, Coulouris G, Avagyan V, Ma N, Papadopoulos J, Bealer K, Madden TL. BLAST+: architecture and applications. BMC Bioinformatics 2009; 10:421. 
2. Clausen PTLC, Aarestrup FM, Lund O. Rapid and precise alignment of raw reads against redundant databases with KMA. BMC Bioinformatics 2018; 19:307. 

License
=======

Copyright (c) 2014, Ole Lund, Technical University of Denmark
All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
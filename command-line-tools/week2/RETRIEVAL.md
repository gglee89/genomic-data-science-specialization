# Sequence and Feature retrieval
- **GenBank: Nucleotide, SRA, GEO** (ncbi.nlm.nih.gov)
  Where we can download Genomic sequences
- **USCS Table Browser** (genome.ucsc.edu)
- **Ensembl** (ensembl.org)
  Where and how we can retrieve information about Genomic features (Gene annotation, promoters, etc.)

# Example to access FASTA sequences (Sanger sequences)
**Let's assume that we would like to retrieve the sequence of one gene. And let's take the IL-2 gene in human.**
1. Go to the website
2. Select the appropriate Database: 
	- Nucleotide (for extracting Nucleotide sequences)
3. Search for the desired DNA: Homo sapiens interleukin 2 (IL2), mRNA
	- IL-2 (Interleukin-2)
	- Homo Sapiens
	- mRNA 
4. Select the sequence type:
	- Genomic
	- Transcript
	- Protein

# Example to access FASTQ sequences (NGS sequences)
- Search: strawberry RNA-seq
- Illumina sequencing of floral transcriptomes in woodland strawberry
  ILLUMINA (Illumina HiSeq 2000)
  run: 15.5M spots, 790.4M bases, 553.9 Mb downloads
  "This is NOT considered as a big dataset"
- Experiment number: SRX426518
- Study Summary: SRP03508 
  More information about the project because it might have multiple samples and they usually do.
- Metadata: Description of the project
- Reads: Individual reads
- Download: Downloading SRA data.
  We're interested of using `wget` to download the file.
  SRR###: Sample number
  SRR#######: Experiment number
  `wget ftp://ftp-trace.ncbi.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/SRR110/SRR1107997/SRR1107997.sra`
- `head SRR1007997.sra` will output file in unreadable format
- In order to produce the appropriate format, we have to run a new utility: `nohup fastq-dump SRR1007997.sra &`
	- Start with the comman `hup` (No Hangup). Even if I'm going to close my environment on my laptop, this is still going to run on the remote terminal if I walk some place else.
	- Finish with the command `&` to run in background while giving us access to the shell for other commands.
	- While the program is running on the background, any error gets written to the file `nohop.out`
- In the end, the output looks like: `head SSRR1107997.fastq`
- (HELP) `fastq-dump --help`
	- Gives you information about other commands and parameters there are available.

# Table Browser
**[Genes and Gene Predictions]**  
- clade: Mammal
- genome: Human
- assembly: GRCh38/hg38
- group: Genes and Gene Predictions
- track: <Number of tracks/datasets that all relate to the gene type> RefSeq
- table: refGene
- region: <genome | position> 
	- genome:
	- position: chr22 (because it's the shortest one. It's easy to download.)
- identifiers (names/accessions): <N/A>
- filter: <N/A>
- intersection: <N/A>
- correlation: <N/A>
- output format: GTF - gene transfer format (We're also doing it for BED)
- output file: <leave it blank>
- file type returned: <plain text | gzip compressed> plain text

Download the file
- Click on `get output`
- Go to file > Save as...
- Give an informative name: RefSeq.gtf.txt
- Give an informative name: RefSeq.bed.txt 
	- For this particular case, we can see being of `multi-intervals` or `multi-exons records`
	- With the number of blocks, length of each block, and relative start position of each block.

**[Repeats]**  
- clade: Mammal
- genome: Human
- assembly: GRCh38/hg38
- group: Repeat Master
- track: <Number of tracks/datasets that all relate to the gene type> RefSeq
- table: refGene
- region: <genome | position> 
	- genome:
	- position: chr22:1-50818468 (Chr22 because it's the shortest one. It's easy to download. Full length)
- identifiers (names/accessions): <N/A>
- filter:
	- There are several classes of repeats. We're selecting ALU repeats, because these are the ones we're interested in.
	- repName: Alu\*
- intersection: <N/A>
- correlation: <N/A>
- output format: Browser Extensible Data (BED)
- output file: <leave it blank>
- file type returned: <plain text | gzip compressed> plain text

Download the file
- Click on `get output`
- Go to file > Save as...
- Give an informative name: `Alus.bed.txt`


# Reference  
**Command Line Tools for Genomics**  
John Hopkins University  


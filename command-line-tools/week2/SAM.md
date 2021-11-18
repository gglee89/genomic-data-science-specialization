# SAM
The first portions represent the Header.  
Every line in the header will start with an '@' sign. 

```sam
@HD	VN:1.0 SO:coordinate  	# HEADER - Version and Sorted parameter
@SQ	SN:chr1	LN:248956422	# SEQUENCE - Chromosome and Length
@PG	ID:TopHat	VN:2.0.13
	CL:/data1/igm3/sw
packages/
tophat-2.0.13.Linux_x86_64/
tophat -p -8 -o ...		# PROGRAM

# Alignments
# Everything that is shown below is actually just one line.
```

```sam - alignments
141217_CIDR4_0073_BHCFG7...		Read id
99					FLAG
chr1					Chr
10021					Start
0					Mapping quality
50M					CIGAR(alignment)
=					Mate chr
10151					Mate start
180					Mate dist
ACCTAACCCTAACCCTAACCCTAACCC...		Query seq
@DC?=2.FFGE@7>C62>BGABGB9HFBAF...	Query base quals
AS:i:0					Alignment score
NM:i:0					Edit distance to reference
NH:i:10					Number of hits
XS:A:-					Strand
HI:i:0					Hit index to this alignment

Tags: [A-Za-z][A-Z[a-z]:[AifZH]:.*
      where A=character, i=integer, 
```

#### `FLAG` attribute
SAM Format: FLAG  
Base 10 number representation.
Read the right most bit.

0x1	multiple segments (mates)			# For Illumina reads, if these are "pairs" of reads OR single end reads.
0x2	each segment properly aligned			# [Second bit from the right] This is the "CONCORDANCE" information
0x4 	segment unmapped				# Often times, files might contain records for the sequences that CANNOT be mapped just for the purposes of providing the unified view and complete view of the original dataset.
0x8	next segment unmapped				# Tells if the "next segment" segment in the template, basically it's "mate" in the pair, is unmapped.
0x10	SEQ is reverse complemented in the alignment	# The SEQuence for the current read  has to be "Reverse complemented" to be aligned to match the GENOME
0x20	SEQ of next segment is reverse complemented	# The SEQuence of the next segment/mate had to be "Reverse complemented" to match the GENOME
0x40	first segment (mate)				# The "first segment" in a pair of reads 
0x80	last segment (mate)				# OR whether this is the "last segment" in a pair of reads
0x100	secondary alignment				# Tells us if this is a "secondary" or "primary" alignment for that read based on the quality of the alignment score.
0x200	not passing quality checks			# IF this bit is SET, then it means that the read is NOT passing the quality checks. Maybe the "BASE QUALITY" values are not high enough, OR maybe there are too many 'N's.
0x400	PCR or optical duplicate			# The bit will tell us if this is a "PCR or optical duplicate" 
0x800	supplementary alignment				# Lastly, the left-most but of this segment, will tell us if this is a "supplementary alignment".


***************
*** Example ***
***************

**99 is a representation in base 10, is what we use to represent numerical representation in day-to-day life.**  
**We're going to write that in base 16, decompose it**  
99_10 = 6*16 + 3 = 63_16 = 0000 0110 0011_2

**So we have below 12 bits.**
**Start from the right, and move to the left.**
**We're going to interpret the meaning of the FLAG 99 using the individual meaning of the bits as reflected in the table above** 

0011	Paired, Proper pair, Mapped, Mate mapped
Tells us that these are: 
	- "Paired end reads"
	- The pair is "properly aligned"
	- This segment is "mapped"
	- And its mate is "mapped"
0110	Forward, Mate reverse, first in pair, Not second (last) in pair
Tells us that:
	- The sequence was matching the "forward" direction. Bascially that it did NOT need to be reverse complemented.
	- The "mate", on the other hand, had to be reverse complemented to match the GENOME
	- The read is the "first" in the pair
	- The read is NOT the "last" in the pair

0000	Passed quality check, Not PCR duplicate, Not a suppl. alignment
Tells us that:
	- It passed ALL the "quality checks"
	- It is NOT a PCR duplicate
	- It is NOT a supplementary FLAG

#### `CIGAR` attribute
Used to represent the alignment in a very compressed and rather lengthy form, a CIGAR-like form.  
It can be represented as a sequence of short strings.  
For each string, there's a number following by a letter.  
The letter marks edit operations.  
The numbers tells us how many of those 'edit operations' we have.

```
M	match (sequence match OR substitution)
I	insertion to the reference
D	deletion from the reference
N	skipped region (intron)
S	soft clipping (sequence start or end NOT aligned; seq appears in SEQ)
H	hard clipping (seq NOT in SEQ)
P	padding first segment (mate)
=	sequence match
X	sequence mismatch
```

#### `NM - Edit distance to reference`
Denote the edit distance to the reference. It tells us, how many of those edit operations, how many substitutions, insertions, and deletions we needed to include to equalize to do the mapping between the query and corresponding genomic sequence.

#### `XS - Predicted strand`
It's a **program specific** attribute (i.e.: Given that is starts with X).



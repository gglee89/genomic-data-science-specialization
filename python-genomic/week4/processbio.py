"""
Using BioPython

We can useBiopython to find out where the sequence comes from.
We're not exactly going to use Python itself.
We're going to use a program called BLAST.

BLAST is one of the most successfully, and most widely used
program ever developed in bioinformatics.

It takes a short sequence or maybe a slightly longer sequence of DNA
or protein, and aligns it to a database, which can be very large,
or other sequences, and tells us how the two are related.

So what we want to do here is we want to take our query
sequence that we've collected from a patient and we want to align it
to every bacterium, every virus, every sequence by scientists.
"""

# The server is a BLAST server that's run at NCBI
# National Center for Biotechnology Information
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
import sys

# Get filename argument
filename = sys.argv[1]

# Open and Read
fasta_string = open(filename).read()

# qblast - Blast query method
#
# :return           A handle that we'll be able to look at later
#                   as a way of getting out the results
# :params
#   'blastn':       Name of the program. There are several other ones.
#   'nt':           Which database to search against
#                   Non-redundant nucleotide database of pretty much everything that's store on NCBI.
#   fastastring:    Our short DNA sequence.
#
# :help             help(NCBIWWW.qblast)
result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)

# XML Record
# :return
#   descriptions: list
#       title
#       score
#       e
#       num_alignments
#   alignments: list
#       title
#       length
#       hsps: list
#           score
#           bits
#           ...
#   multiple_alignments
blast_record = NCBIXML.read(result_handle)

# Blast limits the output to 50 matches
len(blast_record.alignments)

# I don't want to see any matches
# which don't have an e value threshold,
# which is one percent or smaller.
# So they are unlikely to be chance matches
E_VALUE_THRESH = 0.001

# Loop through the alignments and
# Loop through the high score pairs (HSP)
# print out the ones with a good e value
for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < E_VALUE_THRESH:
            print('****Alignment****')
            print('sequence:', alignment.title)
            print('length:', alignment.length)
            print('e value:', hsp.expect)
            print(hsp.query)

# Sample output
# Match to a strain of the Ebola virus.
# We were able to find what the patient had.
"""
****Alignment****
sequence: gi|733962926|gb|KP271020.1| Zaire ebolavirus isolate Ebola virus/
H.sapiens-wt/COD/2013/Lomela-Lokolia19, complete genome
length: 18861
e value: 2.89428e-29
CAT...
|||...
CAT...
"""
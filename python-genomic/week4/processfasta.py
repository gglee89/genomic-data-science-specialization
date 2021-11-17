#!/usr/bin/python
"""
processfasta.py builds a dictionary with all sequences from a FASTA file.
"""
import sys

def usage():
    print("""
    processfasta.py: reads a FASTA file and build a dictionary with all sequences
    bigger than a given length.

    processfasta.py [-h] [-l <length>] <filename>
      -h             print this message
      -l <length>    filter all sequences with a length
                  smaller than <length>
                  (default <length>=0)  
      <filename>     the file has to be in FASTA format
    """)

if __name__ == "__main__":    
    filename=sys.argv[1]

    try:
        f = open(filename)
    except IOError:
        print("File %s does not exist!!" % filename)

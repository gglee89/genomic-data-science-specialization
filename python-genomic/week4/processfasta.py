#!/usr/bin/python
"""
processfasta.py builds a dictionary with all sequences from a FASTA file.
"""
import sys
import getopt

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

def start_stop_codon(dna, frame):
    """
    This function checks if given DNA sequence
    has in frame stop codons.
    """
    start_codons=['atg']
    stop_codons=['tga','tag','taa']
    for i in range(frame, len(dna), 3):
        codon = dna[i:i+3].lower()
        if codon in start_codons:
            position1 = i
            for j in range(position1, len(dna), 3):
                codon2 = dna[j:j+3].lower()
                if codon2 in stop_codons:
                    position2 = j
                    yield (position2-position1+3, dna[position1:position2+3], position1, position2)
                    break

if __name__ == "__main__":        
    filename=sys.argv[1]

    """
    o = list of optional arguments
    a = list of required arguments

    when ':' is added just after, this means
    that the option expects a value
    """
    o, a = getopt.getopt(sys.argv[1:], 'l:h')
    opts = {}
    seqlen = 0

    for k,v in o:
        opts[k] = v
    """
    Print out the usage function.
    Multiple lines can be written on the same line
    if they are separated by ';'
    """
    if '-h' in opts.keys():        
        usage(); sys.exit()
    if len(a) < 1:
        usage(); sys.exit("input fasta file is missing")
    if '-l' in opts.keys():
        if int(opts['l']) < 0:
            print("Length of sequence should be positive!"); sys.exit(0)
        seqlen = opts['-l']        

    try:
        f = open(filename) 
    except IOError:
        print("File %s does not exist!!" % filename)        

    seqs = {}
    longest_record_length = 0   

    for line in f:          
        # let's discard the newline at the end (if any)
        line = line.rstrip()
        # distinguish header from sequence
        if line[0] == '>':
            # or line.startswith('>')
            words = line.split()
            name = words[0][1:]
            seqs[name] = ''
        else:
            # concatenate the sequece read
            seqs[name] = seqs[name] + line

    print('Records:', len(seqs.keys()))
    print('Length of longest sequence: ', len(max(seqs.values(), key=len)))
    print('Length of shortest sequence: ', len(min(seqs.values(), key=len)))
    
    # Frame <1,2,3>
    frame = 1
    longest_orf = [0, 0, 0]
    for seq in seqs.values():
        for orflen, orf, start, end in start_stop_codon(seq, frame-1):
            # print(orflen, start, end)
            if orflen > longest_orf[0]:
                longest_orf = [orflen, start, end]

    print("Frame: ", frame)
    print("Longest ORF: ", longest_orf)
    print("")

    identifier = "gi|142022655|gb|EQ086233.1|16"
    frame = 3
    longest_orf = [0, 0, 0]
    for key in seqs.keys():
        if "gi|142022655|gb|EQ086233.1|16" in key:
            for orflen, orf, start, end in start_stop_codon(seqs[identifier], frame-1):
                # print(orflen, start, end)
                if orflen > longest_orf[0]:
                    longest_orf = [orflen, start, end]

    print("Identifier: ", identifier)
    print("Frame: ", frame)
    print("Longest ORF: ", longest_orf)    

    # Find the most frequently occurring repeat of length 6 in all sequences. How many times does it occur in all?
    # repeats = []
    # for seq in seqs.values():
    #     for i in range(len(seq)):
    #         repeats.append(seq[i:i + 12])

    # print('Most common: ', max(set(repeats), key=repeats.count))
    # print("Most frequent: ", repeats.count(max(set(repeats), key=repeats.count)))
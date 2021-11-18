# Scenario 1
Special type of a genomic feature.  
Thinking about a typical application.  
- A **clinical investigator** who wish to sample all the sequence of a number of patients and control.
- To identify and analyze the DNA or RNA variations.
- OR sequencing of a new species, or plant for instance.

[First step]
In either case, this will start by isolating the DNA or the RNA sequencing it.  

[Second step]
Try to place it into genomic context (i.e. Map it to the genome). We call this an `Alignment`

[Third step]
Intuitively, that particular read/sequence came from some place on the genome. So there should be somewhere on the genome a sequence of nucleotides that strongly resembles it.  
Resembles it, but NOT that it is identical because there can be a number of differences. This can be polymorphisms, or they can be errors introduced by sequencing. And our task is to find an `Alignment`

`Alignment` is essentially a mapping between the letters of the read and the letters of the genomic sequence at the particular location of origin where we're matching each base that is identifical between the two, and we're using some **spacers** in order to fill in the gaps or the portions that do not match.

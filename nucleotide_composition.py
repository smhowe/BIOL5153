#! /usr/bin/env python3

#This script calculates the nucleotide composition of a DNA sequence.

# read the DNA file 
# set the name of the input DNA sequence file
filename= 'nt/nad4L.fasta'

#open the input file, assign to file handle called 'infile'
infile= open(filename, 'r') 

#skip the first line aka header line
next(infile)

# read the file
dna_sequence= infile.read().rstrip()
# dna_sequence = dna_sequence.rstrip()

# close the file
infile.close()

# determine sequence length 
seqlen= len(dna_sequence)
print('Sequence Length:', seqlen)

#determine the Frequency of A
numA= dna_sequence.count('A')
freqA= round(numA/seqlen, 3)
print("Freq of A:", "%.3f" %  freqA)

#determine the Frequency of C
numC= dna_sequence.count('C')
freqC= round(numC/seqlen, 3)
print("Freq of C:", "%.3f" %  freqC)

#determine the Frequency of G
numG= dna_sequence.count('G')
freqG= round(numG/seqlen, 3)
print("Freq of G:", "%.3f" %  freqG)

#determine the Frequency of T
numT= dna_sequence.count('T')
freqT= round(numT/seqlen, 3)
print("Freq of T:", "%.3f" %  freqT)

#determine G+C content
numGC= numC + numG
freqGC= round(numGC/seqlen, 3)
print("G+C content:", "%.3f" %  freqGC)

# check that the nucleotide frequencies are equal to 1
print("Nucleotide frequencies sum to 1: ", 1 == (freqA + freqC + freqG + freqT))
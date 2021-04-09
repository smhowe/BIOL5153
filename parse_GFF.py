#! /usr/bin/env python3

import csv
import argparse
from Bio import SeqIO

# this script will parse a GFF file and extract each feature from the genome
# inputs: 1) GFF file, 2) corresponding genome sequence (FASTA format)

#create an argument parser
parser = argparse.ArgumentParser(description= 'this script will parse a GFF file and extract each feature from the genome')

# add positional arguments (NOT OPTIONAL)
parser.add_argument("gff", help= 'name of gff file')
parser.add_argument("fasta", help= 'name of fasta file')

# parse the arguments
args= parser.parse_args()

# read in the fasta file
genome = SeqIO.read(args.fasta, 'fasta')
# print(genome.id) - prints watermelon
# print(genome.seq) - prints the entire sequence 

# open and read in the GFF file
with open(args.gff, 'r') as gff_in:
    # create a csv reader object
    reader = csv.reader(gff_in, delimiter='\t')
    
    # loop over lines in reader (ie parsed file)
    for line in reader:
        start  = int(line[3])-1 # extracts the start position and converts to integer, -1 ensures the first nucleotide is included
        end    = int(line[4])   # extracts the end position and converts to integer
        strand = line[6]        # extracts the which strand the feature is on (ie. + or -)
        info   = line[8]        # extracts the information needed for header 
        
        # print the fasta header 
        print('>' + genome.id, info)
       
        # extract sequence
        if strand == '-': #if the strand is -
            print(genome.seq[start:end].reverse_complement()) # extract the sequence according to the start and end coordinates and then print the reverse complement
        else: print(genome.seq[start:end]) # if strand is not - (ie. +) print the sequnece accoring to start and end coordinates
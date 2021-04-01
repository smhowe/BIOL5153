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

#  parse the arguments
args= parser.parse_args()

# read in the fasta file
genome = SeqIO.read(args.fasta, 'fasta')
print(genome.id)
print(genome.seq)

# open and read in the GFF file
with open(args.gff, 'r') as gff_in:
    # create a csv reader object
    reader = csv.reader(gff_in, delimiter='\t')
    
    # loop over a;; lines in reader (ie parsed file)
    for line in reader:
        start  = line[3]
        end    = line[4]
        strand = line[6]
        # print(start)
        # print(line[3], line[4])

        #extract the sequence
        print(len(genome.seq))

# parse the GFF file


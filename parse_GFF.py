#! /usr/bin/env python3

import csv
import argparse
from Bio import SeqIO
from collections import defaultdict
import itertools

# this script will parse a GFF file and extract each feature from the genome
# inputs: 1) GFF file, 2) corresponding genome sequence (FASTA format)

#create dictionaries:

#dictionary: key: line 8, value: line 8 split by white space
exon= defaultdict(dict)

#dictionary: key: gene name, exon number (gene_exon), value: sequence
sequences = defaultdict(dict) # contains all the CDS seqs

#dictionary: key: gene name, exon number (gene_exon), value: sequence
sort = defaultdict(dict) # this dictionary only has genes with more than one exon

#dictionary: key: alphabetically sorted sort dictionary keys (gene name, exon number), value: sequence
sorted_dict = defaultdict(dict) # the sort dict., but sorted alphabetically

#dictionary: key: gene_name, value: merged sequences
new_dict = defaultdict(dict) # 




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
        exon[info] = info.split(' ') # makes the info in line 8 extractable, splits by whitespace
        spliced_info = info.split(';') # makes the info in line 8 extractable, splits by ;
        gene_exon = spliced_info[0] # extracts gene name and exon number
        gene = gene_exon.split(' ') # splits gene name and exon number by white space, separating them
        
        # extract sequence 
        if line[2] == 'CDS': #if line 2 is CDS, extract the sequence

            if strand == '-': #if the strand is -
                # extract the sequence from the .fsa file, get the rev. complement, and store in sequence dict.
                sequences[gene_exon] = '>' + genome.id, gene_exon, genome.seq[start:end].reverse_complement() # extract the sequence according to the start and end coordinates and then print the reverse complement
            else: #the strand is positive
                # extract the sequence from the .fsa file and store in sequence dict.
                sequences[gene_exon] = '>' + genome.id, gene_exon, genome.seq[start:end] # if strand is not - (ie. +) print the sequnece accoring to start and end coordinates

            if exon[info][2] == 'exon': # this means that the gene has more than 1 exon
                # create a dictionary of the genes with multiple eoxns and their sequence
               sort[gene_exon] = sequences[gene_exon][2]

            else: print('>Citrullus_lanatus_'+ exon[info][1] + '\n' + sequences[gene_exon][2]) # these genes only have one exon, so print the sequence

        else: continue #if it's not, skip 

    # create a current line variable
    current_line = ('1', '1', '1', '1', '1', '1', '1', '1', '1')

    #create a for loop that will sort the sort dictionary (containing only exons)
    for key, value in sorted(sort.items()): 
        #input the sorted dictionary keys and values into a new dictionary
        sorted_dict[key] = value
        
        #create a gene variable
        gene = key.split(' ')[1]

        #create a previous line variable
        previous_line = current_line
    
    # create the final dictionary, containing just the gene name for the key and the properly merged sequences
        if gene == previous_line[1]: # if the gene name is the same as the previous lines gene name then we have seen this before.
            new_dict[gene] += value # so add this sequences to the previous line
            current_line = key.split(' ') # update the current line variable
        else:
            new_dict[gene] = value # this gene name is not equal to the line above
            current_line = key.split(' ') # update the current line variable


# print each gene and compiled sequence       
for key, value in new_dict.items():
    print('>Citrullus_lanatus_'+ key + '\n'+ value)

        
  
   
    
#! /usr/bin/env python3

#define variables
job_name= 'pinnacle_job_script'
queue= 'comp06'
prefix= 'pinnacle_job_script'
node = 1 #this is n nodes
processor= 32 #this is n processors
wall= 6 #this is n hours

#This script generates a SLURM file for the AHPCC Pinnacle cluster

print('#!/bin/bash')
print()

#This section prints the header/required info for the slurm script  
print('#SBATCH -J', job_name) #set job name
print('#SBATCH --partition', queue) #set the queue the job will run on 
print('#SBATCH -o', prefix + '.txt') #set name of job output file
print('#SBATCH -e', prefix + '.err') #set name of job error file
print('#SBATCH --mail-type=ALL') 
print('#SBATCH --mail-user=smhowe@uark.edu')
print('#SBATCH --nodes=' + str(node)) # how many respurces to ask for 
print('#SBATCH --ntasks-per-node=3'+str(processor)) # number of processors 
print('#SBATCH --time='+ str(wall) + ':00:00') #wall time
print()

print('export OMP_NUM_THREADS=32')
print()
 
# load the necessary modules
print('# load required modules')
print("module load python/3.7.3-anaconda")
print()
 
# cd into the directory where you're submitting this script from
print('# cd into directory where the script will be submitted from')
print('cd $SLURM_SUBMIT_DIR')
print()

# commands for this job
print('#insert job commands here')

#! /usr/bin/env python3

#This script generates a PBS file for the AHPCC Razor cluster

#define variables
job_name= 'razor_job_script'
queue= 'med16core'
prefix= 'razor_job_script'
node = 1 #this is n nodes
processor= 1 #this is n processors
wall= 3 #this is n hours

#This section prints the header/required ifo for the PBS script
print('#PBS -N', job_name) #job name
print('#PBS -q', queue) #which queue
print('#PBS -j oe' ) #join stdout and stderr into a single file
print('#PBS -o', prefix + '.$PBS_JOBID') #set the name of the job output file
print('#PBS -l nodes='+str(node)+':ppn=' + str(processor)) # how many resources to ask for (nodes= numnodes, ppn= numprocessors)
print('#PBS -l walltime=' + str(wall) + ':00:00') #set the walltime (default 1 hour)
print()

#cd into working directory
print('cd $PBS_O_WORKDIR')
print()


# load the necessary modules
print('# load modules')
print('module purge')
print('module load gcc/7.2.1')
print()

#commands for this job
print('# insert commands here')
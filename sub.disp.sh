#!/bin/sh
### Set the job name (for your reference)
#PBS -N gypsum_relax
### Set the project name, your department code by default
#PBS -P mech
### Request email when job begins and ends
#PBS -m bea
### Specify email address to use for notification.
#PBS -M mez168274@iitd.ac.in
####
#PBS -l select=24:ncpus=2
### Specify "wallclock time" required for this job, hhh:mm:ss
#PBS -l walltime=02:00:00

#PBS -l software=
# After job starts, must goto working directory.
# $PBS_O_WORKDIR is the directory from where the job is fired.
echo "==============================="
echo $PBS_JOBID
cat $PBS_NODEFILE
echo "==============================="
cd $PBS_O_WORKDIR

#job
module purge
module load apps/quantum_espresso/6.2.1/impi
#module load apps/quantum_espresso/6.0/impi

for i in {0062..0064}
do
        for j in {001..002}
        do
		cp gypsum.ph disp_${i}_${j}/
		cd disp_${i}_${j}/
		mpirun -n 48 -genv OMP_NUM_THREADS=1 -genv I_MPI_PIN_DOMAIN=omp pw.x < gypsum_${i}_${j}.in > gypsum_${i}_${j}.out
		mpirun -n 48 ph.x < gypsum.ph > ph.out
		cd ..
	done
done


#NOTE
# The job line is an example : users need to change it to suit their applications
# The PBS select statement picks n nodes each having m free processors
# OpenMPI needs more options such as $PBS_NODEFILE


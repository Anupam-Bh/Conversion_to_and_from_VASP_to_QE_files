#!/bin/sh
source ~/miniconda_base_setup_pymatgen
conda activate phonopy
python POSCAR_to_QE.py

for i in {0061..0072}
do 
	echo $i
	for j in {001..002}
	do		
		cat header.in QE_in.${i}.${j} > gypsum_${i}_${j}.in;
		mkdir disp_${i}_${j}
		mv gypsum_${i}_${j}.in disp_${i}_${j}/
		rm QE_in.${i}.${j}
	done
done

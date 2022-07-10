#!/bin/sh
source ~/miniconda_base_setup_pymatgen
conda activate phonopy
#python POSCAR_to_QE.py

for i in {0061..0072}
do 
	echo $i
	for j in {001..002}
	do		
		cp OUTCAR QE_BORN_Dielectric_to_OUTCAR.py disp_${i}_${j}/
		cd disp_${i}_${j}/
		python QE_BORN_Dielectric_to_OUTCAR.py
		#mkdir disp_${i}_${j}
		#mv gypsum_${i}_${j}.in disp_${i}_${j}/
		#rm QE_in.${i}.${j}
		cd ..
	done
done

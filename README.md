# Conversion_to_and_from_VASP_to_QE_files (Phonopy-Spectroscopy)
POSCAR file is converted into QE structure input, which can be concatenated with parameters file to create the QE input file. 

Calculated Dielectric constant and BORN charges are read from ph.out file of QE. An OUTCAR file generated from calculation of Dielectric constant for same material is used. Values of Dielectric constant and BORN charges calculated using VASP is replaced with the values from QE. 

These codes can be used to calculate Raman Tensors using Phonopy Spectroscopy (https://github.com/JMSkelton/Phonopy-Spectroscopy) using QE. This code tricks Phonopy-Spectroscopy to think that outputs were generated using VASP.



Steps:
1. Generate the displaced files using   
<code>phonopy-raman -d --bands="..."</code>
2. Generate QE input file using 
<code>sh create_raman_vasp_to_qe_input.sh</code> (It will call POSCAR_to_QE.py and concat header.in file with to create QE input file.)
3. Calculate Dielectric constants (epsil in QE) and BORN charges (zeu in QE) for each structure. 
4. Get an OUTCAR file which was used by VASP calculation to calculate epsilon
5. ph.out values are read and OUTCAR epsilon and BORN charge values are replaced with QE values :
<code> sh phonopy-raman_QE_to_outcar.sh </code> (This will call QE_BORN_Dielectric_to_OUTCAR.py)
6. Next steps are same as described in Phonopy-Spectroscopy page.

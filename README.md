# Conversion_to_and_from_VASP_to_QE_files (Phonopy-Spectroscopy)
POSCAR file is converted into QE structure input, which can be concatenated with parameters file to create the QE input file. 

Calculated Dielectric constant and BORN charges are read from ph.out file of QE. A OUTCAR file used to calculation of Dielectric constant for same material is used. Values of Dielectric constant and BORN charges calculated using VASP is relaced with the values from QE. 

These codes can be used to calculate Raman Tensors using Phonopy Spectroscopy (https://github.com/JMSkelton/Phonopy-Spectroscopy) using QE. This code tricks Phonopy-Spectroscopy to think that outputs are generated using VASP.

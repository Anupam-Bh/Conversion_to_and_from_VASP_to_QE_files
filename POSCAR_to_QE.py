def Cumulative(lists):
    cu_list = []
    length = len(lists)
    cu_list = [sum(lists[0:x:1]) for x in range(0, length+1)]
    return cu_list[1:]


for i in range(61,73,1):
	for j in range(1,3,1):
		file1 = open('Raman-POSCAR.00'+str(i)+'.00'+str(j)+'.vasp', 'r')
		Lines = file1.readlines()
		file1.close()
		file2 = open('QE_in.00'+str(i)+'.00'+str(j), "a")
		for idx, line in enumerate(Lines):
			if idx ==0:
				file2.write("CELL_PARAMETERS (bohr)\n") # Here 'bohr' is very important as QE+phonopy.yaml gives lattice parameter in bohr. 
			if idx in (2,3,4):
				file2.write(line)
			if idx ==5:
				line=line.strip()
				labels=line.split(' ')
				labels= [m for m in labels if m]
				print(labels)
			if idx ==6:
				line=line.strip()
				natoms=line.split(' ')
				natoms= [n for n in natoms if n]
				natoms = [int(x) for x in natoms]
				cum_line=Cumulative(natoms)
				start_line=[0]+cum_line[0:len(cum_line)-1]
				end_line=[nn-1 for nn in cum_line]
				start_line=[x+8 for x in start_line]
				end_line=[x+8 for x in end_line]
				print(natoms)
				print(cum_line)
				print(start_line)
				print(end_line)
			if idx==7:
				file2.write("\nATOMIC_POSITIONS {crystal}\n")
			if idx > 7:
				count=0
				for nn in start_line:
					if idx >= nn:
						count=count+1
						atom_label=labels[count-1]
				file2.write(atom_label+'   '+line)
				
			#for idy,k in natoms:
			#	if idx in (8+idy(
		file2.close()
			



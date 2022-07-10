import re

file1 = open('ph.out', 'r')

# Read dielectric constant and BORN effective charges from ph.out
RLines = file1.readlines()
Dielectric = []
for line in RLines:
    w = re.findall("\s\s\s\s\s\(\s\s.", line)
    if (w):
        e = re.split('\n|\(|\)', line)
        e = [n for n in e if n]
        Dielectric += [e[1]]
print(Dielectric)


countdir = 0
BORN_charge = []
for line in RLines:
    x = re.findall("\s\sEx\s\s\(|\s\sEy\s\s\(|\s\sEz\s\s\(", line)
    if (x):
        f = re.split('Ex\s\s\(|Ey\s\s\(|Ez\s\s\(|\)|\n', line)
        # print(f[1])
        countdir = countdir+1
        # In the OUTCAR each line has a direction index
        f[1] = '  '+str(countdir)+f[1]
        BORN_charge += [f[1]]
        if countdir == 3:
            countdir = 0
print(BORN_charge)
file1.close()


# Replace the Dielectric constant and BORN charge in the OUTCAR
# Replace the Dielectric constant
file2 = open('OUTCAR', 'r')
WLines = file2.readlines()
file2.close()
sw = 0
count = 0
for idx, line in enumerate(WLines):
    w = re.findall("MACROSCOPIC STATIC DIELECTRIC TENSOR", line)
    if (w):
        sw = 1
    if sw == 1:
        count = count+1
        # print(idx)
    if (count == 3 or count == 4 or count == 5):
        WLines[idx] = Dielectric[count-3]+'\n'
        print(WLines[idx])
    if count == 6:
        sw = 0
        count = 0
file = open('OUTCAR', 'w')
file.writelines(WLines)
file.close()

# Replace the BORN charges
found = 0
count = 0
BORN_count = 0
for idx, line in enumerate(WLines):
    w = re.findall("BORN EFFECTIVE CHARGES ", line)
    if (w):
        found = 1
    if found == 1:
        count = count+1
    if count%4 != 3 and count > 3:
        BORN_count = BORN_count+1
        WLines[idx] = BORN_charge[BORN_count-1]+'\n'
    if BORN_count==len(BORN_charge):
        break
file = open('OUTCAR', 'w')
file.writelines(WLines)
file.close()






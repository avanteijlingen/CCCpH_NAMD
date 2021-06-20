import sys
import random # don't use numpy as then we need to module load anaconda
import time

def readin(fname):
    f = open(fname, 'r')
    content = f.read()
    return content
def writeout(fname, content):
    f = open(fname, 'w')
    f.write(content)
    f.close()
def buffer(string, L):
	string = str(string)
	while len(string) < L:
		string = string+"0"
	return string

def logwater(fname, cycle):
	psf = readin(fname).split("!NATOM")[1].split("!NBOND")[0].split("\n")
	atom_lines = [line for line in psf if "H2O" in line]
	charged = []
	for line in atom_lines:
		if len(line.split()) < 7:
			continue
		ID = line.split()[0]
		charge = float(line.split()[-3])
		if charge != 0.0:
			charged.append(ID)
	if cycle == 0:
		log = open("ConstantCharge.log", 'w')
	else:
		log = open("ConstantCharge.log", 'a')
	log.write(str(cycle) + "," + ",".join(charged) + "\n")
	log.close()
	print("Python: Charged waters:", charged)


def neutralise(fname):
	charge = parsepsf(fname)
	# First try to turn off waters we had previously turned on
	if charge == 0:
		return
	elif charge > 0:
		TurnOff(fname, "1.000000", charge)
	elif charge < 0:
		TurnOff(fname, "-1.000000", abs(charge))
	#Check if this did the trick
	charge = parsepsf(fname)
	if charge == 0:
		return
	# Turn on some water molecules to balance the charge
	if charge > 0:
		TurnOn(fname, "-1.000000", charge)
	elif charge < 0:
		#print("Turning on")
		TurnOn(fname, "1.000000", abs(charge))

def TurnOn(fname, C, N):
	psf = readin(fname).split("\n")
	atom_lines = [i for i in range(len(psf)) if "H2O" in psf[i] and "0.000000" in psf[i]]
	for line in random.choices(atom_lines, k=int(min([N, len(atom_lines)]))):
		if float(C) > 0:
			psf[line] = psf[line].replace("0.000000", buffer(C,8))
		else:
			psf[line] = psf[line].replace(" 0.000000", buffer(C,8))
	writeout(fname, "\n".join(psf))
		
def TurnOff(fname, C, N):
	psf = readin(fname).split("\n")
	atom_lines = [i for i in range(len(psf)) if "H2O" in psf[i] and buffer(C,8) in psf[i]]
	for line in random.choices(atom_lines, k=int(min([N, len(atom_lines)]))):
		if float(C) > 0:
			psf[line] = psf[line].replace(buffer(C,8), "0.000000")
		else:
			psf[line] = psf[line].replace(buffer(C,8), " 0.000000")
	writeout(fname, "\n".join(psf))

def parsepsf(fname):
	psf = readin(fname).split("!NATOM")[1].split("!NBOND")[0]
	charge = 0
	for line in psf.split("\n"):
		line = line.split()
		if len(line) < 7:
			continue
		charge += float(line[-3])
	return charge	
	
if __name__ == "__main__":
	random.seed(time.time())
	basename = sys.argv[1]+".psf"
	cycle = int(sys.argv[2])
	print("Python: Args", sys.argv)
	print("Python: Basename", basename)
	print("Python: Inital charge:", parsepsf(basename))
	neutralise(basename)
	print("Python: Neutralised charge:", parsepsf(basename))
	logwater(basename, cycle)

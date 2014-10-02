#!/usr/bin/python

# prob005
# Finde die kleinste Zahl i, die durch alle natuerlichen Zahlen 1 ... n
# geteilt werden kann

# Hier brauchen wir eigentlich gar nicht rechnen, das ganze hat einen einfachen
# Algorithmus:
# 1)  Finde die Primfaktor-Zerlegung fuer jede natuerliche Zahl bis n
# 2)  Schreibe jeweils die groessten Potenzen jedes Primfaktors heraus
# 3)  Multipliziere all diese Faktoren
#
# Das wird aber fuer grosse Zahlen nervig per Hand... also doch ein Script:

import imp
import sys
pn = imp.load_source('primenum', 'tools/primenum.py')


try:
	n = int(sys.argv[1])
except:
	n = 20

resultfacs = {}

for z in range(2, n+1):
	for f in pn.primefac_dict(z):
		#print pn.primefac_dict(z)
		if str(f) in resultfacs:
			if resultfacs[str(f)] < pn.primefac_dict(z)[str(f)]:
				resultfacs[str(f)] = pn.primefac_dict(z)[str(f)]
		else:
			resultfacs[str(f)] = pn.primefac_dict(z)[str(f)]
			
print resultfacs

product = 1
for f in resultfacs:
	product *= int(f)**resultfacs[f]

print product

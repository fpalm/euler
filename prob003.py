#!/usr/bin/python

# prob003.py
# Finde den groessten Primfaktor der Zahl n

import imp, math
pn = imp.load_source('primenum', 'tools/primenum.py')

n = 600851475143

primelist = pn.findprimes(int(math.sqrt(n))+1)
for i in reversed(primelist):
	if n % i == 0:
		print "Groesster Primfaktor: ", i
		break

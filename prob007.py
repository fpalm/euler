#!/usr/bin/python

# prob007.py
# Finde die n-te Primzahl

import imp
pn = imp.load_source('primenum', 'tools/primenum.py')

n = 10001
count = 1

p = 3

while count < n:
	if pn.isprime(p):
		count += 1
	p += 2

print "Die %i te Primzahl ist %i" %(count-1, p-2)

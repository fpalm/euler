#!/usr/bin/bash

# prob008.py
# Finde das groesste Produkt von n aufeinander folgenden Zahlen in prob008.txt

n = 13
f = open('prob008.txt')

numlist = []

for i in f.read():
	numlist.append(int(i))

f.close()

#print numlist

maxprod = 0
for z in range(len(numlist)-(n-1)):
	prod = 1
	for x in range(z, z+n):
		prod *= numlist[x]
	if prod > maxprod:
		maxprod = prod

print maxprod

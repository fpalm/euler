#!/usr/bin/bash

# prob004.py
# Finde die groesste Palindromzahl, die aus der Multiplikation von zwei n-stelligen Zahlen erzeugt werden kann

n = 3
palindromes = []

for x in range(1, 10**n):
	for y in range(1, 10**n):
		p = x*y
		if len(str(p)) % 2 == 0:
			for pos in range(len(str(p))/2):
				if str(p)[pos] != str(p)[-(1+pos)]:
					break
			else:
				palindromes.append(x*y)
		else:
			for pos in range((len(str(p))-1)/2):
				if str(p)[pos] != str(p)[-(1+pos)]:
					break
			else:
				palindromes.append(x*y)

print max(palindromes)

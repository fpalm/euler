#!/usr/bin/python

# prob001.py
# Berechne die Summe aller Vielfachen der Zahlen in base unter n

base = [3, 5]
n = 1000

result = 0

for i in range(n):
	for z in base:
		if i%z == 0:
			result += i
			break

print result

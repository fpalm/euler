#!/usr/bin/python

# prob006.py
# Berechne die Differenz zwischen (1**2+2**2+...+n**2) und (1+2+...+n)**2

n = 100
sum1 = sum([i**2 for i in range(n+1)])
sum2 = sum(range(n+1))**2

print sum2, "-", sum1, "\t = \t", sum2-sum1

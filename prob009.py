#!/usr/bin/bash

# prob009.py
# Finde das Pythagoras-Triple a^2+b^2=c^2, fuer das a+b+c = 1000;  Gib a*b*c aus

import math

a=1
while a:
	#print a
	b = a
	while a + b < 1000 :
		c = math.sqrt(a**2+b**2)
		if a + b + c == 1000:
			print a, b, int(c), a*b*int(c)
			a = b = 0
			break
		else:
			b += 1
	if b != 0:
		a += 1

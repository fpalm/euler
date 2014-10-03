#!/usr/bin/bash

# prob010.py
# Finde die Summe aller Primzahlen unter n

# Praktischerweise haben wir schon ein Modul, das zumindest die Zahlen findet...
import imp
pn = imp.load_source('primenum', 'tools/primenum.py')

n = 2000000
print sum(pn.findprimes(n))

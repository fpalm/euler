#!/usr/bin/python

# prob002.py
# Berechne die Summe aller geraden Fibonacci-Zahlen unter n

n = 4000000

fiblist = [1, 2]
i = 3
result = 2

while i <= n:
	fiblist.append(i)
	i += fiblist[fiblist.index(i)-1]
	if i % 2 == 0:
		result += i

#print fiblist
print result

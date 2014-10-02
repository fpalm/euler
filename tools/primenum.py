def isprime(n):
	primelist = [2, 3, 5, 7]
	if n in primelist:
		return True
	elif n not in primelist and n < 11:
		return False
	else:
		t = 2
		while t*t <= n:
			if n % t == 0:
				return False
			t += 1

		if t*t > n:
			return True

def findprimes(primemax=3, returnList = True):
	primelist = [2, 3]
	p = 5
	if primemax >= 5:
		primelist.append(5)
		p = 7
	if primemax >= 7:
		primelist.append(7)
		p = 11
	while p < primemax:
		if isprime(p):
			primelist.append(p)
		p += 2

	if returnList == True:
		return primelist
	else:
		print primelist[-10:]

def primefac_raw(n):
	import math
	facs = [n]
	primelist = findprimes(int(math.sqrt(facs[0]))+1)
	while not isprime(facs[0]):
		for i in primelist:
			if facs[0] % i == 0 and facs[0]/i > 1:
				facs.append(i)
				facs[0] /= i
				break
	return facs

def primefac_dict(n):
	facs = primefac_raw(n)
	facdict = {}
	for i in facs:
		try:
			facdict[str(i)] += 1
		except:
			facdict[str(i)] = 1
	
	return facdict

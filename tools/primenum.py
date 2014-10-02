def findprimes(primemax, returnList = True):
	primeliste = [2, 3, 5, 7 ]
	p = 11
	while p < primemax:
	    t = 3
	    while  t*t <= p :
	      if p % t == 0 :
	          break
	      t += 2
	    if t*t > p :
	        primeliste.append(p)
	    p += 2

	if returnList == True:
		return primeliste
	else:
		print primeliste[-10:]

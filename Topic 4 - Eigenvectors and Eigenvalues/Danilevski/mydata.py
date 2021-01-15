import numpy as np

def findRoots(a):
	#roots = np.zeros(len(a)-1)
	roots = []
	for r in range(len(a)-1):
		root = newtonHorner(a,0) # initial guess of zero
		if root == None:
			break
		else:
			#print("r",r," = ",root)
			#roots[r] = root
			roots.append(root)
			a = quotient(a, root)
		
	return roots
def quotient(a, x):
	q = np.zeros(len(a))
	q[len(a)-1] = a[len(a)-1]
	for i in range(len(a)-2, -1, -1):
		q[i] = x * q[i+1]+a[i]
	return q[1:len(q)]

def newtonHorner(a, x):
	i = 0
	px = horner(a,x)
	qx = hornerDeriv(a,x)
	while abs(px) > 0.0000001 and i < 1000:
		if qx == 0: # avoid divide by zero
			return None
		x = x - px / qx
		px = horner(a,x)
		#qx = horner(q,x) # Power Rule
		qx = hornerDeriv(a,x) # Ruffini's Rule
		i = i + 1
	
	if i == 1000: # hit the iteration cap (divierging or stuck in loop)
		return None
	
	r = round(x) # check if rounding will give you a better answer
	if(abs(horner(a,r)) < abs(horner(a,x))):
		x = r
	return x

def hornerDeriv(a, x):
	q = quotient(a, x)
	return horner(q,x)
def horner(a, x):
	result = a[len(a)-1]
	for i in range(len(a)-2,-1,-1):
		result = a[i] + x * result
	return result

#p = [-3, -2, -4, -1, 1]
#s = list(reversed(p))
#p = [3,2,1]
#u = findRoots(p)
#print(u)

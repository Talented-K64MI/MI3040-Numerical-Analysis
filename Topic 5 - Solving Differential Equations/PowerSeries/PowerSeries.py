from numpy.core.defchararray import array
from sympy import *
import matplotlib.pyplot as plt
import numpy

x = symbols('x')

#test
#y''' - 2/3 y'' - 2xy' + 6y =0
y = x**3 +x -1
string = diff(y,x,3) - 2/3 * diff(y,x,2) - 2*x*diff(y,x,1) + 6 *y 
string = simplify(string)
print(string)

#input: 
k=3; N=10
arr = numpy.zeros((k,N))
arr[2][0] = -2/3
arr[1][1] = -2
arr[0][0] = 6
print("input: ")
print(arr)


result = [-1,1,0]

#main loops
for n in range(0,N-k):
    c=0
    for m in range(0,n+1):
        mult = 1
        for i in range(0,k):
            c+=arr[i][n-m] * result[m+i] * mult
            mult *= m+i+1
    c= -c/ (n+1) / (n+2) / (n+3)
    result.append(c)

print("result: ")
print(result)
f=0
for n in range(0,N):
    f = f + result[n] * x**n
print(f)
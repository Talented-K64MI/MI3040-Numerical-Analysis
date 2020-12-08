import numpy as np

import bisection
print("Running bisection ... ")
uu = bisection.bisection_oop(1, 5, 0.01, "x**2-2");
print(uu.Solve());

print("---------------------- The End -------------------------")
print("Running newton_ralphson ... ")

from newton_ralphson import *
expr = "x^3 + x^2 - x + 1";
L = -3; R = -1; eps = 1e-12;
uu = newton_oop(L, R, eps, expr);
print(f"Nghiệm của phương trình {expr} trên khoảng [{L}, {R}] là: {uu.Solve()}");

print("---------------------- The End -------------------------")
print("Running Bordering ... ")

import Bordering
a = np.loadtxt("test.txt",dtype='float', delimiter=' ')
if(Bordering.checkdet(a) <0):
    print("eo lam dc")
else:
    n = len(a)
    b = Bordering.bordering(a,n)
    print(b)

print("---------------------- The End -------------------------")
print("Running Pica ... ")

import Pica
filename = "pica1.txt"
result = Pica.Pica(filename)
length = 3
result1 = Pica.Pica1(filename, length)

print(result)
Pica.PlotBoth(result, result1)

print("---------------------- The End -------------------------")
print("Running Cholesky ... ")

import PowerSeries
print("Running PowerSeries ... ")
filename = "PowerSeries.txt"
result = Polynomial(filename)        #example1
print("Radius of convergence = " + str(result[0]) + ", Result: \n")
resultArray = result[1]
print(resultArray)
Plot(resultArray)

print("---------------------- The End -------------------------")

#Save(result,outputPath_1,"w")

#import Cholesky
# 
# 4 methods for 1 task ?!
# im not gonna input each position on the matrix

print("---------------------- The End -------------------------")
print("Running GaussJordan_final ... ")

#import GaussJordan_final
# this code is connected to a hard-defined global var
# in the end, i only use the function, which should connect to my input, not your global var

print("---------------------- The End -------------------------")

#import Cholevsky

# it's literally a function
# so dont put code outside function -_-


#import 


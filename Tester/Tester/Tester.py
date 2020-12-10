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
#Pica.PlotBoth(result, result1)

print("---------------------- The End -------------------------")

import PowerSeries
print("Running PowerSeries ... ")

filename = "PowerSeries.txt"
result = PowerSeries.Polynomial(filename)        #example1
print("Radius of convergence = " + str(result[0]) + ", Result: \n")
resultArray = result[1]
print(resultArray)
#PowerSeries.Plot(resultArray, -2, 2)
PowerSeries.Save(result,"PowerSeries_ouput.txt","w")

print("---------------------- The End -------------------------")
print("Running GaussJordan_final ... ")

from GaussJordan_source import Gauss_Jordan_Algorithms

try:
    RUN = Gauss_Jordan_Algorithms("GJ_input.txt")
    RUN.main()
except:
    f = open("GJ_output.txt", "w")
    f.write("Da co loi xay ra!")
    f.close()


print("---------------------- The End -------------------------")



#import 


from sympy import *
import matplotlib.pyplot as plt
from numpy import linspace
import numpy
from sympy.codegen.cfunctions import log10

#input
#x0 = input("giá trị đầu x(t_0) = ")
#f = 


#symbol:
t = symbols('t')
tVals = linspace(-0.5,0.5,100)


#example 1: x' = x^2 + t^2
x = 0
for i in range(5):
    xn=x
    x = integrate(x*x + t*t,t)

    print("x = ")
    print(expand(x))

    difference = log10(abs(xn-x))
    # xLambda=lambdify(t,x*1000,"numpy")
    # xnLambda=lambdify(t,xn*1000,"numpy")
    func = lambdify(t,difference,"numpy")
    plt.plot(tVals,func(tVals))

    
    plt.show()
plt.show()
    


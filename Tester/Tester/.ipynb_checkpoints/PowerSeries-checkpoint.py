#region
import matplotlib.pyplot as plt
import math

from sympy import *
import matplotlib.pyplot as plt
from numpy import linspace
import numpy as np
t = symbols('t')
f = symbols('f', cls=Function)
#endregion
#read input
#region
def ReadArray(f):
    line = f.readline()
    result = list(map(lambda x: float(N(x)), line.split()))
    return result

def ReadMatrix(f):
    listCoef = []
    line = f.readline()
    while(line.strip() != ''):
        coef = list(map(lambda x: float(N(x)), line.split()))
        listCoef.append(coef)
        line = f.readline()
    #print('listCoef: ')
    #print(listCoef)
    return listCoef

def RandN(listCoef):
        # R & N
    R = listCoef[0][0]
    N = math.inf
    for coef in listCoef:
        if(R > coef[0]): R = coef[0]
        coef.pop(0)
        if(N > len(coef)): N = len(coef)
    if R <= 0:
        raise ValueError("invalid input: bán kính <= 0")

    return (R,N)

#endregion
def calculate(initial, listCoef, N):
    result = initial              # mảng kết quả c_i
    k=len(listCoef)-1             # mảng mảng hệ số a_i và f
    for n in range(0,N-k):
        c=0
        offset = 1;
        for i in range(n+1,n+k+1): offset *= i
        #start calculating c_{n+k}
        for m in range(0,n+1):
            mult = 1
            for i in range(0,k):
                c += listCoef[i][n-m] * result[m+i] * mult
                mult *= m+i+1
        c= (listCoef[k][n]-c)/offset           # -1*n! / (n+k)!
        result.append(c)
    return result

#Program
def Polynomial(inputPath):
    f = open(inputPath,"r")
    initial = ReadArray(f)
    listCoef = ReadMatrix(f)
    f.close()
    R,N = RandN(listCoef)
    result = calculate(initial, listCoef, N)
    return (R, result)
def Restore(array):
    3
    
#region
def Save(result, outputPath, mode):
    f = open(outputPath, mode)
    f.write("Radius of convergence = " + str(result[0]) + ", Result: \n");
    f.write(str(result[1]))
    f.close()

def Plotf(f, interval):
    t_vals = linspace(interval[0], interval[1], 1000)
    lam_x = lambdify(t, f, modules = ['numpy'])
    x_vals = lam_x(t_vals)
    plt.plot(t_vals, x_vals)
    
def Plot(result, start, end, g = None):
    f = 0
    power = 0
    for i in result:
        f += i * (t ** power)
        power += 1
    Plotf(f, (start, end))
    if g is not None:
        Plotf(g, (start, end))
    return f
#endregion
#source
#region

#import
#region
import math
from sympy import *
import matplotlib.pyplot as plt
from numpy import linspace
import numpy as np
from sympy.codegen.cfunctions import log10
from sympy.abc import x,t,y
from collections import OrderedDict
from operator import itemgetter, attrgetter
from sympy.plotting import plot
#endregion


#mode
#region
symbolicMode = "symbolic"
numericMode = "numeric"
autoMode = "auto"
#endregion


#symbol declaration
#region
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)
#endregion


#input, output
#region
inputPath_1 = "symbol1.txt"

outputPath_1 = "output1.txt"
def ReadInput(file):
    f = file.readline()
    (lowT, upT) = map(float, file.readline().split(","))
    (lowX, upX) = map(float, file.readline().split(","))
    (t0, x0) = map(float, file.readline().split(","))
    epsilon = N(file.readline())
    return (f, lowT, upT, lowX, upX, t0, x0, epsilon)

def StringToArrayFunction(string_Array):
    f = list(map(lambda s: s.split(":"), string_Array.split(",")))
    f = list(map(lambda arr:
             (float(arr[0].strip()), float(arr[1].strip()))
             , f))
    f = sorted(f, key = lambda x: x[0])
    return f
#endregion


#geting M,L,H,T,N, ...
#region
def GetM(f, lowT, upT, lowX, upX):
    #not implemented
    return 100
def GetL(f, lowT, upT, lowX, upX):
    #not implemented
    return 100
def MaxDerivative(arr):
    n = f.length()
    if(n>1):
        L = f[1] - f[0]
    else:
        raise ValueError("array too small !")
    for i in range(n):
        delta = f[i+1] - f[i]
        if(delta > L):
            L = delta
    return L

def HandT(deltaX, M, L):
    deltaT = min(deltaX / M, 1 / (2 * L))
    h = deltaT * L
    return (h,deltaT)

def GetN(h,epsilon, deltaX):
    N = ceil(log(h, epsilon / delta)) + 1
    return N

def GetStuff(f, lowX, upX, lowT, upT, epsilon):
        M = GetM(x, lowT, upT, lowX, upX)
        L = GetL(x, lowT, upT, lowX, upX)
        deltaX = upX - lowX
        (h, deltaT) = HandT(deltaX, M, L)
        N = math.ceil(log(h,epsilon / deltaX)) + 1

        try:
            return (M,L,deltaX,h,deltaT,N)
        except:
            raise NotImplementedError()

def MakeArrayFunction(f):

    return
#endregion


#main loop (integrate)
#region

def NumericIntegrate(f, xn, x0, segmentLength, N):
    n = (int) (len(xn)/2)
    for j in range(N):
        integral = 0
        for i in range(n, 0, -1):
            integral = integral - segmentLength/2 * (f.subs([(t, xn[i][0]), (x, xn[i][1])]) 
                                                 + f.subs([(t, xn[i-1][0]), (x, xn[i-1][1])]))
            xn[i-1][1] = x0 + integral

        integral = 0
        for i in range(n, 2*n):
            integral = integral + segmentLength/2 * (f.subs([(t, xn[i][0]), (x, xn[i][1])]) 
                                                + f.subs([(t, xn[i+1][0]), (x, xn[i+1][1])]))
            xn[i+1][1] = x0 + integral

    return xn

def NumericIntegrate2(f, xn, x0, segmentLength, N):
    n = (int) (len(xn)/2)
    xn2 = []
    for num in xn:
        xn2.append([num[0],num[1]])

    for j in range(N):

        integral = 0
        for i in range(n, 0, -1):
            integral = integral - segmentLength/2 * (f.subs([(t, xn[i][0]), (x, xn[i][1])]) 
                                                 + f.subs([(t, xn[i-1][0]), (x, xn[i-1][1])]))
            xn2[i-1][1] = x0 + integral
            PlotPairs(xn2)

        integral = 0
        for i in range(n, 2*n):
            integral = integral + segmentLength/2 * (f.subs([(t, xn[i][0]), (x, xn[i][1])]) 
                                                + f.subs([(t, xn[i+1][0]), (x, xn[i+1][1])]))
            xn2[i+1][1] = x0 + integral
        xn =[]
        for num in xn2:
            xn.append([num[0],num[1]])

    return xn

def Trapezoid(f, firstIndex, lastIndex):
    f = f[firstIndex:lastIndex+1]
    return (
        sum(f) - f[0]/2 - f[f.length() - 1]/2
        ) / varRange
        

def SymbolicIntegrate(f, t0, x0, N):
     xn = x0
     for i in range(0,N):
        xn = x0 + integrate(f.replace(x,xn), (t,t0,t))
     return xn


#endregion


#plot
#region

def PlotPairs(pairList):
    t,x = zip(*pairList)
    plt.scatter(t,x)
    plt.show()

def PlotSymbol(symbolOutput):
    func, interval = symbolOutput
    #t = linspace(interval[0], interval[1], 1000)
    #func = t**3/3 + t**7/67
    plot((func, (t, interval[0], interval[1])))
    
def PlotBoth(symbolOutput, pairList):
    t1, x1 = zip(*pairList)
    plt.scatter(t1,x1)

    #Why(symbolOutput)
    func, interval = symbolOutput
    t_vals = linspace(interval[0], interval[1], 1000)
    lam_x = lambdify(t, func, modules=['numpy'])
    x_vals = lam_x(t_vals)
    plt.plot(t_vals, x_vals)

    plt.show()
#endregion


#Program
#region

def Pica(filename):
    file = open(filename, "r")
    (f, lowT, upT, lowX, upX, t0, x0, epsilon) = ReadInput(file)
    try:
        f = sympify(f)
    except:
        raise ValueError("invalid Pica input (symbolic)")
    file.close()
    (M,L,deltaX,h,deltaT,N) = GetStuff(f, lowT, upT, lowX, upX, epsilon)
    
    xn = SymbolicIntegrate(f, t0, x0, N)

    return (xn, (t0-deltaT, t0 + deltaT))

def Pica1(filename, length):
    file = open(filename, "r")
    (f, lowT, upT, lowX, upX, t0, x0, epsilon) = ReadInput(file)
    try:
        f = sympify(f)
    except:
        raise ValueError("invalid Pica input (symbolic)")
    file.close()
    (M,L,deltaX,h,deltaT,N) = GetStuff(f, lowT, upT, lowX, upX, epsilon)
    xn = []
    segmentLength = 2*deltaT/length
    n = (int) (length/2)
    for i in range(-n, n+1):
        xn.append([t0 + i*segmentLength, x0])

    xn = NumericIntegrate(f, xn, x0, segmentLength, N)

    return xn

# test
#region
def ReadPair(file):
    f = "99:1, 2: 3.3, 5: 44,  3: 3.6"
    f = list(map(lambda s: s.split(":"), f.split(",")))
    f = list(map(lambda arr:
                 (float(arr[0].strip()), float(arr[1].strip()))
                 , f))
    f = sorted(f, key = lambda x: x[0])
    print(f)

#endregion

#endregion

#main
#region

#guideline:
#region
# This code use sympy and numpy (see import), make sure to install them before using this code

# There are 2 function
# pica for symbolic: Pica(string filename)                  #name of input file
# pica for numeric: Pica1(string filename, int length)      #length of output array
# input example:
#t^2+x^2    #function f
#-10,10     #range of t
#-10,10     #range of x
#0,0        #t0 and x0 = x(t0)
#10^-10     #epsilon

# symbolic result: (t**7/63 + t**3/3, (-0.005, 0.005))
# numeric result: [[-0.004838709677419355, -3.78470007730525e-8], [-0.004516129032258065, -3.07811083890629e-8], ...]
#endregion

#example:
filename = inputPath_1

result = Pica(filename)                 #symbolic

length = 31 # length of output array
result1 = Pica1(filename, length)       #numeric

#plot result:

#PlotSymbol(result)
#PlotPairs(result1)
#PlotBoth(result, result1)

print("ended")

#endregion
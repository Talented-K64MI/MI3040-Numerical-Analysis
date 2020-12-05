
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
inputPath_1 = "input1.txt"

outputPath_1 = "output1.txt"

def ReadInput(file):
    f = file.readline()
    (lowT, upT) = map(lambda s: N(s), file.readline().split(","))
    (lowX, upX) = map(lambda s: N(s), file.readline().split(","))
    (t0, x0) = map(lambda s: N(s), file.readline().split(","))
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
    if(n > 1):
        L = f[1] - f[0]
    else:
        raise ValueError("array too small !")
    for i in range(n):
        delta = f[i + 1] - f[i]
        if(delta > L):
            L = delta
    return L

def GetN(M, L , deltaX, epsilon):
    deltaT = min(deltaX / M, 1 / (2 * L))
    h = deltaT * L
    N = 1
    error = M * deltaT
    while error > epsilon:
        N+=1
        error = error * h / N
    return deltaT, N

def GetStuff(f, lowX, upX, lowT, upT, epsilon):
        M = GetM(x, lowT, upT, lowX, upX)
        L = GetL(x, lowT, upT, lowX, upX)
        deltaX = upX - lowX
        deltaT, N = GetN(M, L, deltaX, epsilon)

        try:
            return (M,L,deltaX,h,deltaT,N)
        except:
            raise NotImplementedError()

def MakeArrayFunction(f):

    return
#endregion


#main loop (integrate)
#region
def NumericIntegrate(f, xn, x0, segmentLength, epsilon):
    n = (int) (len(xn)/2)
    segmentLength /=2
    maxError = -1
    loop = 0
    while abs(maxError) > epsilon:
        loop += 1
        maxError = -1

        integral = 0
        for i in range(n, 0, -1):
            integral = integral - segmentLength * (f.subs([(t, xn[i][0]), (x, xn[i][1])]) + f.subs([(t, xn[i - 1][0]), (x, xn[i - 1][1])]))
            newValue = x0 + integral
            error = abs(xn[i - 1][1] - newValue)
            xn[i - 1][1] = newValue
            if(error > maxError): maxError = error

        integral = 0
        for i in range(n, 2 * n):
            integral = integral + segmentLength * (f.subs([(t, xn[i][0]), (x, xn[i][1])]) + f.subs([(t, xn[i + 1][0]), (x, xn[i + 1][1])]))
            newValue = x0 + integral
            error = abs(xn[i + 1][1] - newValue)
            xn[i + 1][1] = x0 + integral
            if(error > maxError): maxError = error

    return xn

def Trapezoid(f, firstIndex, lastIndex):
    f = f[firstIndex:lastIndex + 1]
    return (sum(f) - f[0] / 2 - f[f.length() - 1] / 2) / varRange
        

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

    t1 = float(t0-deltaT)
    t2 = float(t0+deltaT)
    return (xn, (t1,t2))

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
    segmentLength = 2 * deltaT / length
    n = (int)(length / 2)
    for i in range(-n, n + 1):
        xn.append([t0 + i * segmentLength, x0])

    xn = NumericIntegrate(f, xn, x0, segmentLength, epsilon)

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
# This code use sympy and numpy (see import), make sure to install them before
# using this code

# There are 2 function
# pica for symbolic: Pica(string filename) #name of input file
# pica for numeric: Pica1(string filename, int length) #length of output array
# input example:
#t^2+x^2 #function f
#-10,10 #range of t
#-10,10 #range of x
#0,0 #t0 and x0 = x(t0)
#10^-10 #epsilon

# symbolic result: (t**7/63 + t**3/3, (-0.005, 0.005))
# numeric result: [[-0.004838709677419355, -3.78470007730525e-8],
# [-0.004516129032258065, -3.07811083890629e-8], ...]
#endregion

#example:
#inputPath_1 = "input1.txt"
#inputPath_2 = "input2.txt"
#inputPath_3 = "input3.txt"
#inputPath_4 = "input4.txt"      # dont symbol this
#
#filename = inputPath_3
#result = Pica(filename)                 #symbolic
#length = 31 # length of output array
#result1 = Pica1(filename, length)      #numeric
#print(result)
#
##plot result:
#
#PlotBoth(result, result1)

##PlotSymbol()
##PlotPairs(result1)

#print("ended")

#endregion

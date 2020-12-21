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
from sympy.plotting import plot
#endregion

#symbol declaration
#region
x, t = symbols('x t')
f = symbols('f', cls=Function)
#endregion

#input, output
#region
def ReadInput(file):
    f = file.readline()
    (lowT, upT) = map(lambda s: N(s), file.readline().split(","))
    (lowX, upX) = map(lambda s: N(s), file.readline().split(","))
    (t0, x0) = map(lambda s: N(s), file.readline().split(","))
    epsilon = N(file.readline())
    return (f, lowT, upT, lowX, upX, t0, x0, epsilon)
#endregion

#Main Program
#region
def Pica1(f, deltaT, deltaX, t0, x0, M, L, epsilon, mode = ""):
    
    N = GetN(M, L, deltaT, deltaX, epsilon)
    xn = SymbolicIntegrate(f, t0, x0, N, mode)

    return xn

def Pica2(f, deltaT, t0, x0, M, L, epsilon, length = 69, mode = ""):
    
    xn = []
    segmentLength = 2 * deltaT / length
    n = (int)(length / 2)
    for i in range(-n, n + 1):
        xn.append([t0 + i * segmentLength, x0])

    xn = NumericIntegrate(f, xn, x0, segmentLength, epsilon, mode)

    return xn

def Pica(filename, length = None, M = None, L = None, deltaT = None, mode = ""):
    try:
        file = open(filename, "r")
        (f, lowT, upT, lowX, upX, t0, x0, epsilon) = ReadInput(file)
        f = sympify(f)
    except:
        raise ValueError("invalid Pica input")
    file.close()
    
    if not lowX< x0 <upX or not lowT< t0< upT:
        raise ValueError("invalid Pica input")
        
    if M is None:
        M = GetM(x, lowT, upT, lowX, upX)
    else:
        if M <= 0:
            raise ValueError("invalid Pica input")
        
        
    if L is None:
        L = GetL(x, lowT, upT, lowX, upX)
    else:
        if L < 0:
            raise ValueError("invalid Pica input")
    if L == 0:
        SymbolicIntergrate(f, t0, x0, 1, mode)
        
    deltaX = min(x0 - lowX, upX - x0)
    if deltaT is None:
        deltaT = min(deltaX / M, 1 / (2 * L), t0 - lowT, upT - t0)
    interval = (float(t0-deltaT), float(t0+deltaT))
    if length is None:
        return (Pica1(f, deltaT, deltaX, t0, x0, M, L, epsilon, mode), interval)
    return Pica2(f, deltaT, t0, x0, M, L, epsilon, length, mode)

#endregion

#Main loops
#region
def NumericIntegrate(f, xn, x0, segmentLength, epsilon, mode = ""):
    n = (int) (len(xn)/2)
    segmentLength /=2
    maxError = -math.inf
    loop = 0
    while abs(maxError) > epsilon:
        if mode == "test":
            dx = []
        loop += 1
        maxError = -math.inf
        
        integral = 0
        for i in range(n, 0, -1):
            integral = integral - segmentLength * (f.subs([(t, xn[i][0]), (x, xn[i][1])]) + f.subs([(t, xn[i - 1][0]), (x, xn[i - 1][1])]))
            newValue = x0 + integral
            error = abs(xn[i - 1][1] - newValue)
            xn[i - 1][1] = newValue
            if(error > maxError): maxError = error
            if mode == 'test':
                dx.append((xn[i][0], error))

        integral = 0
        for i in range(n, 2 * n):
            integral = integral + segmentLength * (f.subs([(t, xn[i][0]), (x, xn[i][1])]) + f.subs([(t, xn[i + 1][0]), (x, xn[i + 1][1])]))
            newValue = x0 + integral
            error = abs(xn[i + 1][1] - newValue)
            xn[i + 1][1] = x0 + integral
            if(error > maxError): maxError = error
            if mode == 'test':
                dx.append((xn[i][0], error))
                
        if mode == "test":
            print("Lặp lần ", loop, " với max error = ", maxError)
            PlotPairs(dx)
            plt.show()
    return xn

def GetN(M, L, deltaT, deltaX, epsilon, mode = ""):
    h = deltaT * L
    N = 1
    error = M * deltaT
    while error > epsilon:
        N+=1
        error = error * h / N
    return N

def SymbolicIntegrate(f, t0, x0, N, mode = ''):
     xn = x0
     for i in range(0,N):
        if mode == 'test':
            print(xn.evalf(2))
        xn = x0 + integrate(f.replace(x,xn), (t,t0,t))
     return xn

#endregion

# sup
#region
def GetM(f, lowT, upT, lowX, upX):
    #not implemented
    return 10
def GetL(f, lowT, upT, lowX, upX):
    #not implemented
    return 10

#endregion

#plot
#region
def PlotPairs(pairList):
    t,x = zip(*pairList)
    plt.scatter(t,x)

def PlotSymbol(symbolOutput):
    func, interval = symbolOutput
    #t = linspace(interval[0], interval[1], 1000)
    #func = t**3/3 + t**7/67
    plot((func, (t, interval[0], interval[1])))
    
def PlotBoth(symbolOutput, pairList):
    t1, x1 = zip(*pairList)
    plt.scatter(t1,x1)
    func, interval = symbolOutput
    t_vals = linspace(interval[0], interval[1], 1000)
    lam_x = lambdify(t, func, modules=['numpy'])
    x_vals = lam_x(t_vals)
    plt.plot(t_vals, x_vals)

def Plot(f, interval):
    t_vals = linspace(interval[0], interval[1], 1000)
    lam_x = lambdify(t, f, modules = ['numpy'])
    x_vals = lam_x(t_vals)
    plt.plot(t_vals, x_vals)
    #plt.show()
#endregion


#guideline:
#region
# This code use sympy and numpy (see import), make sure to install them before
# using this code

# Main function
# Pica(filename) with optional input: length for numeric approximation; M and L.
#
# input file example:
#t*(3-2*x)  #function f
#-0.5,0.5   #range of t
#-1,2       #range of x
#0,1        #t0 and x0 = x(t0)
#10**-8     #epsilon

# symbolic result example: (t**7/63 + t**3/3, (-0.005, 0.005))
# numeric result example: [[-0.004838709677419355, -3.78470007730525e-8],
# [-0.004516129032258065, -3.07811083890629e-8], ...]
#endregion

#example:
#inputPath_1 = "input1.txt"
#inputPath_2 = "input2.txt"
#inputPath_3 = "input3.txt"
#inputPath_4 = "input4.txt"      # cant use symbolic approximation

# usage example:
#filename = "input2.txt"
#
#result = Pica(filename, M = 2.5, L = 1)
#result1 = Pica(filename, M = 2.5, L = 1, length = 31)
#
#print(result)
#PlotBoth(result, result1)
#plt.show()
from sympy import *
import numpy as np
import math

cotezCoefs = [[1/2,     1/2],
             [1/6,      4/6,        1/6],
             [1/8,      3/8,        3/8,        1/8],
             [7/90,     32/90,      12/90,      32/90,      7/90],
             [19/288,   75/288,     50/288,     50/288,     75/288,19/288]]

#h^n - error term
convergeSpeeds = [2, 4, 4, 6, 6]

multiplier = [12, 90, 80/3, 945/8]

def CotezCoef(n):
    return cotezCoefs[n-1]
# M is sup(|f^(k)|) where f^(k) is the k-derivative of f, n is the degree of polynomial used
# k is the converge speed
# n < 5 pls ...
def Integral(f, M, rangeX, epsilon, n = 2):
    cotezCoef = CotezCoef(n)
    speed = convergeSpeeds[n]
    mult = multiplier[n-1]

    a,b = rangeX
    length = b-a

    #M/multiplier * length * h^k < eps
    h = math.pow(epsilon*mult/M/length, 1/speed)

    steps = (int) (length/h) + 1
    dx = length/steps/n

    integral = 0
    xn = a
    x = symbols('x')
    for step in range(steps):
        for t in range(n+1):
            integral += f.subs(x, xn)*cotezCoef[t]
            xn += dx
        xn -= dx
    
    return integral*dx*n

x = symbols('x')



############ WRITE YOUR FRICKING INPUT HERE ######################

f = 1/(x**2 + 1)
epsilon = 10**-12
M = 1000        # sup f^(n)

# khoảng tích phân
a = 0
b = 1

n = 4

############ WRITE YOUR FRICKING INPUT HERE ######################

############ PRINT IT OUT ...               ######################

integral = Integral(f, M, (a,b), epsilon, n)  # YOUR RESULT HERE

pi = 4*integral.evalf(30)                       # 30 CHỮ SỐ

print("pi = ", pi)

print("tích phân = ", integral.evalf(30))      # PRINT YOUR RESULT

############ PRINT IT OUT ...               ######################
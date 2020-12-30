#!/usr/bin/env python
# coding: utf-8

# # Newton interpolation polynomial

# ## Import library

import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from sympy import init_printing
init_printing()

# Nhap input
def inputData():
    x = []
    y = []
    with open('Newton.txt','r+') as f:
            for line in f.readlines():
                xt = float(line.split(' ')[0])
                yt = float(line.split(' ')[1])
                check = True
                for x_check in x:
                    if x_check == xt:
                        check = False
                        break
                if check:
                    x.append(xt)
                    y.append(yt)
    return x, y, len(x)-1

# Dung bang ty hieu
def buildBTH(x, y, n):
    ## Khoi tao
    BTH = np.zeros([n+1, n+1])
    ## Gan cot dau
    for i in range(n+1):
        BTH[i, 0] = y[i]
    ## Xay dung ty hieu
    for j in range(1,n+1):
        for i in range(n+1-j):
            BTH[i, j] = (BTH[i+1, j-1] - BTH[i, j-1]) / (x[i+j] - x[i])
    return BTH


# Noi suy Newton tien
def nsNewtonTien(x, y, n):
    BTH = buildBTH(x, y, n)
    t = Symbol('t')
    f = BTH[0, 0]
    var = (t - x[0])
    for i in range(1,n+1):
        f += var * BTH[0, i]
        var = var * (t - x[i])
    return f


# Noi suy Newton lui
def nsNewtonLui(x, y, n):
##    f = Symbol('f')
    BTH = buildBTH(x, y, n)
    t = Symbol('t')
    f = BTH[n, 0]
    var = (t - x[n])
    for i in range(1,n+1):
        f += var * BTH[n-i, i]
        var = var * (t - x[n-i])
    return f


# Xap xi gia tri
def pickPoints(x, x0, num):
    if num > len(x):
        raise Exception('Moi nhap lai')
    else:
        hieu = [abs(x[i] - x0) for i in range(len(x))]
        index = [i[0] for i in sorted(enumerate(hieu), key=lambda t:t[1])]
        return index[:num]

def estimate(x, y, x0, deg):
    index = pickPoints(x, x0, deg+1)
    x1 = [x[i] for i in index]
    y1 = [y[i] for i in index]
    ## buildBTH
    BTH = buildBTH(x1, y1, deg)
    f = nsNewtonTien(x1, y1, deg)
    value = f.subs(Symbol('t'), x0)
    return f, value    

def main():
    x, y, n = inputData()
    x0 = float(input("Moi nhap gia tri can tinh: "))
    deg = int(input("Moi nhap bac da thuc (< bac lon nhat): "))
    f, v = estimate(x, y, x0, deg)
    print("Da thuc noi suy la: ", simplify(f))
    print("Gia tri can tinh tai ", x0, " la: ", v)
    ## plot
    xx = np.linspace(x[0], x[-1], 100)
    fx = [f.subs(Symbol('t'), xxx) for xxx in xx]

    plt.figure()
    plt.scatter(x, y, marker='*')
    plt.plot(xx, fx)
    plt.xlabel('Points')
    plt.ylabel('Values')
    plt.savefig("mygraph.png")

if __name__=='__main__':
    main()

import numpy as np
import matplotlib.pyplot as plt
import math

def feval(funcName, *args):
    return eval(funcName)(*args)


def RungeKutta4thOrder(func, yinit, xspan, h):
    m = len(yinit)
    n = int((xspan[-1] - xspan[0]) / h)

    x = xspan[0]
    y = yinit

    xsol = np.empty((0))
    xsol = np.append(xsol, x)

    ysol = np.empty((0))
    ysol = np.append(ysol, y)

    for i in range(n):
        k1 = feval(func, x, y)

        yp2 = y + k1*(h/2)

        k2 = feval(func, x+h/2, yp2)

        yp3 = y + k2*(h/2)

        k3 = feval(func, x+h/2, yp3)

        yp4 = y + k3*h

        k4 = feval(func, x+h, yp4)

        for j in range(m):
            y[j] = y[j] + (h/6)*(k1[j] + 2*k2[j] + 2*k3[j] + k4[j])

        x = x + h
        xsol = np.append(xsol, x)

        for r in range(len(y)):
            ysol = np.append(ysol, y[r]) 

    return [xsol, ysol]


def ABM4thOrder(func, yinit, xspan, h):

    m = len(yinit)

    dx = int((xspan[-1] - xspan[0]) / h)

    xrk = [xspan[0] + k * h for k in range(dx + 1)]

    [xx, yy] = RungeKutta4thOrder(func, yinit, (xrk[0], xrk[3]), h)

    x = xx
    xsol = np.empty(0)
    xsol = np.append(xsol, x)

    y = yy
    yn = np.array([yy[0]])
    ysol = np.empty(0)
    ysol = np.append(ysol, y)

    for i in range(3, dx):
        x00 = x[i]; x11 = x[i-1]; x22 = x[i-2]; x33 = x[i-3]; xpp = x[i]+h

        y00 = np.array([y[i]])
        y11 = np.array([y[i - 1]])
        y22 = np.array([y[i - 2]])
        y33 = np.array([y[i - 3]])

        y0prime = feval(func, x00, y00)
        y1prime = feval(func, x11, y11)
        y2prime = feval(func, x22, y22)
        y3prime = feval(func, x33, y33)

        ypredictor = y00 + (h/24)*(55*y0prime - 59*y1prime + 37*y2prime - 9*y3prime)
        ypp = feval(func, xpp, ypredictor)

        for j in range(m):
            yn[j] = y00[j] + (h/24)*(9*ypp[j] + 19*y0prime[j] - 5*y1prime[j] + y2prime[j])

        xs = x[i] + h
        xsol = np.append(xsol, xs)

        x = xsol

        for r in range(len(yn)):
            ysol = np.append(ysol, yn)

        y = ysol

    return [xsol, ysol]

#############################   INPUT GOES HERE


def myFunc(x, y):
    return math.e**(-2*x)-2*y


h = 0.2

x0 = 0
xn = 2

y0 = 0.1


#############################   \INPUT GOES HERE

xspan = np.array([x0, xn])
yinit = np.array([y0])

[ts, ys] = ABM4thOrder('myFunc', yinit, xspan, h)


dt = int((xspan[-1]-xspan[0])/h)
t = [xspan[0]+i*h for i in range(dt+1)]

#############################   PRINT RESULT

for i in range(len(ts)):
    print("x = ", ts[i], ";             y = ", ys[i])

#############################   \PRINT RESULT


plt.plot(ts, ys, 'r')
plt.xlim(xspan[0], xspan[1])

plt.tight_layout()
plt.show()

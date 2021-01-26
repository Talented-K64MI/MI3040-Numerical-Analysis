
import matplotlib.pyplot as plt
import numpy as np


def feval(funcName, *args):
    return eval(funcName)(*args)


def RK4thOrder(func, yinit, x_range, h):
    m = len(yinit)
    n = int((x_range[-1] - x_range[0]) / h)
    
    x = x_range[0]
    y = yinit
    
    # Containers for solutions
    xsol = np.empty(0)
    xsol = np.append(xsol, x)

    ysol = np.empty(0)
    ysol = np.append(ysol, y)

    for i in range(n):
        k1 = feval(func, x, y)

        yp2 = y + k1 * (h / 2)

        k2 = feval(func, x + h / 2, yp2)

        yp3 = y + k2 * (h / 2)

        k3 = feval(func, x + h / 2, yp3)

        yp4 = y + k3 * h

        k4 = feval(func, x + h, yp4)

        for j in range(m):
            y[j] = y[j] + (h / 6) * (k1[j] + 2 * k2[j] + 2 * k3[j] + k4[j])

        x = x + h
        xsol = np.append(xsol, x)

        for r in range(len(y)):
            ysol = np.append(ysol, y[r])  

    return [xsol, ysol]

#########################       INPUT GOES HERE

def myFunc(x, y):
    dy = np.zeros((len(y)))

    n = y[0]
    p = y[1]
    K = 100
    r = 0.6
    a = 0.04
    muy = 1.2

    dy[0] = r * n * (1 - n / K) - a * n * p
    dy[1] = -muy * p + a * n * p
    return dy


h = 0.01
t0 = 0.0
tn = 100

y01 = 70.0
y02 = 20.0


##########################       \INPUT GOES HERE


x = np.array([t0, tn])
yinit = np.array([y01, y02])

[ts, ys] = RK4thOrder('myFunc', yinit, x, h)

node = len(yinit)
ys1 = ys[0::node]
ys2 = ys[1::node]

##########################       PRINT RESULT

for i in range(len(ts)):
    print("t = ", ts[i])
    print("y1 = ", ys1[i], ";   y2 = ", ys2[i])

##########################       \PRINT RESULT


##########################       Plot y1, y2 with respect to t

plt.plot(ts, ys1, 'r')
plt.plot(ts, ys2, 'b')
plt.xlim(x[0], x[1])
plt.legend(["y(1)", "y(2)"], loc=2)
plt.xlabel('x', fontsize=17)
plt.ylabel('y', fontsize=17)
plt.tight_layout()
plt.show()

##########################       \Plot y1, y2 with respect to t

##########################       plot y1 - y2 as x - y

plt.plot(ys1, ys2, 'r')
plt.xlabel('con mồi', fontsize=17)
plt.ylabel('thú săn mồi', fontsize=17)
plt.show()

##########################       \plot y1 - y2


# Uncomment the following to print the figure:
#plt.savefig('Fig_ex7_RK4th.png', dpi=600)


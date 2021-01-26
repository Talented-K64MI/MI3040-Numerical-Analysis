
import matplotlib.pyplot as plt
import numpy as np
import math

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

def myFunc(t, vectorY):
    df = np.zeros((len(vectorY)))

    y = vectorY[0]
    z = vectorY[1]

#########################       INPUT GOES HERE

    # y' = z
    df[0] = z
    # z' = ty^2(1+sin(t)y) + yt^3
    df[1] = t*y**2*(1+math.sin(t)*y) + t**3*y
    return df

h = 0.01    # độ dài 1 bước
t0 = 0      # điểm bắt đầu
tn = 1      # điểm kết thúc

y0 = 1      # giá trị đầu y(t0)
z0 = 1      # giá trị đầu z(t0)

# this work with more than 2 equation ...

##########################       \INPUT GOES HERE

y0 = float(y0)
z0 = float(z0)

x = np.array([t0, tn])
yinit = np.array([y0, z0])

[ts, ys] = RK4thOrder('myFunc', yinit, x, h)

node = len(yinit)
ys1 = ys[0::node]
ys2 = ys[1::node]

##########################       PRINT RESULT

for i in range(len(ts)):
    print("t = ", ts[i])
    print("y1 = ", ys1[i], ";   y2 = ", ys2[i])

##########################       \PRINT RESULT


##########################       Plot y, z with respect to t  ( but currently only y, uncomment plt.plot... below to plot z )

plt.plot(ts, ys1, 'r')
#plt.plot(ts, ys2, 'b')
plt.xlim(x[0], x[1])
plt.legend(["y(1)", "y(2)"], loc=2)
plt.xlabel('x', fontsize=17)
plt.ylabel('y', fontsize=17)
plt.tight_layout()
plt.show()

##########################       \Plot y, z with respect to t

##########################       plot y - z as x - y(x)

plt.plot(ys1, ys2, 'r')
plt.xlabel('con mồi', fontsize=17)
plt.ylabel('thú săn mồi', fontsize=17)
plt.show()

##########################       \plot y1 - y2


# Uncomment the following to print the figure:
#plt.savefig('Fig_ex7_RK4th.png', dpi=600)


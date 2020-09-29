
#import math            # by anh Tài đz :D #
def bisection(a, b, esp, f):
    while (True):
        if f(a) < 0:
            t = -1
        else:
            t = 1
        c = (a + b) / 2
        z = f(c)
        if z == 0:
            return c
            break
        else:
            if (z * t) < 0:
                b = c
            else:
                a = c
        if abs(b - a) < esp:
            return c
            break
#f = lambda x: x**2 - 15
#print(halfing(2,5,0.01,f))
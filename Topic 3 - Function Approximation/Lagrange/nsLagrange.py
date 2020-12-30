import numpy as np
import matplotlib.pyplot as plt

def hoocneNhan(A,xk):
    A.append(1)
    for i in range(len(A)-2,0,-1):
        A[i] = A[i - 1] - A[i] * xk
    A[0] = - A[0] * xk
    return A

def hoocneChia(A,xk):
    B = np.ones(len(A) - 1)
    for i in range(len(B) - 2,-1,-1):
        B[i] = A[i + 1] + B[i + 1] * xk
    return B

def init():
    global x,y,n
    x = []
    y = []
    with open('nsLagrange.txt','r+') as f:
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
                plt.scatter(xt,yt)
    x = np.asarray(x)
    y = np.asarray(y)
    n = len(x)

def PolyCoefficients(xt, coeffs):
    """ Returns a polynomial for ``x`` values for the ``coeffs`` provided.

    The coefficients must be in ascending order (``x**0`` to ``x**o``).
    """
    o = len(coeffs)
    yt = 0
    for i in range(o):
        yt += coeffs[i] * xt ** i
    return yt


def main():
    init()

    # tinh D
    D = []
    for i in range(n):
        D.append(1)
        for j in range(n):
            if(i != j):
                D[i] *= (x[i] - x[j])
    D = np.asarray(D)
    
    # tinh w
    w = [1]
    for i in range(n):
        w = hoocneNhan(w,x[i])
    w = np.asarray(w)

    # tinh wi
    wi = []
    for i in range(n):
        wi.append(hoocneChia(w,x[i]))
    wi = np.asarray(wi)

    # tinh px
    px = np.zeros(n)
    for i in range(n):
        for j in range(n):
            px[i] += wi[j,i] * y[j] / D[j]

    print(px)
    
    plt.scatter(x,y)
    
    xt = np.linspace(x[0]-0.5,x[n - 1] + 0.5,1000)
    plt.plot(xt,PolyCoefficients(xt,px))
    plt.savefig("mygraph.png")

    #plt.show()

if __name__=='__main__':
    main()
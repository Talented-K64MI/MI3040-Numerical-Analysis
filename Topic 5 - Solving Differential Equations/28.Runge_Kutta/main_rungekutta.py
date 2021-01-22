from sympy import *
from math import *
import sys


from lib_rungekutta import *

uu = rungekutta_oop("y - x*x + 1", 0, 0.5, 0.01, 10, 4);
g = (uu.Solve());

for x in g: print(x);


import matplotlib.pyplot as plt
def PlotPairs(pairList):
    t,x = zip(*pairList)
    plt.scatter(t,x)
    plt.show()


PlotPairs(g)

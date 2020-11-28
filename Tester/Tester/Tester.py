import bisection
uu = bisection.bisection_oop(1, 5, 0.01, "x**2-2");
print(uu.Solve());

print("---------------------- The End -------------------------")

from newton_ralphson import *
expr = "x^3 + x^2 - x + 1";
L = -3; R = -1; eps = 1e-12;
uu = newton_oop(L, R, eps, expr);
print(f"Nghiệm của phương trình {expr} trên khoảng [{L}, {R}] là: {uu.Solve()}");

print("---------------------- The End -------------------------")

#import Bordering
#
# cant import without input file

print("---------------------- The End -------------------------")

#import Cholesky
# 
# 4 methods for 1 task ?!
# im not gonna input each position on the matrix

print("---------------------- The End -------------------------")

#import GaussJordan_final
# this code is connected to a hard-defined global var
# in the end, i only use the function, which should connect to my input, not your global var


#import Cholevsky

# it's literally a function
# so dont put code outside function -_-


#import 


from sympy import *
from math import *
import sys
from lib_newton_ralphson import *

expr = input("Nhập hàm f(x) trong phương trình f(x) = 0: ");
a    = float(input("Nhập a trong khoảng cách ly nghiệm [a, b]: "));
b    = float(input("Nhập b trong khoảng cách ly nghiệm [a, b]: "));
eps  = float(input("Nhập sai số epsilon: "));

uu = newton_oop(a, b, eps, expr);
sol = uu.Solve();

print(f"Nghiệm của phương trình {expr} = 0 trên khoảng [{a}, {b}] với sai số {eps} là x = {sol}");
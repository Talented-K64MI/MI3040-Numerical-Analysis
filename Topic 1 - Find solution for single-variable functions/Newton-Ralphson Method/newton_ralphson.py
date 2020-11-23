#===================================================================================
#
#   Code (đã cái tiến) cho PP Newton-Ralphson. 
#       * Input: f(x) trong pt f(x) = 0; khoảng cách li ban đầu (a, b); sai số epsilon
#       * Output: Nghiệm PT f(x) = 0;
#       * Hạn chế: Chưa có gói tìm khoảng cách ly nghiệm
#       * Cải tiến: Giảm khối lượng tính toán - tính f(a) 1 lần + thêm SymPy
#       
#===================================================================================
from sympy import *
from math import *
import sys


#===================================================================================
# Phần thuật toán chính
class newton_oop:
#{
    def __init__(self, a_0, b_0, eps, expr):
    #{
        x = symbols("x");
        func = sympify(expr);

        self.a_0 = a_0;
        self.b_0 = b_0;
        self.eps = eps;
        
        self.sym_df = [
            func, 
            diff(func, x), 
            diff(func, x, 2)
        ];
        self.df = [
            lambdify(x, self.sym_df[0], "math"),
            lambdify(x, self.sym_df[1], "math"),
            lambdify(x, self.sym_df[2], "math"),
        ];

        print(self.sym_df, file=sys.stderr);
    #}


    def __checkSign(self, sym_f, f):
    #{
        x = symbols("x");
        a = self.a_0;
        b = self.b_0;

        sol_set = solveset(diff(sym_f, x), x, Interval(a, b));
        if(f(b) > f(a)): val_max = f(b), val_min = f(a);
        else: val_max = f(a), val_min = f(b);

        if(sol_set != EmptySet and sol_set.is_iterable): 
            for args in sol_set:
            #{
                val_max = max(val_max, f(args));
                val_min = min(val_min, f(args));
            #}

        if(val_max * val_min >= 0): return val_min;
        return float("NaN");
    #}
    def checkInputValidity(self):
    #{
        L = self.a_0;
        R = self.b_0;

        # Corner case: f(L) = 0 or f(R) = 0
        if(self.f(L) == 0 or self.f(R) == 0): return 1;

        # Check if a < b
        if(L > R or (L == R and self.f(L) != 0)): return 0;

        # Check if f(a) * f(b) < 0
        if(self.f(L) * self.f(R) >= 0): return 0;

        # Check if [a, b] is "safe" to converge
        val1 = self.__checkSign(self.sym_df[1], self.df[1]);
        val2 = self.__checkSign(self.sym_df[2], self.df[2]);
        if(val1 == float("NaN") or val2 == float("NaN")): return 0;

        return 1;
    #}
    def __newtonMethod(self):
    #{
        print("foo");
    #}



    def Solve(self):
    #{
        if(self.__checkInputValidity() == 0):
        #{
            print("Invalid input. The program will now exit", file=sys.stderr);
            return float("NaN");
        #}
        return self.__newtonMethod();
    #}
#}


#===================================================================================
# Chương trình ví dụ
# input_expr = input('Please enter f(x) in f(x) = 0 equation: ');
# L   = float(input('Please enter the initial left bound a = '));
# R   = float(input('Please enter the initial right bound b = '));
# eps = float(input('Please enter the error value eps = '));
# uu = bisection_oop(L, R, eps, input_expr);
# print(uu.Solve());

uu = newton_oop(-300, 300, 1e-6, "x**3 - 24*x**2 + 5*x + 3000");
uu.checkInputValidity();
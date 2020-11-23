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

        # print(self.sym_df, file=sys.stderr);
    #}

    # Trị tuyệt đối và check dấu
    def __abs(self, x):
    #{
        return x if x >= 0 else -x;
    #}
    def __sign(self, x):
    #{
        if(x > 0): return 1;
        if(x < 0): return -1;
        return 0;
    #}


    # Tìm max/min của f
    def __findMaxMin(self, sym_f, f):
    #{
        x = symbols("x");
        a = self.a_0;
        b = self.b_0;

        val_max = val_min = f(a);
        sol_set = FiniteSet(a, b);
        sol_set = Union(sol_set, solveset(diff(sym_f, x), x, Interval(a, b)));

        if(sol_set.is_iterable): 
            for args in sol_set:
            #{
                val_max = max(val_max, f(args));
                val_min = min(val_min, f(args));
            #}
        
        return (
            val_min, 
            val_max, 
            self.__sign(val_min),
            self.__sign(val_max)
        );
    #}


    # Chốt 141
    def __checkInputValidity(self):
    #{
        a = self.a_0;
        b = self.b_0;
        f = self.df[0];

        # Corner case: f(a) = 0 or f(b) = 0
        if(f(a) == 0 or f(b) == 0): return 1;

        # Check if a < b
        if(a > b or (a == b and f(a) != 0)): 
        #{
            print("Khoảng [a, b] không hợp lệ 8==>");
            return 0;
        #}

        # Check if f(a) * f(b) < 0
        if(f(a) * sign(f(b)) >= 0): 
        #{
            print("Khoảng [a, b] không phải khoảng cách ly 8==>");
            return 0;
        #}

        # Check if [a, b] is "safe" to converge
        d1f_maxmin = self.__findMaxMin(self.sym_df[1], self.df[1]);
        d2f_maxmin = self.__findMaxMin(self.sym_df[2], self.df[2]);

        if(d2f_maxmin[2] * d2f_maxmin[3] < 0 or d1f_maxmin[2] * d1f_maxmin[3] <= 0): 
        #{
            print("PP Newton ko hội tụ được");
            return 0;
        #}


        # print(d1f_maxmin, file=sys.stderr);
        # print(d2f_maxmin, file=sys.stderr);

        # Assign auxiliary variables
        self.m1 = -d1f_maxmin[1] if (d1f_maxmin[0] < 0) else d1f_maxmin[0];
        self.M2 = -d2f_maxmin[0] if (d2f_maxmin[0] < 0) else d2f_maxmin[1];
        self.sign =  d2f_maxmin[2];
        return 1;
    #}



    def __newtonMethod(self):
    #{
        eps = self.eps;
        a = self.a_0;
        b = self.b_0;
        m1 = self.m1;
        
        f = self.df[0];
        d1f = self.df[1];
        x0 = a if (f(a) * self.sign > 0) else b;

        if(f(a) == 0): return a;
        if(f(b) == 0): return b;

        # print(x0, m1, self.sign, file=sys.stderr);

        while(self.__abs(f(x0)) > eps * m1):
        #{
            x0 = x0 - f(x0) / d1f(x0);
            # print(x0, file=sys.stderr);
        #}

        return x0;
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
# expr = "x^3 + x^2 - x + 1";
# L = -3;
# R = -1;
# eps = 1e-12;

# uu = newton_oop(L, R, eps, expr);
# print(f"Nghiệm của phương trình {expr} trên khoảng [{L}, {R}] là: {uu.Solve()}");
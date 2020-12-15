#===================================================================================
#
#   Code cho phương pháp Dây cung 
#       * Input: f(x) trong pt f(x) = 0; khoảng cách li ban đầu (a, b); sai số epsilon
#       * Output: Nghiệm PT f(x) = 0;
#       
#===================================================================================
from math import *
from sympy import *
import sys

#===================================================================================
# Phần thuật toán chính
class daycung_oop:
#{
    def __init__(self, a_0, b_0, eps, expr):
    #{
        x = symbols("x");
        self.func = sympify(expr);
        self.a_0 = a_0;
        self.b_0 = b_0;
        self.eps = eps;
        f=self.func
        self.sym_df = [
            f, 
            diff(f, x), 
            diff(f, x, 2)
        ];
        
        self.df = [
            lambdify(x, self.sym_df[0], "math"),
            lambdify(x, self.sym_df[1], "math"),
            lambdify(x, self.sym_df[2], "math"),
        ];
        # print(self.sym_df, file=sys.stderr);
    #}


    # Tìm max/min của f
    def __Kiem_tra_don_dieu(self):
    #{
        x = symbols("x");
        a = self.a_0;
        b = self.b_0;
        sol_set = solveset(diff(self.func, x ), x, Interval(a, b))
        sol_set = Union(sol_set, solveset(diff(self.func, x, 2), x, Interval(a, b)));
        sol_set = Union(sol_set, solveset(diff(self.func, x , 3), x, Interval(a, b)));
        if(sol_set.is_empty): 
            for i in sol_set:
                print(i)
            return 1
        else: 
            return 0m
    #}


    # Chốt 141
    def __checkInputValidity(self):
    #{
        a = self.a_0;
        b = self.b_0;
        f = self.df[0];
        
        # Check if f(a) * f(b) < 0
        if(f(a) * f(b) >= 0): 
        #{
            print(f(a)," ",f(b))
            print(f"Khoảng cách ly [{a}, {b}] không hợp lệ");
            return 0;
        #}

        if(self.__Kiem_tra_don_dieu()==0): 
        #{
            print("Khoảng đã cho không hợp lệ");
            return 0;
        #}
    #}



    def __Daycung(self):
    #{

        eps = self.eps
        a = self.a_0
        b = self.b_0
        
        f = self.df[0]
        f1 = self.df[1]
        f2 = self.df[2]

        if ((f1(a)>0 and f2(a)>0) or (f1(a)<0 and f2(a)<0)):
            d=b
            x=a
        else:
            d=a
            x=b
        x_pre=-1000

        while (x-x_pre > eps):
            x_pre=x
            x=x_pre - (d-x_pre)/(f(d)-f(x_pre))*f(x_pre)
        return x


    def Solve(self):
        if(self.__checkInputValidity() == 0):
            print("Vui lòng nhập lại dữ liệu", file=sys.stderr);
            exit(0)
        return self.__Daycung();


#===================================================================================
# Chương trình chính

expr = "sin(x)+cos(x)-0.5"
L = -1
R = 1
eps = 1e-6

uu = daycung_oop(L, R, eps, expr);
print(f"Nghiệm của phương trình {expr} trên khoảng [{L}, {R}] là: {uu.Solve()}");

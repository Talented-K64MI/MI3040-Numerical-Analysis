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
        if(sol_set.is_empty): 
            return 1
        else: 
            return 0
    #}

    # Chốt 141
    def __checkInputValidity(self):
    #{
        a = self.a_0;
        b = self.b_0;
        f = self.df[0];
        
        # Check if f(a) * f(b) < 0
        if (f(a)==0):
            print(f"Phương trình có nghiệm đúng x={a}")
            return 0;
        if (f(b)==0):
            print(f"Phương trình có nghiệm đúng x={b}")
            return 0;  
        if(f(a) * f(b) > 0): 
        #{
            print(f(a)," ",f(b))
            print("Khoảng cách ly không hợp lệ, không tồn tại nghiệm duy nhất");
            return 0;
        #}

        if(self.__Kiem_tra_don_dieu()==0): 
        #{
            print("Khoảng cách ly không hợp lệ, không thỏa mãn điều kiện hội tụ");
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
        Min=min(abs(f1(a)),abs(f1(b)))
        Max=max(abs(f1(a)),abs(f1(b)))
        xi=(Max-Min)/Min

        while (abs(x-x_pre)*xi> eps):
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

<<<<<<< HEAD
expr = "x^3-1"
L = -1
R = 2
eps = 1e-2
=======
expr = "sqrt(log(x)) - 1"
L = 2.7
R = 3
eps = 1e-1
>>>>>>> 84cd015e26f45a64c149a54968af0c8aee686e9f

uu = daycung_oop(L, R, eps, expr)
print(f"Nghiệm của phương trình {expr} trên khoảng [{L}, {R}] là: {uu.Solve()}")

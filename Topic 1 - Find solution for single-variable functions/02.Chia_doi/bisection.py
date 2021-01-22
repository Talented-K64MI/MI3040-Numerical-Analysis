#===================================================================================
#
#   Code (đã cái tiến) cho PP chia đôi. 
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
class bisection_oop:
#{
    def __init__(self, a_0, b_0, eps, expr):
    #{
        self.symf = sympify(expr);
        self.f = lambdify(symbols("x"), self.symf, "math");
        self.a_0 = a_0;
        self.b_0 = b_0;
        self.eps = eps;
    


    def __checkInputValidity(self):
    #{
        L = self.a_0
        R = self.b_0

        # Corner case: f(L) = 0 or f(R) = 0
        if(self.f(L) == 0 or self.f(R) == 0): return 1

        # Check if a < b
        if(L > R or (L == R and self.f(L) != 0)): return 0

        # Check if f(a) * f(b) < 0
        if(self.f(L) * self.f(R) >= 0): return 0
        
        return 1
    #}
    def __bisectionMethod(self):
    #{
        # Internal function 
        # Return root of f(x) = 0 which f(x), eps and range [a_0, b_0] are given.
        # Assign [a, b] and eps
        nIterations = 0
        left    = self.a_0
        right   = self.b_0
        epsilon = self.eps

        # Special case: f(a) = 0 or f(b) = 0
        if(self.f(left) == 0): return left
        if(self.f(right) == 0): return right

        # Evaluation phase
        mid   = (left + right) / 2
        lft_sign = 1 if self.f(left) >= 0 else -1
        while abs(right - left) >= epsilon:
        #{
            mid = (left + right) / 2
            val = self.f(mid)

            # print(left, mid, right, sep=',', file=sys.stderr)

            if(val == 0): return mid
            if(val * lft_sign < 0):
                right = mid
            else:
                left = mid

            nIterations = nIterations + 1
        #}
        
        # print(left, mid, right, sep=',', file=sys.stderr)
        print(f"Phương pháp chia đôi kết thúc sau {nIterations} lần lặp")
        return mid
    #}


    def Solve(self):
    #{
        if(self.__checkInputValidity() == 0):
        #{
            print("Invalid input. The program will now exit", file=sys.stderr)
            return float("NaN")
        #}
        return self.__bisectionMethod()
    #}
#}


#===================================================================================
# Chương trình ví dụ
# uu = bisection_oop(L, R, eps, input_expr)
# print(uu.Solve())
uu = bisection_oop(-2, 2, 1e-10, "x^2+5")
print(f" Nghiệm của PT f(x) = 0 theo PP chia đôi là: x = {uu.Solve()}")

#===================================================================================
#
#   Code (đã cái tiến) cho PP dây cung. 
#       * Input: f(x) trong pt f(x) = 0; khoảng cách li ban đầu (a, b); sai số epsilon
#       * Output: Nghiệm PT f(x) = 0;
#       * Hạn chế: Chưa có gói tìm khoảng cách lý nghiệm và phần tính giá trị f(x) chưa tối ưu
#       * Cải tiến: Giảm khối lượng tính toán - tính f(a) 1 lần
#       
#===================================================================================
from math import *
import sys


#===================================================================================
# Phần thuật toán chính
def evaluate(x, evalString):
#{
    return eval(evalString);
#}
def checkInputValidity(L, R, evalString):
#{
    #Check if a < b
    if(L > R): return 0;
    if(L == R and evaluate(L, evalString) != 0): return 0;

    #Check if f(a) * f(b) < 0
    fa = evaluate(L, evalString);
    fb = evaluate(R, evalString);
    if(fa * fb >= 0): return 0;
    
    return 1;
#}
def internal___bisectionMethod(initialLeftBound, initialRightBound, epsilon, evalString):
#{
    if(evaluate(initialLeftBound, evalString) == 0): return initialLeftBound;
    if(evaluate(initialRightBound, evalString) == 0): return initialRightBound;

    # Internal function 
    # Return root of f(x) = 0 which f(x), eps and range [a, b] are given.

    left  = initialLeftBound;
    right = initialRightBound;
    mid   = (left + right) / 2;
    lft_sign = 1 if evaluate(left, evalString) >= 0 else -1;


    while abs(right - left) >= epsilon:
    #{
        mid = (left + right) / 2;
        val = evaluate(mid, evalString);


        #print(left, mid, right, sep=',', file=sys.stderr)

        
        if(val == 0): return mid;
        if(val * lft_sign < 0):
            right = mid;
        else:
            left = mid;
    #}
    
    #print(left, mid, right, sep=',', file=sys.stderr)
    return mid;
#}




#===================================================================================
# Hàm giải phương trình sử dụng các hàm từ thuật toán chính
def bisectionMethod(initialLeftBound, initialRightBound, epsilon, evalString):
#{
    if(checkInputValidity(initialLeftBound, initialRightBound, evalString) == 0):
    #{
        print("Invalid input. The program will now exit");
        return;
    #}
    print(internal___bisectionMethod(initialLeftBound, initialRightBound, epsilon, evalString));
#}






#===================================================================================
# Chương trình ví dụ
input_expr = input('Please enter f(x) in f(x) = 0 equation: ');
L   = float(input('Please enter the initial left bound a = '));
R   = float(input('Please enter the initial right bound b = '));
eps = float(input('Please enter the error value eps = '));
bisectionMethod(L, R, eps, input_expr);

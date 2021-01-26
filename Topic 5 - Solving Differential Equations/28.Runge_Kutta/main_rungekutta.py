from sympy import *
from math import *
import sys


from lib_rungekutta import *

# Cấp chính xác
precision_x   = 3;
precision_y   = 7;
precision_eps = 12;


# Nhập dữ liệu
expr      = input("Nhập hàm f(x, y)trong phương trình y' = f(x, y) = ");
x_0       = float(input("Nhập giá trị ban đầu x_0 = "));
y_0       = float(input(f"Nhập giá trị ban đầu y({x_0}) = "));
h         = float(input("Nhập khoảng cách giữa 2 điểm liên tiếp h = "));
n         = int(input("Nhập số mốc của lưới điểm n = "));
s         = input("Nhập số nấc Runge-Kutta (1, 2, 3, 4 hoặc Heun):");

# Giải PTVP
s  = s if(s == "heun" or s == "Heun") else int(s); 
uu = rungekutta_oop(expr, x_0, y_0, h, n, s);
g  = (uu.Solve());



# In ra sai số và kết quả
if(s == "heun" or s == "Heun"):
#{
    print(f"Phương pháp Runge-Kutta 3 nấc với cấu hình hệ số kiểu Heun hoàn tất với lưới điểm sau, sai số toàn cục O(h^3) = {round(h**3, precision_eps)}:");
#}
else:
#{
    print(f"Phương pháp Runge-Kutta {s} nấc với hoàn tất với lưới điểm sau, sai số toàn cục O(h^{s}) = {round(h**s, precision_eps)}:");
#}
for x in g: print(round(x[0], precision_x), round(x[1], precision_y));

# Đồ thị
uu.getPlot();


# Nghiệm kiểm chứng
print("====================================================================")
sol_expr  = input("Nhập phương trình nghiệm kiểm chứng y(x) hoặc NONE nếu không có: y(x) = ");
if(sol_expr != "NONE"):
#{
    sol = lambdify(symbols("x"), sympify(sol_expr), "math");
    print("So sánh với giá trị đúng của nghiệm:");
    for x in g: print(f"y*({round(x[0], precision_x)}) = {round(x[1], precision_y)}, so sánh với giá trị chuẩn y({round(x[0], precision_x)}) = {round(sol(x[0]), precision_y)}, sai số {round(abs(sol(x[0]) - x[1]), precision_eps)}");
#}



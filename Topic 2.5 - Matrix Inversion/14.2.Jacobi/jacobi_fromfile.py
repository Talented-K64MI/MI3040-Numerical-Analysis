import sympy as sym
import scipy as sci
import numpy as np
from math import *
import sys

from lib_jacobi import *

A             = np.zeros((1,0));
n             = 0;
eps           = 0;
wholeSize     = 1;


# Load ma trận từ file
while(n * n != wholeSize):
#{
    print("Đang tải ma trận.....");
    A = np.loadtxt("input.txt");
    A = np.ravel(A);

    # Tự sinh kích thước ma trận
    wholeSize = np.shape(A)[0];
    n = int(sqrt(wholeSize));


    if (n * n != wholeSize):
    #{
        c = input("Kích cỡ ma trận không hợp lệ. Vui lòng chỉnh sửa file input.txt gõ \"Y\" để tải lại chương trình hoặc gõ \"N\" để thoát chương trình:");
        if(c == "N"):
            exit();
    #}
    else:
        A = np.reshape(A, (n,n));
        print("Tải ma trận thành công.")
#}


# Nhập sai số eps
eps           = float(input("Nhập sai số eps: "));

# In ra ma trận A
print("--------------------------------------------------------------------");
print("Ma trận A:");
print(A);


# Nghịch đảo ma trận
uu = jacobi_mat_inversion(A, n, eps);
A1 = uu.jacobi_iteration(1);

# In ra ma trận nghịch đảo
print("--------------------------------------------------------------------");
print("Ma trận nghịch đảo của A theo PP Jacobi tiên nghiệm:");
print(A1);

# Kiểm tra nhân ngược
print("--------------------------------------------------------------------");
print("Kiểm tra nhân ngược:");
print(A1 @ A);



A2 = uu.jacobi_iteration(2);
# In ra ma trận nghịch đảo
print("--------------------------------------------------------------------");
print("Ma trận nghịch đảo của A theo PP Jacobi hậu nghiệm:");
print(A2);

# Kiểm tra nhân ngược
print("--------------------------------------------------------------------");
print("Kiểm tra nhân ngược:");
print(A2 @ A);
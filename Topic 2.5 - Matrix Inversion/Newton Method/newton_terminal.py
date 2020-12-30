import sympy as sym
import scipy as sci
import numpy as np
from math import *
import sys

from lib_newton import *


#===================================================================================
# Chương trình ví dụ
n = 2          # Kích cỡ ma trận
A = [1,5,6,-3] # Ma trận đầu vào
eps = 0.0001   # Sai số epsilon


# Tiến hành thuật toán
A = np.reshape(np.array(A), (n, n));
uu = newton_mat_inversion(A, n, eps);
print(A);


# In ra ma trận A
print("--------------------------------------------------------------------");
print("Ma trận A:");
print(A);

# Nghịch đảo ma trận
print("--------------------------------------------------------------------");
print("Tiến hành nghịch đảo ma trận bằng PP Newton....")
uu = newton_mat_inversion(A, n, eps);
A1 = uu.improved_newton();

# In ra ma trận nghịch đảo
print("--------------------------------------------------------------------");
print("Ma trận nghịch đảo của A:");
print(A1);

# Kiểm tra nhân ngược
print("--------------------------------------------------------------------");
print("Kiểm tra nhân ngược:");
print(A1 @ A);
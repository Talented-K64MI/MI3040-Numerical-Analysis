import sympy as sym
import scipy as sci
import numpy as np
from math import *
import sys

from lib_jacobi import *


#===================================================================================
# Chương trình ví dụ
n = 2          # Kích cỡ ma trận
A = [1,5,6,-3] # Ma trận đầu vào
eps = 0.0001   # Sai số epsilon


# Tiến hành thuật toán
A = np.reshape(np.array(A), (n, n));
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
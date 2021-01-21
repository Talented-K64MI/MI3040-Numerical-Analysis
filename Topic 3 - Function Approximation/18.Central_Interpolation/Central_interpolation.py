# Đề tài: Tính giá trị của một điểm từ bảng số liệu cho trước bằng các công thức nội suy trung tâm
# Code bởi Lê Nguyên Bách - CTTN Toán Tin K64
# Ngôn ngữ sử dụng: Python 3.9
# Sửa đổi gần nhất vào ngày 6/1/2021

import time # Tính thời gian chạy code
from math import * # Thư viện cho phép dùng các hàm toán học
import numpy

# Tạo bảng sai phân (del_table)
def Above_add(Mat, num):
    # Thêm hàng mới (Gồm giá trị mới ở đầu hàng, còn lại là các số 0) lên trên đầu Mat
    new_row = numpy.zeros((1, len(Mat)))
    new_row[0][0] = num
    Mat = numpy.append(new_row, Mat, axis = 0)

    # Thêm cột chứa toàn số 0 vào bên phải Mat
    Mat = numpy.append(Mat, numpy.zeros((len(Mat), 1)), axis = 1)

    # Đặt các giá trị delta phù hợp vào đường chéo chính
    for i in range(1, len(Mat)):
        Mat[i][i] = Mat[i-1][i-1] - Mat[i][i-1]

    # Trả về ma trận Mat
    return Mat # Mat sẽ là ma trận tam giác dưới
def Below_add(Mat, num):
    # Tạo hàng mới (Gồm giá trị mới ở đầu hàng, còn lại là các giá trị delta tương ứng)
    new_row = numpy.zeros((1, len(Mat)+1))
    new_row[0][0] = num
    for i in range(len(Mat[0])):
        new_row[0][i+1] = Mat[len(Mat)-1][i] - new_row[0][i]

    # Thêm cột mới (Gồm các số 0) vào bên phải Mat
    Mat = numpy.append(Mat, numpy.zeros((len(Mat), 1)), axis = 1)

    # Bây giờ mới thêm hàng mới (new_row) vào phía dưới Mat
    Mat = numpy.append(Mat, new_row, axis = 0)

    # Trả về ma trận Mat
    return Mat  # Mat sẽ là ma trận tam giác dưới

# Công thức nội suy Stirling
def Stirling_coef(num):
    S = numpy.identity(num) # Khởi tạo ma trận đơn vị, cỡ num x num
    for i in range(1, num):
        S[i] = numpy.add(
            [-x*i*i for x in S[i-1]],
            numpy.roll(S[i-1], 1)
        )
    return S
def Stirling_interpolation(arr_x, arr_y, x):
    # Kiểm tra xem giá trị x có nàm ngoài khoảng nội suy hay không
    if x > arr_x[len(arr_x) - 1] or x < arr_x[0]:
        print("Giá trị x nằm ngoài khoảng nội suy")
        return None

    # Xác định mốc x_0
    h = arr_x[1] - arr_x[0] # Bước nhảy
    x0 = round((x - arr_x[0]) / h) # Chỉ số của giá trị hoành độ gần x nhất
    max_milestone = min(2 * min(len(arr_x) - 1 - x0, x0) + 1, 9) # Lấy (tối đa) 9 mốc nội suy phù hợp
    t = (x - arr_x[x0]) / h  # Biến phụ trong công thức nội suy Stirling
    t_square = t*t
    table = [list(a) for a in zip(arr_x, arr_y)] # Ghép hai mảng arr_x và arr_y vào nhau
    table = numpy.roll(table, -x0, axis = 0) # Chuyển vị trí của giá trị x0 về chỉ số 0 trong mảng

    # Khởi tạo ma trận cột T_odd chứa các biến t^(2i-1)
    # T_odd = transpose(t t^3 t^5 ... t^(2n-1))
    T_odd = numpy.full((max_milestone//2, 1), t)
    for i in range(max_milestone//2 - 1):
        T_odd[i+1][0] = T_odd[i][0]*t_square
    
    # Khởi tạo ma trận cột T_even chứa các biến t^(2i)
    # T_even = transpose(t^2 t^4 ... t^(2n))
    T_even = [i*t for i in T_odd]
    
    # Lập bảng sai phân, đồng thời khởi tạo các ma trận hàng A_even và A_odd
    # A_even = (a_2 a_4 ... a_(2n))
    # A_odd = (a_1 a_3 ... a_(2n-1))
    A_even = [[ ]]
    A_odd = [[ ]]
    del_table = [[table[0][1]]] # Bảng sai phân dưới dạng ma trận tam giác dưới
    for i in range(1, max_milestone//2 + 1):
        del_table = Above_add(del_table, table[i][1])
        del_table = Below_add(del_table, table[-i][1])
        l = len(del_table)
        A_odd = numpy.append(A_odd, [[(del_table[l-2][l-2] + del_table[l-1][l-2])/2/factorial(2*i-1)]], axis = 1)
        A_even = numpy.append(A_even, [[del_table[l-1][l-1]/factorial(2*i)]], axis = 1)

    # Công thức nội suy trung tâm
    # S(t) = y_0 + A_even.S.T_even + A_odd.S.T_odd
    S = Stirling_coef(max_milestone // 2)
    value = table[0][1] + numpy.add(A_even @ S @ T_even, A_odd @ S @ T_odd)[0][0]
    
    # Tính toán sai số
    error = A_even[0][len(A_even[0])-1]
    for i in range(1, (max_milestone + 1)//2):
        error *= (t_square - i*i)
        
    # Các giá trị trung gian (Uncomment 6 dòng dưới đây để theo dõi các giá trị này)
    # print("Ma trận chuyển vị của T_odd\n", numpy.transpose(T_odd), "\n")
    # print("Ma trận chuyển vị của T_even\n", numpy.transpose(T_even), "\n")
    # print("Ma trận A_odd\n", A_odd, "\n")
    # print("Ma trận A_even\n", A_even, "\n")
    # print("Bảng sai phân\n", del_table, "\n")
    # print("Ma trận S\n", S, "\n")

    # Đầu ra chính (Main output)
    print("Giá trị của f(x) tại x =", x, "là ", value)
    print("Sai số |R(t)| <", abs(error), "\n")
    return value

# Công thức nội suy Bessel
def Bessel_coef(num):
    B = numpy.identity(num) # Khởi tạo ma trận đơn vị, cỡ num x num
    for i in range(1, num):
        B[i] = numpy.add(
            [-x* (i-0.5)**2 for x in B[i-1]],
            numpy.roll(B[i-1], 1)
        )
    return B
def Bessel_interpolation(arr_x, arr_y, x):
    # Kiểm tra xem giá trị x có nàm ngoài khoảng nội suy hay không
    if x > arr_x[len(arr_x) - 1] or x < arr_x[0]:
        print("Giá trị x nằm ngoài khoảng nội suy")
        return None

    # Xác định mốc x_0
    h = arr_x[1] - arr_x[0] # Bước nhảy
    x0 = int(floor((x - arr_x[0]) / h)) # Chỉ số của giá trị hoành độ nằm bên trái x
    max_milestone = int(min(2 * min(x0 + 1, len(arr_x) - 1 - x0), 8)) # Lấy (tối đa) 8 mốc nội suy phù hợp
    u = (x - arr_x[x0]) / h - 0.5  # Biến phụ trong công thức nội suy Bessel
    u_square = u*u
    table = [list(a) for a in zip(arr_x, arr_y)] # Ghép hai mảng arr_x và arr_y vào nhau
    table = numpy.roll(table, -x0, axis = 0) # Chuyển vị trí của giá trị x0 về chỉ số 0 trong mảng

    # Khởi tạo ma trận cột U_even chứa các biến u^(2i)
    # U_even = transpose(1 u^2 u^4 ... u^(2n))
    U_even = numpy.full((max_milestone//2, 1), 1.0)
    for i in range(max_milestone//2 - 1):
        U_even[i+1][0] = U_even[i][0]*u_square
    

    # Khởi tạo ma trận cột U_even chứa các biến u^(2i+1)
    # U_even = transpose(u u^3 u^5 ... u^(2n+1))
    U_odd = [i*u for i in U_even]
    

    # Khởi tạo ma trận hàng chứa các hệ số a_i
    # A = (a_0 a_1 a_2 a_3 ... a_n)
    A_even = [[(table[0][1] + table[1][1])/2]]
    del_table = [[table[0][1]]]  # Bảng sai phân dưới dạng ma trận tam giác dưới
    del_table = Above_add(del_table, table[1][1])
    A_odd = [[del_table[1][1]]]
    for i in range(1, max_milestone//2):
        del_table = Above_add(del_table, table[i+1][1])
        del_table = Below_add(del_table, table[-i][1])
        l = len(del_table)
        A_even = numpy.append(A_even, [[(del_table[l-2][l-2] + del_table[l-1][l-2])/2/factorial(2*i)]], axis = 1)
        A_odd = numpy.append(A_odd, [[del_table[l-1][l-1] / factorial(2*i+1)]], axis = 1)
    
    # Công thức nội suy Bessel: B(u) = A.B.U
    B = Bessel_coef(max_milestone//2)
    print(B)
    value = numpy.add(A_even @ B @ U_even, A_odd @ B @ U_odd)[0][0] # Toán tử @ dùng để nhân ma trận
    

    # Tính toán sai số
    error = A_odd[0][len(A_odd[0])-1]
    for i in range(max_milestone//2):
        error *= (u_square - (i+0.5)**2)
        
    # Các giá trị trung gian (Uncomment 6 dòng dưới đây để theo dõi các giá trị này)
    # print("Ma trận chuyển vị của U_even\n", numpy.transpose(U_even), "\n")
    # print("Ma trận chuyển vị của U_odd\n", numpy.transpose(U_odd), "\n")
    # print("Bảng sai phân\n", del_table, "\n")
    # print("Ma trận hệ số chẵn\n", A_even, "\n")
    # print("Ma trận hệ số lẻ\n", A_odd, "\n")
    # print("Ma trận B\n", B, "\n")
    
    print("Giá trị của f(x) tại x =", x, "là ", value)
    print("Sai số |R(x)| < ", abs(error), "\n")
    return value

start_time = time.time() # Ghi lại thời gian bắt đầu chạy code

arr_x = [0.000, 0.250, 0.500, 0.750, 1.000, 1.250, 1.500, 1.750, 2.000, 2.250, 2.500, 2.750, 3.000]
arr_y = [0.000, 0.074, 0.249, 0.486, 0.745, 1.006, 1.257, 1.493, 1.713, 1.920, 2.112, 2.291, 2.459]
x = 1.274

# Stirling_interpolation(arr_x, arr_y, x)
Bessel_interpolation(arr_x, arr_y, x)

end_time = time.time() # Ghi lại thời gian kết thúc code
print("Total runtime", (end_time - start_time)*1000, "ms")

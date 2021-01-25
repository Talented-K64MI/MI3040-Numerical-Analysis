# Đề tài: Công thức nội suy ngược
# Code bởi Lê Nguyên Bách - CTTN Toán Tin K64
# Ngôn ngữ sử dụng: Python 3.9
# Sửa đổi gần nhất vào ngày 26/1/2021

from math import *
import numpy
import time

# y = x + sin(x^(3/2))
arr_x = [1.000, 1.250, 1.500, 1.750, 2.000, 2.250, 2.500, 2.750, 3.000]
arr_y = [1.841, 2.235, 2.465, 2.486, 2.308, 2.019, 1.775, 1.762, 2.115] # n + 1 mốc nội suy

# Phân hoạch đơn điệu
def Monotonous_Partition(arr): # Phân hoạch đơn điệu
    extre_idx = [0] # Chỉ số của các điểm cực trị
    for i in range(1, len(arr) - 1):
        if arr[i] > max(arr[i-1], arr[i+1]) or arr[i] < min(arr[i-1], arr[i+1]):
            extre_idx.append(i)
        else:
            continue
    extre_idx.append(len(arr)-1)

    mono_par = [] # Mảng chứa chỉ số của dãy đơn điệu
    for j in range(len(extre_idx) - 1):
        mono_par.append([x for x in range(extre_idx[j], extre_idx[j+1] + 1)])

    print("Phân hoạch đơn điệu:", mono_par, "\n")
    return mono_par

# Tạo bảng sai phân (del_table)
def Add_ele(Mat, num): # Mat là bảng sai phân, num là giá trị bổ sung
    # Thêm hàng mới (Gồm giá trị mới ở đầu hàng, còn lại là các số 0) lên trên đầu Mat
    new_row = numpy.zeros((1, len(Mat)))
    new_row[0][0] = num
    Mat = numpy.append(new_row, Mat, axis=0)

    # Thêm cột chứa toàn số 0 vào bên phải Mat
    Mat = numpy.append(Mat, numpy.zeros((len(Mat), 1)), axis=1)

    # Đặt các giá trị delta phù hợp vào đường chéo chính
    for i in range(1, len(Mat)):
        Mat[i][i] = Mat[i - 1][i - 1] - Mat[i][i - 1]

    # Trả về bảng sai phân mới
    return Mat  # Mat sẽ là ma trận tam giác dưới

# Lập ma trận Phi
def Mat_phi(arr):
    # Lập bảng sai phân, đồng thời khởi tạo các ma trận hàng A
    # A = (del^2(y0)/2!  del^3(y0)/3!  ...  del^n(y0)/n!)
    A = [[]]
    del_table = [[arr[1], 0],
                 [arr[0], arr[1]-arr[0]]]  # Bảng sai phân dưới dạng ma trận tam giác dưới
    for i in range(2, len(arr)):
        del_table = Add_ele(del_table, arr[i])
        l = len(del_table)
        A = numpy.append(A, [[del_table[l-1][l-1] / factorial(i)]], axis=1)

    # Lập ma trận Coef cỡ (n-1) x n với các hàng là các tọa độ của
    # các đa thức t(t-1), t(t-1)(t-2), ..., t(t-1)(t-2)(...)(t-n+1)
    # theo cơ sở {t, t^2, t^3, ..., t^n}
    n = len(arr) - 1
    if n == 1: return None
    else:
        Coef = numpy.zeros((n - 1, n))
        Coef[0][0] = -1
        Coef[0][1] = 1
        for i in range(1, n - 1):
            Coef[i] = numpy.add(
                numpy.roll(Coef[i - 1], 1),
                [-x * (i + 1) for x in Coef[i - 1]]
            )
        return A @ Coef

# Trích ra mảng con gồm các mốc nội suy thích hợp
def Extract_subarr(arr, y):
    sgn = 1
    # Nếu mảng đang sắp xếp theo chiều giảm thì đảo ngược thứ tự lại
    if arr[0] > arr[1]: sgn *= -1
    arr = arr[::sgn]
    # Tìm chỉ số của 2 giá trị kề với y (Phương pháp chặt nhị phân)
    l_idx = 0
    r_idx = len(arr) - 1
    while True:
        idx = int((l_idx + r_idx) / 2)
        if y > arr[idx]: l_idx = idx
        else: r_idx = idx

        if r_idx - l_idx == 1: break

    if len(arr) - l_idx < r_idx + 1:
        a = min(r_idx + 1, 6)
        subarr = [arr[i] for i in range(a)]
    else:
        a = min(len(arr) - l_idx + 1, 6)
        subarr = [arr[i] for i in range(l_idx, l_idx + a - 1)]
    subarr = subarr[::sgn]
    print("Mảng con trích xuất: ", subarr)
    return subarr

# Công thức nội suy ngược
def Inverse_interpolation(arr_x, arr_y, y, eps):
    # Kiểm tra xem giá trị y có nàm ngoài khoảng nội suy hay không
    if y > numpy.max(arr_y) or y < numpy.min(arr_y):
        print("Giá trị y nằm ngoài khoảng nội suy")
        return None

    root = [] # Các nghiệm của phương trình f(x) = y
    h = arr_x[1] - arr_x[0] # Bước nhảy
    for idx_arr in Monotonous_Partition(arr_y):
        print("Với dãy đơn điệu có chỉ số", idx_arr)
        # Nếu y không nằm trong khoảng đơn điệu nào thì loại khoảng đơn điệu đó
        l = len(idx_arr)
        if y < min(arr_y[idx_arr[0]], arr_y[idx_arr[l-1]]) or y > max(arr_y[idx_arr[0]], arr_y[idx_arr[l-1]]):
            print("f(x) = y vô nghiệm tại khoảng này\n")
            continue
        elif l == 2:
            x = arr_x[idx_arr[0]] + h * (y - arr_y[idx_arr[0]]) / (arr_y[idx_arr[1]] - arr_y[idx_arr[0]])
            print("Phương trình f(x) = y có nghiệm x =", x, "\n")
            root.append(x)
        else:
            arr = [arr_y[i] for i in idx_arr]
            subarr = Extract_subarr(arr, y)
            Phi = Mat_phi(subarr)
            delta = subarr[1] - subarr[0]
            t = (y - subarr[0]) / delta # Xấp xỉ đầu t0 = (y - y0)/(y1 - y0)

            def Loop_func(t): # Hàm lặp trong công thức nội suy ngược
                T = [[t**i] for i in range(1, len(subarr))]
                return (y - subarr[0] - (Phi @ T)[0][0]) / delta

            # Thực hiện công thức lặp cho tới khi sai số nhỏ hơn epsilon
            while True:
                temp = Loop_func(t)
                error = abs((t - temp)/t)
                t = temp
                if error < eps:
                    break
            x = arr_x[arr_y.index(subarr[0])] + h * t
            print("Phương trình f(x) = y có nghiệm x =", x, "\n")
            root.append(x)

    return root

start_time = time.time()

print("Tập nghiệm của phương trình f(x) = y là:\n", Inverse_interpolation(arr_x, arr_y, 2, 1e-5))

end_time = time.time()

print("Total runtime", (end_time - start_time)*1000, "ms")
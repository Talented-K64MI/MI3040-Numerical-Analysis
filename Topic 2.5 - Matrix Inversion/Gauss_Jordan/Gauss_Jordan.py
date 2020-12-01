# Khai báo sử dụng thư viện Numpy
import numpy as np
np.set_printoptions(suppress=True, linewidth=np.inf, precision=10)

#Nhập ma trận
matrix = np.loadtxt("test3.txt", dtype="float", delimiter=" ")

test = matrix
n = len(matrix)
print(matrix)
index_row = []  # Mảng lưu các hàng của phần tử giải (theo thứ tự)
index_column = []  # Mảng lưu các cột của phần tử giải (theo thứ tự)
e = np.zeros([n,n])
for i in range(n):
    e[i,i] = 1.0
# Tìm trụ tối đại
def timtrutoidai():
    global index_row, index_column
    index_temp = []
    maxvalue = 0
    for row in range(0, len(matrix)):
        if row in index_row:  # Bỏ qua vì hàng này đã có phần tử giải
            continue
        max_row = np.amax(abs(matrix[row, 0:(len(matrix[0]))]))  # Tìm phần tử lớn nhất trong hàng row
        if (1 in matrix[row, 0:(len(matrix[0]))]) or (
                -1 in matrix[row, 0:(len(matrix[0]))]):  # Nếu có 1 hoặc -1 trong hàng row => chọn làm phần tử giải
            maxvalue = 1
            hang = row
            index_temp = np.where(abs(matrix[row, 0:(len(matrix[0]))]) == maxvalue)
            index_temp = index_temp[:1]
            index_temp = index_temp[0][0]
            break
        elif max_row > maxvalue:  # Lưu giá trị phần tử giải, tìm vị trí trên ma trận
            maxvalue = max_row
            hang = row
            index_temp = np.where(abs(matrix[row, 0:(len(matrix[0]))]) == maxvalue)
            index_temp = index_temp[:1]
            index_temp = index_temp[0][0]
    if maxvalue != 0:  # Lưu vị trí hàng và cột của phần tử giải
        index_row.append(hang)
        index_column.append(int(index_temp))
    else:
        print("Ma trận không khả nghịch!!!!")
        quit()


# Thuật toán GaussJordan
def GaussJordan():
    global matrix,e
    timtrutoidai()
    zeros_array = np.zeros([n,n])  # Tạo 1 ma trận không
    z = np.zeros([n,n])  # Tạo 1 ma trận không
    for row in range(0, len(matrix)):
        if row == index_row[-1]:
            continue
        m = - matrix[row][index_column[-1]] / matrix[index_row[-1]][index_column[-1]] #Tìm m
        zeros_array[row] = matrix[index_row[-1]] * m
        z[row] = e[index_row[-1]] * m
    matrix = matrix + zeros_array
    e = e+z


# Chuẩn hóa hệ số bằng 1
def chuanhoaheso():
    for i in range(len(index_row)):
        e[index_row[i]] = e[index_row[i]] / matrix[index_row[i]][index_column[i]]
        matrix[index_row[i]] = matrix[index_row[i]] / matrix[index_row[i]][index_column[i]]
def sosanh(a, b, n):
    check = 0
    for i in range(n):
        if a[i] > b[i]: return 1
        elif a[i] < b[i]: return -1
    return  check

# Chương trình chính
print("- - - - - - - - - - - - - - - - - - - -")
print()
print("Gauss-Jordan method to find the inversed matrix")
for i in range(0, n):
    GaussJordan()
chuanhoaheso()
print()
for i in range(n):
    for j in range(0, n-i-1):
        if sosanh(matrix[j],matrix[j+1],n) == -1:
            for k in range(n):
                matrix[j,k], matrix[j+1, k] = matrix[j+1, k], matrix[j, k]
                e[j, k], e[j + 1, k] = e[j + 1, k], e[j, k]
print("Ma trận nghịch đảo là:")
print(e)
print("=======================================================")

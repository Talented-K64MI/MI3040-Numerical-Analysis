import numpy as np  # Khai báo sử dụng thư viện Numpy(xử lý ma trận)
np.set_printoptions(suppress=True, linewidth=np.inf, precision=10)  # Căn chỉnh ma trận lúc in ra trên màn hình

# Đọc ma trận từ file
matrix = np.loadtxt("VD.txt", delimiter=' ')
index_row = []  # Khởi tạo mảng lưu các hàng của phần tử giải (theo thứ tự)
index_column = []  # Khởi tạo mảng lưu các cột của phần tử giải (theo thứ tự)
result = np.zeros((len(matrix[0])-1, 1))  #Khởi tạo ma trận lưu kết quả (mảng 0)


# Kiểm tra lại nghiệm
def kiemtranghiem():
    A = np.loadtxt("VD.txt", delimiter=' ')[:, :-1]
    print()
    print("- - - - - Kiểm tra nghiệm - - - - -")
    print(np.matmul(A, result))  # In ra ma trận A * ma trận X


# Tìm phần tử giải
def timphantugiai():
    global index_row, index_column
    index_temp = []
    maxvalue = 0
    for row in range(0, len(matrix)):
        if row in index_row:  # Bỏ qua vì hàng này đã có phần tử giải
            continue
        max_row = np.amax(abs(matrix[row, 0:(len(matrix[0]) - 1)]))  # Tìm phần tử lớn nhất trong hàng row
        if (1 in matrix[row, 0:(len(matrix[0]) - 1)]) or (
                -1 in matrix[row, 0:(len(matrix[0]) - 1)]):  # Nếu có 1 hoặc -1 trong hàng row => chọn làm phần tử giải
            maxvalue = 1
            hang = row
            index_temp = np.where(abs(matrix[row, 0:(len(matrix[0]) - 1)]) == maxvalue)
            index_temp = index_temp[:1]
            index_temp = index_temp[0][0]
            break
        elif max_row > maxvalue:  # Lưu giá trị phần tử giải, tìm vị trí trên ma trận
            maxvalue = max_row
            hang = row
            index_temp = np.where(abs(matrix[row, 0:(len(matrix[0]) - 1)]) == maxvalue)
            index_temp = index_temp[:1]
            index_temp = index_temp[0][0]
    if maxvalue != 0:  # Lưu vị trí hàng và cột của phần tử giải
        index_row.append(hang)
        index_column.append(int(index_temp))
        # In ra giá trị và vị trí phần tử giải
        print("Phan tu giai: ", round(matrix[index_row[-1]][index_column[-1]], 10))
        print("Vi tri: ", index_row[-1] + 1, index_column[-1] + 1)
        print()


# Thuật toán GaussJordan
def GaussJordan():
    global matrix
    timphantugiai()
    zeros_array = np.zeros((len(matrix), len(matrix[0])))  # Tạo 1 ma trận không
    for row in range(0, len(matrix)):
        if row == index_row[-1]:
            continue
        m = - matrix[row][index_column[-1]] / matrix[index_row[-1]][index_column[-1]] #Tìm m
        zeros_array[row] = matrix[index_row[-1]] * m
    matrix = matrix + zeros_array


# Chuẩn hóa hệ số bằng 1
def chuanhoaheso():
    for i in range(len(index_row)):
        matrix[index_row[i]] = matrix[index_row[i]] / matrix[index_row[i]][index_column[i]]
    print(matrix)


# Kết luận nghiệm
def ketluan():
    rank1 = 0  # Hạng của ma trận hệ số x
    rank2 = 0  # Hạng của ma trận mở rộng
    for row in range(0, len(matrix)):
        if np.amax(abs(matrix[row, 0:(len(matrix[0]) - 1)])) > 0:
            rank1 = rank1 + 1
        if np.amax(abs(matrix[row, 0:len(matrix[0])])) > 0:
            rank2 = rank2 + 1
    if rank1 < rank2:
        print("Hệ PT vô nghiệm!")
    elif rank1 < (len(matrix[0]) - 1):
        print("Hệ PT có vô số nghiệm")
        bieudien()
    else:
        print("Hệ PT có nghiệm duy nhất")
        bieudien()
        kiemtranghiem()


# Biểu diễn nghiệm
def bieudien():
    global result
    flag = False
    for column in range(len(matrix[0]) - 1):
        if (column + 1 >= (len(matrix[0]) - 1) / 2) and (flag == False):  # In các x và dấu ở giữa
            flag = True
            print("X = ", end="")
            if column in index_column:
                vt = index_column.index(column)
                print("  |{:>15.10f}| ".format(matrix[index_row[vt]][len(matrix[0]) - 1]), end="")
                for i in range(len(matrix[0]) - 1):
                    if i not in index_column:
                        print("-   |{:>15.10f}|x{} ".format(matrix[index_row[vt]][i], i + 1), end="")
                print()
            else:
                print("  |{:>15.10f}| ".format(0), end="")
                for i in range(len(matrix[0]) - 1):
                    if i not in index_column:
                        if column == i:
                            print(" -  |{:>15.10f}|x{}".format(-1, i + 1), end="")
                        else:
                            print(" -  |{:>15.10f}|x{}".format(0, i + 1), end="")
                print()

        else:
            if column in index_column:
                vt = index_column.index(column)
                print("      |{:>15.10f}| ".format(matrix[index_row[vt]][len(matrix[0]) - 1]), end="")
                for i in range(len(matrix[0]) - 1):
                    if i not in index_column:
                        print("    |{:>15.10f}|  ".format(matrix[index_row[vt]][i]), end="")
                print()
            else:
                print("      |{:>15.10f}| ".format(0), end="")
                for i in range(len(matrix[0]) - 1):
                    if i not in index_column:
                        if column == i:
                            print("    |{:>15.10f}|  ".format(-1), end="")
                        else:
                            print("    |{:>15.10f}|  ".format(0), end="")
                print()
        try:
            result[column] = matrix[index_row[vt]][len(matrix[0]) - 1]  # Cho các nghiệm x vào ma trận result
        except:
            pass


# Chương trình chính
print(matrix)
print("- - - - - - - - - - - - - - - - - - - -")
print()
for i in range(0, min(len(matrix), len(matrix[0]))):
    GaussJordan()
    print(matrix)
    print("- - - - - - - - - - - - - - - - - - - -")
print("- - - - - Chuẩn hóa hệ số - - - - -")
chuanhoaheso()
print("- - - - - Kết luận - - - - -")
ketluan()

#Khai báo thư viện
import numpy as np
import  math
#Load file
f = open("input.txt", "r")
a = f.readline()
n =  int(a)
print('Ma trận cỡ: {} x {}'.format(n, n))
b = f.readline()
b = b.split()
X = []
for i in (b):
    X.append(float(i))
X = np.array(X)
Y = X.reshape(n, 1)
#print('Vector Y là: ',X)
# Y = np.random.rand(n, 1)
c = f.read()
c = c.split()
A = []
for i in c:
    A.append(float(i))
A = np.array(A).reshape(n, n)
print('Ma trận A là: ')
print(A)
print('_'*100)

E = 0.1
#Chuẩn hóa
def Chuan_Hoa(M):
    maxi = abs(M[0][0])
    c = M[0][0]
    for i in range (len(M)):
        if maxi < abs(M[i][0]):
            maxi = abs(M[i][0])
            c = M[i][0]
    matrix = M / c
    return matrix
#Kiểm tra
def Kiem_tra(B, m, n):
    A = B[m] - B[n]
    return max(abs(A))
#Lũy thừa
def Luy_thua(A, B, m):
    M = A.dot(B[m])
    return M

#Xử lí
def Xu_li(A, Y):
    B = []
    B.append(Y)
    Z = np.zeros((n, 1))

    B.append(Luy_thua(A, B, 0))
    B.append(Luy_thua(A, B, 1))
    B.append(Luy_thua(A, B, 2))
    m = 3
    TH = 4
    while True:
        M = []
        F = B[-1]
        for i in range (len(F)):
            x = round(F[i][0], 4)
            M.append(x)
        M = np.array(M).reshape(n, 1)
        if sum(F == Z) == n:
            sys.exit()
        if m == 50:
            break
        if Kiem_tra(B, m - 1, m - 2) <= E:
            TH = 1
            break
        if Kiem_tra(B, m  - 1, m - 3) <= E:
            TH = 3
            break
        m += 1
        B.append(Chuan_Hoa(Luy_thua(A, B, m - 1)))


    return m, TH, B
#Chuyển ma trận xuống thang
def Chuyen_MT(A, VTR):
    B = A
    V = VTR.reshape(n,)
    M = np.eye(n, dtype=float)
    maxi_1 = V.max()
    index = 0
    for i in range (n):
        if V[i] == maxi_1:
            index += i
            break
    E = M[: , index: index + 1] - VTR.reshape(n, 1)
    E[index][0] =0
    M[:, index: index + 1] = E
    A = M.dot(A)
    return A
for i in range(n):
    m, TH, B = Xu_li(A, Y)

    if TH == 1:
        VTR = B[-1]
        VTR_T = VTR.reshape(1, n)
        AX = A.dot(VTR)

        XTAX = (VTR_T.dot(AX))
        XTX = (VTR_T.dot(VTR))
        lamda = XTAX[0] / XTX[0]
        lamda = round(lamda[0], 4)
        print('Sau {} lần lặp'.format(m))
        print('Giá trị riêng là: ', lamda)
        print('Vector riêng tương ứng là: ')
        print(VTR)
        A = Chuyen_MT(A, VTR)
        Y = np.random.rand(n,1)
        print('_' * 100)
    elif TH == 3:
        AmY = A.dot(B[-1])
        Am1Y = A.dot(AmY)
        Am2Y = A.dot(Am1Y)
        lamda_N = max(Am2Y)/max(AmY)
        lamda_N = math.sqrt(lamda_N[0])

        VTR_N = Am1Y + lamda_N * AmY
        VTR_N = Chuan_Hoa(VTR_N)
        print('Sau {} lần lặp'.format(m))
        print('Giá trị riêng là: ', round(lamda_N, 4))
        print('Vector tương ứng là: ')
        print(VTR_N)
        A = Chuyen_MT(A, VTR_N)
        Y = np.random.rand(n, 1)
        print('_' * 100)

    elif TH == 4:
        M = B[-1]
        AmY = A.dot(M)
        Am1Y = A.dot(AmY)
        a_1 = Am1Y[0][0]
        a_2 = Am1Y[1][0]
        b_1 = AmY[0][0]
        b_2 = AmY[1][0]
        c_1 = M[0][0]
        c_2 = M[1][0]
        a = 1
        b = (a_1 * c_2 - c_1 * a_2) / (c_1 * b_2 - b_1 * c_2)
        c = (b_1 * a_2 - a_1 * b_2) / (c_1 * b_2 - b_1 * c_2)
        print('Phươnng trình tìm đc: Z^2 + {}Z + {} = 0 '.format(b, c))
        print()
        denta = b ** 2 - 4 * a * c
        if denta >= 0:
            print('Phương trình có denta >= 0')
        else:
            lamda_1 = complex(-b / (2 * a), -math.sqrt(abs(denta)) / (2 * a))
            lamda_2 = complex(-b / (2 * a), math.sqrt(abs(denta)) / (2 * a))
            VTR_1 = Am1Y - lamda_1 * AmY
            VTR_2 = Am1Y - lamda_2 * AmY
            print('Giá trị riêng là: {}'.format(lamda_1))
            print('Vector riêng tương ứng là: ')
            print(VTR_1)
            print('*' * 100)
            print('Gía trị riêng là: {}'.format(lamda_2))
            print('Vector riêng tương ứng là: ')
            print(VTR_2)
        break


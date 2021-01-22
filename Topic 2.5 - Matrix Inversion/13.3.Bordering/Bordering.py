import time
import numpy as np
np.set_printoptions(suppress=True, linewidth=np.inf, precision=12)
print("========================================================================")
print("Chương Trình Tìm nghịch đảo của ma trận bằng phương pháp viền quanh")
print("========================================================================")
a = np.loadtxt("test1.txt",dtype='float', delimiter=' ')
n = len(a)
b = np.transpose(a)
t = b.dot(a)
check = True
print(t)
print(np.linalg.det(t))
print("Ma trận vừa nhập là:")
print(a)
print("========================================================================")
def bordering(a, n):# Nhap ma tran a va kich thuoc cua ma tran

    if n == 2: #Trường hợp chặn đệ quy
        inv = np.zeros([2,2]) #Khởi tạo ma trận nghịch đảo alpha^-1
        if (a[0, 0] * a[1, 1] - a[1, 0] * a[0, 1]) == 0:
            print("Ma tran ko kha nghich")
            quit()
        else:
            inv[0, 0] = a[1, 1] / (a[0, 0] * a[1, 1] - a[1, 0] * a[0, 1])
            inv[0, 1] = -a[0, 1] / (a[0, 0] * a[1, 1] - a[1, 0] * a[0, 1])
            inv[1, 0] = -a[1, 0] / (a[0, 0] * a[1, 1] - a[1, 0] * a[0, 1])
            inv[1, 1] = a[0, 0] / (a[0, 0] * a[1, 1] - a[1, 0] * a[0, 1])
            return inv
    a_11 = np.zeros([n - 1, n - 1])  # Khởi tạo các ma trận con
    a_12 = np.zeros([n - 1, 1])
    a_21 = np.zeros([1, n - 1])
    a_22 = a[n - 1, n - 1]
    for i in range(0, n - 1):
        for j in range(0, n - 1):
            a_11[i, j] = a[i, j]
    for i in range(0, n - 1):
        a_12[i, 0] = a[i, n - 1]
        a_21[0, i] = a[n - 1, i]
    if n>2: #Nếu chưa gặp trường hợp chặn
        a_111 = bordering(a_11, n-1)
        X = a_111.dot(a_12)
        Y = a_21.dot(a_111)
        theta = a_22 - (Y.dot(a_12))
        if abs(theta)<  1e-14:
            print('Ma Tran Khong Kha Nghich')
            quit()
        x = X.dot(Y)
        for i in range(0, n - 1):
            for j in range(0, n - 1):
                a[i, j] = a_111[i, j] + x[i, j] / theta
                a[n - 1, i] = Y[0, i] / (-theta)
                a[i, n - 1] = -X[i, 0] / theta
        a[n - 1, n - 1] = 1 / theta
    return a
st = time.time()
s = bordering(t, n)
et = time.time()

print("========================================================================")
if(check == True):
    print("Ma trận nghịch đảo là:")
    print(s.dot(b))
    np.savetxt("output.txt",s.dot(b),fmt= '%-.8f' ,delimiter=' ' )
else:
    print('Ma Tran Khong Kha Nghich')
print("========================================================================")
print((et-st)*1000,'ms')
print("========================================================================")
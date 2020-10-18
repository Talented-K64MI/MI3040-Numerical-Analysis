from sympy import *
import matplotlib.pyplot as plt
import numpy as np
import math

#input
inputPath_1 = 'example1.txt'
inputPath_2 = 'example1.txt'

outputPath_1 = 'outputPath_1.txt'

##############


R,result = Do(inputPath_1)
Save(R, result, outputPath_1, "w")

print("Radius of convergence = "+ str(R) + ", Result: ");
print(str(result))


###############

empty = lambda s: s != ''

#read input
def ReadArray(f):
    line = f.readline()
    result = list(map(float, list(filter(empty,line.split(' ')))))
    #print('result')
    #print(result)
    return result

def ReadMatrix(f):
    listCoef = []
    line = f.readline()
    while(line.strip() != ''):
        coef = list(map(float,list(filter(empty,line.split(' ')))))
        listCoef.append(coef)
        line = f.readline()
    #print('listCoef: ')
    #print(listCoef)
    return listCoef

def RandN(listCoef):
        # R & N
    R = listCoef[0][0]
    N = math.inf
    for coef in listCoef:
        if(R > coef[0]): R = coef[0]
        coef.pop(0)
        if(N > len(coef)): N = len(coef)
    print(listCoef)
    #print("bán kính hội tụ: ", end =''); print(R)
    #print("bậc tối đa sẽ tìm của t: ", end = ''); print(N)
    return (R,N)

def calculate(initial, listCoef, N):
    result = initial
    k=len(listCoef)
    for n in range(0,N-k):
        c=0
        #start calculating c_{n+k}
        for m in range(0,n+1):
            mult = 1
            for i in range(0,k):
                c+=listCoef[i][n-m] * result[m+i] * mult
                mult *= m+i+1
        offset = 1;
        for i in range(n+1,n+k+1): offset *= i
        c= -c/offset
        result.append(c)
    return result
    #print("result: ")
    #print(result)

def Do(inputPath):
    f = open(inputPath,"r")
    initial = ReadArray(f)
    listCoef = ReadMatrix(f)
    f.close()
    R,N = RandN(listCoef)
    result = calculate(initial, listCoef, N)
    return (R, result)

def Save(R, result, outputPath, mode):
    f = open(outputPath, mode)
    f.write("Radius of convergence = " + str(R) + ", Result: \n");
    f.write(str(result))
    f.close()

def Show():
    return 0

def validate():
    return 1










#code anh Chí
#for line in f:
#    __temp=line.split(",")
#    listCoef.append([(i) for i in __temp]) 
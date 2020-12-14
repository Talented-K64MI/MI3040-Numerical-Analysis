from mydata import *
import numpy as np
def specialCase1(A, k, j):
    '''
        Solve special case A[k][k-1] = 0 and A[k][j] != 0 (j < k-1)
        Switch column (row) k-1 and column (row) j
        Args:
            A: 2-D numpy array
            k: Element manipulation
        Return:
            Matrix is smilarity A
    '''
    copA = A.copy()
    copA[[k-1, j], :] = copA[[j, k-1], :]
    copA[:, [k-1, j]] = copA[:, [j, k-1]]
    return copA

def specialCase2(A, k):
    '''
        Solve special case A[k][k-1] = 0 and A[k][j] = 0 (j<k-1)
        Args:
            2-D numpy array
            k: Element manipulation
        Return:
            subFrobenius, B 
    '''
    
    return A[k:, k:], A[0:k, 0:k]

def findSimpleA(A, k):
    '''
        Find similar matrix (simple case - A[k][k-1]!=0) 
        Args:
            A: 2-D numpy array
            k: Element manipulation - A[k][k-1]
        Return:
            Similarity transformation of matrix A
    '''
    n, _ = A.shape
    M = np.eye(n)
    M[k-1, :] = A[k, :]

    #Find inverse of M
    inverseM = np.eye(n)
    inverseM[k-1, :] = -A[k, :] / A[k, k-1]
    inverseM[k-1, k-1] = 1 / A[k, k-1]

    #similarA = M*A*inverseM
    similarA = M.dot(A).dot(inverseM)
    return similarA, M, inverseM

def getCharPolynomial(A):
    '''
        Get characteristic polynomial from Frobenius matrix
        Args:
            A: 2-D Frobenius matrix
        Return:
            p: 1-d coefficients (high --> low)
    '''
    n = A.shape[0]
    p = (-1)**n * np.ones(n+1)
    p[1:] = p[1: ] * (-1) *A[0, :]
    return p

def mulPoly(p):
    '''
        Multiple coeffictients of polynomials
        p: list coefficients of polynomials
    '''
    res = p[0]
    for i in range(1, len(p)):
        res = np.polymul(res, p[i])
    return res

def Danilevski(A):
    '''
        Danilevski method for find eigenvalues, eigenvectors
        Args:
            A: 2-d numpy array
        Output:
            list_eigenvalues: Eigenvalues
            list_eigenvectors: Eigenvectors
    '''
    all_polynomial = []
    n = A.shape[0]
    back = np.eye(n)
    similar = A.copy()
    list_eigenvalues = []
    list_eigenvectors = []
    charFunc = []
    k = n-1
    m = n    #Size of matrix
    while k > 0:
        if similar[k, k-1] != 0:
            #Simple case
            similar, _, inverseM = findSimpleA(similar, k)
            back = back.dot(inverseM)
            
            #print(similar)
        else:
            non = False
            for j in range(0, k-1):
                #find similar[k][j] if equal 0
                if similar[k, j] != 0:
                    similar = specialCase1(similar, k , j)
                    
                    back[:, [j, k-1]] = back[:, [k-1, j]]
                    
                    non = True
                    k = k+1
                    break
                    
                    
            if not non:
                #Decompose columns
#                 print("Case 2")
                for j in range(k, m-1):
                    M = np.eye(m)
                    M[:k, j+1] = -similar[:k, j]
                    #Inverse M
                    inverseM = np.eye(m)
                    inverseM[:k, j+1] = similar[:k, j]
                    similar = M.dot(similar).dot(inverseM)
                    back = back.dot(inverseM)
                    
                tt= False
                #Find similar A[j, m-1] != 0
                for j in range(k-1, -1, -1):
                    if similar[j, m-1] != 0:
                        M = np.eye(m)
                        x = M[k:m, :]
                        y = M[k-1, :]
                        M = np.vstack([M[0:k-1, :], x, y])
                        M1 = M.T
                        similar = M.dot(similar).dot(M1)
                        back = back.dot(M1)
                        k = m;
                        tt = True
                        break
                
                if not tt:
                    X = similar[k:, k:]
                    #Get size of X
                    t = X.shape[0]
                    eigenValues = findValue(X)
                    for j in range(len(eigenValues)):
                        print("Vector rieng cua: ", eigenValues[j])
                        list_eigenvalues.append(eigenValues[j])
                        y = np.power(eigenValues[j], np.arange(t))[::-1].reshape((t, 1))
                        v = np.zeros((n, 1))
                        p = np.zeros((m, 1))
                        p[k:m] = y
                        p = back.dot(p)
                        v[:m] = p
                        list_eigenvectors.append(v)
                        print(v)
                    m = k
                    similar = similar[:k, :k]
                    back = np.eye(m)
#         print("K: ",k)
        k = k - 1
    X = similar
    t = X.shape[0]
    eigenValues = findValue(X)
    for j in range(len(eigenValues)):
        print("Vector rieng cua: ", eigenValues[j])
        list_eigenvalues.append(eigenValues[j])
        y = np.power(eigenValues[j], np.arange(t))[::-1].reshape((t, 1))
        p = np.zeros((m, 1))
        v = np.zeros((n, 1))
        p[k:m] = y
        p = back.dot(p)
        v[:m] = p
        list_eigenvectors.append(v)
        print(v)
    return list_eigenvalues, list_eigenvectors
def findValue(A):
    '''
        Find eigenvalue for frobenius matrix
        Args:
            A: 2-d numpy array
        Return:
            Eigenvalue
    '''
    p = getCharPolynomial(A)
    p = list(p)[::-1]
    eigenValues = findRoots(p)
    return sorted(eigenValues)
	
if __name__ == '__main__':
	A = np.array([[1, 2, 3, 4], [2, 1, 2, 3], [3, 2, 1, 2], [4, 3, 2, 1]])
	eigenvalues, eigenvectors = Danilevski(A)
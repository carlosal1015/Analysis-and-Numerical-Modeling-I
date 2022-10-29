import numpy as np
from numpy.linalg import inv
from numpy import linalg as LA
def SVD(a):
    n,m = np.shape(a)
    sig = np.zeros([n,m])
    b = np.matmul(a,a.T)
    print("C:")
    print(b)
    print("================")

    val, vec = np.linalg.eig(b)
    val.sort()
    print(val)
    print("U:")
    print(vec)

    print("================")

    for i in range(n):
        sig[i][i] = np.sqrt(val[n-i-1])
        
    print("SIGMA :")
    print(sig)
    
    ########################
    print("================")
    print("V: ")
    V = (np.matmul(inv(np.matrix(a)),np.matmul(vec,sig)))
    print(V)
    VALID = np.matmul(vec,(np.matmul(sig,np.transpose(V))))
    print("================")
    print("VALIDAR: ")
    print(VALID)
a = np.array([[-1,2],[0,1]])

SVD(a)
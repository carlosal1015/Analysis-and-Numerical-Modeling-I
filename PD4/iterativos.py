import numpy as np


def verificar(A):
    m, n = A.shape
    if m != n:
        print("La matriz no es cuadrada")
        return False
    return True


def matrizE(A):
    n = len(A)
    E = np.zeros(n, n)
    for i in range(n):
        for j in range(n):
            if i > j:
                E[i][j] = -A[i][j]
    return E


def iterativo(M, c, tol=1e-6):
    x = np.zeros_like(c)
    aux = x
    print("El x en la iteracion 0  es: ", x)
    x = np.dot(M, x) + c
    i = 1
    while np.linalg.norm(x - aux, np.inf) / np.linalg.norm(x, np.inf) > tol:
        print("El x en la iteracion", i, " es: ", x)
        aux = x
        x = np.dot(M, x) + c
        i = i + 1
    print("El numero de iteraciones es: ", i)
    print("La respuesta en la iteración ", i, " es:", x)


def GaussSeidel(A, b):
    D = np.diag(np.diag(A))
    E = matrizE(A)
    aux = D - E
    F = aux - A
    inv = np.linalg.inv(aux)
    G = np.dot(inv, F)
    c = np.dot(inv, b)
    iterativo(G, c)


def Richardson(A, b):
    n = len(A)
    I = np.identity(n)
    M = I - A
    iterativo(M, b)


def Jacobi(A, b):
    n = len(A)
    I = np.identity(n)
    D = np.diag(np.diag(A))
    print(D)
    invD = np.linalg.inv(D)
    J = I - np.dot(invD, A)
    c = np.dot(invD, b)
    iterativo(J, c)


#A = np.array([[10, -1, 2, 0], [-1, 11, -1, 3], [2, -1, 10, -1], [0, 3, -1, 8]], float)
A = np.array([[0.5, -0.2, 0.5], [0.1, 0.6, 0.4], [-0.3, 0.1, 0.0]], float)
#b = np.array([6, 25, -11, 15])
b = np.array([-1, 6.5, 0.7])
b = np.transpose(b)

#Jacobi(A, b)
Richardson(A, b) # da warning
#GaussSeidel(A, b) # no funciona
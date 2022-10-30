import numpy as np


def limpiadorm(ma, n):
    for i in range(0, n):
        for j in range(0, n):
            if abs(ma[i][j]) < 0.00000001:
                ma[i][j] = 0


def limpiadorv(vec, n):
    for i in range(0, n):
        if abs(vec[i]) < 0.00000001:
            vec[i] = 0


def crear_elemtal(n, k):
    e_k = np.array([0] * n)
    e_k[k - 1] = 1
    return e_k


def crear_P_k(n, k1, k2):
    P = np.array([crear_elemtal(n, i) for i in range(1, n + 1)])
    P[k1] = crear_elemtal(n, k2 + 1)
    P[k2] = crear_elemtal(n, k1 + 1)
    return P


def parlet_raid(A):
    n = len(A)
    P = np.identity(n)
    L_1 = np.identity(n)
    L = np.identity(n)
    for i in range(0, n - 2):
        b = np.zeros(n)
        for j in range(i, n - 1):
            b[1 + j] = A[j + 1][i]

        maximo = max(abs(b))
        posimax = np.where(b == maximo)
        band = b[i + 1]
        b[i + 1] = maximo
        b[posimax] = band
        b[i + 1] = 0
        P_k = crear_P_k(n, i + 1, posimax[0][0])
        P = np.dot(P_k, P)
        limpiadorm(P, n)
        b = b / maximo
        limpiadorv(b, n)
        print("vector b : \n", b)
        print("matriz P : \n", P_k)
        e_k = crear_elemtal(n, i + 2)
        M_k = np.identity(n) - np.outer(b, e_k)
        limpiadorm(M_k, n)
        print("matriz M : \n", M_k)
        L_1 = M_k @ P_k @ L_1
        limpiadorm(L, n)
        A = M_k @ P_k @ A @ P_k.T @ M_k.T
        limpiadorm(A, n)
        print("matriz A : \n", np.around(A, 6))
    L = np.linalg.inv(np.dot(L_1, P.T))
    print("Matriz L : \n", L)
    print("Matriz T : \n", A)


A = np.array(
    [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ],
    dtype=np.float64,
)

B = np.array([[0, 1, 2, 3], [1, 2, 2, 2], [2, 2, 3, 3], [3, 2, 3, 4]], dtype=np.float64)
parlet_raid(B)

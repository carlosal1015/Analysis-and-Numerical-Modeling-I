import numpy as np


def cholesky(A):
    n = len(A)
    l = np.zeros_like(A, dtype=float)
    suma = 0

    for j in range(n):
        suma = 0
        for k in range(j):
            suma += l[j][k] ** 2
        l[j][j] = np.sqrt(A[j][j] - suma)
        for i in range(j + 1, n):
            suma = 0
            for k in range(j):
                suma += l[i][k] * l[j][k]
            l[i][j] = (A[i][j] - suma) / l[j][j]

    return l


A = np.array([[50, 12, 35], [12, 3, 9], [35, 9, 29]], dtype=float)
l1 = cholesky(A)

# -*- coding: utf-8 -*-
import numpy as np


def LDLt(A, n):
    Lt = np.identity(n)
    for i in range(n):
        suma = A[i][i]
        for k in range(i):
            suma = suma - A[k][i] ** 2
        if suma < 0:
            print(" No es posible factorizar.")

        A[i][i] = np.sqrt(suma)
        for j in range(i + 1, n):
            suma = A[i][j]
            for k in range(i):
                suma = suma - A[k][i] * A[k][j]
            A[i][j] = suma / A[i][i]

    for j in range(n):
        for i in range(n):
            if i > j:
                A[i][j] = 0.0
    Lt = A
    L = Lt.T
    D = np.identity(n, float)

    for i in range(n):
        D[i][i] = L[i][i]
        for j in range(i + 1):
            L[i][j] = L[i][j] / D[j][j]

    Lt = L.T
    for i in range(n):
        D[i][i] = D[i][i] ** 2

    return L, D, Lt


A = np.array([[50, 12, 35], [12, 3, 9], [35, 9, 29]], dtype=float)

print("Factorización LDLt :")
print(A)
L, D, Lt = LDLt(A, 3)
print("Matriz L: ")
print(L)
print("Matriz D:")
print(D)
print("Matriz Lt:")
print(Lt)

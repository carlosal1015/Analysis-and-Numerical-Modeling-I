import numpy as np
import math
from numpy.linalg import eig

Ap = [[1, 1], [5, -3]]
bp = [16, 32]
A = np.transpose(Ap) @ Ap
b = np.transpose(Ap) @ bp


def SOR(A, b, x0, w, iter, tol):
    n = np.shape(A)[0]
    k = 0
    x = []
    while k < iter:
        for i in range(n):
            sum1 = sum(A[i][j] * x[j] for j in range(i))
            sum2 = sum(A[i][j] * x0[j] for j in range(i + 1, n))
            x.append((1 - w) * x0[i] + (w * (-sum1 - sum2 + b[i])) / A[i][i])
        if np.linalg.norm(np.array(x) - np.array(x0), 2) < tol or k < iter:
            print("Iteracion", k + 1, ": ")
            print(x)
        for i in range(n):
            x0[i] = x[i]
        k = k + 1
        x = []


SOR(A, b, [0, 0], 0.8, 300, 0.1)

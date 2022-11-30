import numpy as np
from numpy.linalg import inv
from numpy import linalg as LA
import pandas as pd
from tabulate import tabulate


def a(i, j):
    if j == 0:
        return 4
    elif (
        (j == i + 1 and i % 4 != 3)
        or (j == i - 1 and i % 4 != 0)
        or (j == i + 4 and i < 12)
        or (j == i - 4 and 3 < i < 16)
    ):
        return -1
    else:
        return 0


A = np.fromfunction(function=np.vectorize(a), shape=(16, 16), dtype=np.float64)
b = np.array(
    object=[
        1.902207,
        1.051143,
        1.175689,
        3.480083,
        0.819600,
        -0.264419,
        -0.412789,
        1.175689,
        0.913337,
        -0.150209,
        -0.264419,
        1.051143,
        1.966694,
        0.913337,
        0.819600,
        1.902207,
    ],
    dtype=np.float64,
)
x0 = np.zeros(16, dtype=np.float64)

tabla = {"x": [], "rk": [], "error": []}


def Max_des(A, b, x, tol):
    xk = x
    tabla["x"].append(xk.flatten())
    tabla["error"].append("=====")
    tabla["rk"].append("-----")
    iter = 100
    for i in range(iter):
        rk = b - np.dot(A, xk)
        num = np.dot(rk.T, rk)
        den = np.dot(np.dot(rk.T, A), rk)
        alphak = num / den
        xk1 = xk + alphak * rk
        if np.linalg.norm(xk1 - xk, np.inf) < tol:
            print("Se termina en la iteacion", i)
            break
        tabla["x"].append(xk.flatten())
        tabla["error"].append(np.linalg.norm(xk1 - xk, np.inf))
        tabla["rk"].append(rk.flatten())

        xk = xk1
    df = pd.DataFrame(tabla)
    print(tabulate(df, headers="keys", tablefmt="fancy_grid"))
    return xk


# probelma 1
# A = np.array([[3, 3, 4], [3, 6, 7], [4, 7, 11]], float)
# b = np.transpose(np.array([6, 9, 11]))
# x0 = np.transpose(np.array([1.0, 1.0, 1.0], float))

x0 = np.zeros(16, dtype=np.float64)
print(Max_des(A.T @ A, A.T @ b.T, x0, 1e-5))
print(np.linalg.solve(A.T @ A, A.T @ b.T))

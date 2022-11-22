# -*- coding: utf-8 -*-

"""
Métodos iterativos de SOR para la solución de sistema de sistema de ecuaciones lineales
"""

"""
Implementa el metodo de sor, para obtener una aproximacion de la solucion
del sistema Ax = b.
w: parametro de relajacion
x0: punto de inicializacion de la iteracion
"""

import numpy as np
import scipy.linalg as sl
import sys
import pandas as pd
from tabulate import tabulate

tabla = {"x": [], "error": []}

# ok
def inf_matrix(A):
    """
    Retorna la matriz triangular inferior de A.
    NOTA: No incluye la diagonal
    """
    E = np.zeros_like(A)
    nrowA = np.shape(A)[0]

    for k in range(nrowA):
        E[k, :k] = A[k, :k]

    return E


# ok
def sup_matrix(A):
    """
    Retorna la matriz triangular superior de A.
    NOTA: No incluye la diagonal.
    """

    F = np.zeros_like(A)
    nrowA = np.shape(A)[0]

    for k in range(nrowA):
        F[k, k + 1 :] = A[k, k + 1 :]

    return F


# ok
def radio_spectral(G):
    eig, *_ = sl.eig(G)

    max_eig = max(eig)
    return sl.norm(max_eig)


# ok
def ispositive(A):
    nrowA = np.shape(A)[0]
    return np.alltrue(sl.det(A[: k + 1, : k + 1]) for k in range(nrowA - 1))


def sor_iterations(A, b, x0, w, ERROR, NUM_ITERATIONS):
    """
    Implementa las iteraciones del metodo del sor
    """
    E = -inf_matrix(A)
    F = -sup_matrix(A)
    D = np.diag(np.diag(A))
    R = D - w * E
    S = (1 - w) * D + w * F
    invR = sl.inv(R)

    c = w * np.dot(invR, b)
    G = np.dot(invR, S)
    tabla["x"].append(x0.flatten())
    tabla["error"].append("---")

    # print("G = {}".format(G))
    for k in range(NUM_ITERATIONS):
        x1 = np.dot(G, x0) + c
        comp = sl.norm(x1 - x0) / sl.norm(x1)

        tabla["x"].append(x1.flatten())
        tabla["error"].append(comp)

        if comp < ERROR:
            df = pd.DataFrame(tabla)
            print(tabulate(df, headers="keys", tablefmt="psql"))
            return x1
        x0 = x1
    df = pd.DataFrame(tabla)
    print(tabulate(df, headers="keys", tablefmt="psql"))
    return x1


def sor_matrix(A, w):
    E = -inf_matrix(A)
    F = -sup_matrix(A)
    D = np.diag(np.diag(A))
    R = D - w * E
    S = (1 - w) * D + w * F
    if np.isclose(sl.det(R), 0.0):
        sys.exit("Matrix de sor indeterminada, utilice otro metodo iterativo.")
    invR = sl.inv(R)

    G = np.dot(invR, S)

    return G


def sor(A, b, x0, w, ERROR=1e-5, NUM_ITERATIONS=1000):
    if np.all(A == A.T) and ispositive(A):
        x = sor_iterations(A, b, x0, w, ERROR, NUM_ITERATIONS)
        return x

    elif radio_spectral(sor_matrix(A, w)) < 1:
        x = sor_iterations(A, b, x0, w, ERROR, NUM_ITERATIONS)
        return x
    else:
        print("El proceso iterativo de SOR, no converge")
        return x0


# A = np.array([[9, 3, 1], [16, 4, 1], [25, 5, 1]], float)
A_burden = np.array([[4, 3, 0], [3, 4, -1], [0, -1, 4]], float)
A_11 = np.array(
    [
        [4, -1, 0, -1, 0, 0],
        [-1, 4, -1, 0, -1, 0],
        [0, -1, 4, 0, 0, -1],
        [-1, 0, 0, 4, -1, 0],
        [0, -1, 0, -1, 4, -1],
        [0, 0, -1, 0, -1, 4],
    ],
    float,
)
print(f"A_11 = \n{A_11}\n")
# b = np.array([[0], [2], [5]], float)
# b_burden = np.array([[24], [30], [-24]], float)
b_11 = np.array([[0, 5, 0, 6, -2, 6]], float).T
print(f"b_11 = \n{b_11}\n")
# x0 = np.array([[1], [0], [0]], float)
# x0_burden = np.array([[1], [1], [1]], float)
x_0_11 = np.array([[0, 0, 0, 0, 0, 0]], float).T
print(f"x_0_11 = \n{x_0_11}\n")
# w < 1 o w >1    condicion necesaria de convergencia   0<w<2
# x_burden = sor(A_burden, b_burden, x0_burden, 1.25, 1e-9, 100)
x_11 = sor(A_11, b_11, x_0_11, 1, 0.001, 100)
# print(x_burden)
print(x_11)
# test = ispositive(A)
# test = [x for x in test]
# print(test)
# checkear si es

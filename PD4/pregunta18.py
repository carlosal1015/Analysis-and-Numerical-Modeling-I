import numpy as np
from scipy.sparse.linalg import cg

np.set_printoptions(suppress=True)

# A = np.array(
#     object=[
#         [
#             15000,
#             20000,
#             30000,
#         ],
#         [
#             10000,
#             15000,
#             20000,
#         ],
#         [
#             1,
#             1,
#             1,
#         ],
#     ],
#     dtype=np.float64,
# )

# b = np.array(
#     object=[
#         [
#             250000,
#             175000,
#             140,
#         ]
#     ],
#     dtype=np.float64,
# ).T

A = np.array([[3, 4, 6], [2, 3, 4], [1, 1, 1]])
b = np.array([[50, 35, 140]])
print(f"A = \n{A}")
print(f"b = \n{b}")
x = np.linalg.solve(A, b.T)
print(x)

# A_tilde = A.T @ A
# b_tilde = A.T @ b.T
# print(f"A_tilde = \n{A_tilde}")
# print(f"b_tilde = \n{b_tilde}")
# x = np.linalg.solve(A_tilde, b_tilde)
# print(x)


def is_pos_def(A):
    """Retorna verdadero si la matriz A es definida positiva"""
    return np.all(np.linalg.eigvals(A) > 0)


# print(is_pos_def(A_tilde))

# from gradienteconjugado import gradienteConjugada, imprimirResultados
# import pandas as pd
# from tabulate import tabulate

# x0 = np.zeros(3)
# iteraciones = 10

# gradienteConjugada(A, b.T, x0, iteraciones)

# resultados = {"alphak": [], "rk": [], "betak": [], "pk": [], "xk": []}

# imprimirResultados(resultados)

# x, exit_code = cg(A, b.T, maxiter=1000000)
# print(x)
# print(exit_code)

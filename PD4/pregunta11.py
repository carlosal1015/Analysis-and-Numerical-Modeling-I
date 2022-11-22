#!/usr/bin/env python

# -*- coding: utf-8 -*-

import numpy as np


"""Decomposition of the matrix A into the strictly lower triangular matrix L,
the diagonal matrix D and the strictly upper triangular matrix U.
"""


def diagonal(A):
    """Retorna la matriz diagonal de A."""
    D = np.diag(np.diag(A))
    return D


def lower_inferior(A):
    """Retorna la matriz estrictamente triangular inferior de -A."""
    E = np.zeros_like(A)
    n = len(A)
    for k in range(n):
        E[k, :k] = -A[k, :k]
    return E


def upper_superior(A):
    """Retorna la matriz estrictamente triangular superior de -A."""
    return diagonal(A) - lower_inferior(A) - A


def is_positive_definite(A):
    """Retorna verdadero si la matriz A es definida positiva."""
    return np.all(np.linalg.eigvals(A) > 0)


def is_symmetric(A, rtol=1e-5, atol=1e-8):
    """Retorna verdadero si la matriz A es simétrica."""
    return np.allclose(A, A.T, rtol=rtol, atol=atol)


A = np.array(
    object=[
        [4, -1, 0, -1, 0, 0],
        [-1, 4, -1, 0, -1, 0],
        [0, -1, 4, 0, 0, -1],
        [-1, 0, 0, 4, -1, 0],
        [0, -1, 0, -1, 4, -1],
        [0, 0, -1, 0, -1, 4],
    ],
    dtype=np.float64,
)
# print(f"Triangular superior:\n{-np.triu(A, 1)}\n")
# print(f"Triangular inferior:\n{-np.tril(A, -1)}\n")
b = np.array(object=[0, 5, 0, 6, -2, 6], dtype=np.float64).T
D = diagonal(A)
L = lower_inferior(A)
U = upper_superior(A)

if __name__ == "__main__":
    print(f"A = \n{D - L - U}\n")
    print(f"D = \n{D}\n")
    print(f"L = \n{L}\n")
    print(f"U = \n{U}\n")
    print(f"La matriz A es definida positiva: {is_positive_definite(A)}.\n")
    print(f"La matriz A es simétrica: {is_symmetric(A)}.\n")


def sor_left_sum(A, x_new, i):
    # Calcula $\operatorname{Left}\coloneqq\sum\limits_{j=1}^{i-1}a_{ij}x_j^{\left(k+1\right)}$
    result = 0
    for j in range(i - 1):
        result += A[i][j] * x_new[j]

    return result


def sor_right_sum(A, x_old, i):
    # Calcula $\operatorname{Right}\coloneqq\sum\limits_{j=i+1}^{n}a_{ij}x_{j}^{\left(k\right)}$
    n = len(x_old)
    result = 0
    for j in range(i, n):
        result += A[i][j] * x_old[j]

    return result


def sor(A, b, omega, epsilon=1e-5, max_iterations=1000):
    # Calcula $x_{i}^{\left(k+1\right)}=\frac{w}{a_{ii}}\left(b_{i}-\operatorname{Left}-\operatorname{Right}\right)+\left(1-w\right)x_{i}^{\left(k\right)}$
    size = len(A)
    x_old = np.zeros(size)
    x_new = np.zeros(size)
    for k in range(max_iterations):
        x_old = x_new.copy()

        for i in range(size):
            x_new[i] = (omega / A[i][i]) * (
                b[i] - sor_left_sum(A, x_new, i) - sor_right_sum(A, x_old, i)
            ) + (1 - omega) * x_old[i]

        if np.sqrt(np.dot(x_old - x_new, x_old - x_new)) < epsilon:
            print("Converged after ", k, " steps")
            break

    return x_new


omega = 1.25
T_w = np.linalg.inv(D - omega * L) @ ((1 - omega) * D + omega * U)
print(f"T_w = \n{T_w}\n")
c_w = omega * np.linalg.inv(D - omega * L) @ b
print(f"c_w = \n{c_w}\n")
print(
    f"El radio espectral de T_w es menor que 1: {np.all(np.absolute(np.linalg.eigvals(T_w)) < 1)}"
)  # \rho(T_w) menor que 1
# from descensorapido import maximo_descenso

x_0 = np.ones(6)
print(f"x_0 = \n{x_0}\n")
for w in np.linspace(0 + 0.1, 2 - 0.1, 20):
    x = sor(A=A, b=b, omega=w)
    print(x)
# print(x)
# xk = maximo_descenso(A, b, x0.T, 1e-5, 200)
# x = np.linalg.solve(A, b)
# print(x)
# print(f"Verificacion: A x = \n{A @ x}")
# print(f"Verificacion: b = \n{b}")
# print(f"La solución es \n{np.linalg.solve(A, b)}")
# r_0 = b - A @ x0
# print(f"b - A * x0= \n{r_0}")
# alpha_0 = np.round(np.dot(r_0.T, r_0) / (r_0.T @ A @ r_0), 3)
# print(alpha_0)

# x_1 = x0 + alpha_0 * r_0
# print(x_1)


# def plot_sor_error():
#     import matplotlib.pyplot as plt

#     x = np.linspace(start=1, stop=20)
#     y = np.sin(x)
#     plt.plot(x, y)
#     plt.savefig("sor_error.png")


# plot_sor_error()

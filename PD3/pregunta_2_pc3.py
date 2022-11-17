#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Copyright (C) 2022 Carlos Aznarán <caznaranl@uni.pe>


# This file is part of https://github.com/carlosal1015/Analysis-and-Numerical-Modeling-I .
# https://github.com/carlosal1015/Analysis-and-Numerical-Modeling-I is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

# https://github.com/carlosal1015/Analysis-and-Numerical-Modeling-I is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with https://github.com/carlosal1015/Analysis-and-Numerical-Modeling-I .  If not, see <http://www.gnu.org/licenses/>.


import numpy as np
from numpy.linalg import eig, solve, cholesky

def is_pos_def(A):
    """Retorna verdadero si la matriz A es definida positiva"""
    return np.all(np.linalg.eigvals(A) > 0)


def LDLt(A, n):
    """Descompone una matriz simétrica A de orden nxn en el tipo LDLt."""
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


def choleskyllt(A):
    if not is_pos_def(A):
        return 0
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


A = np.array(
    [
        [4, -1, 0, -1, 0, 0],
        [-1, 4, -1, 0, -1, 0],
        [0, -1, 4, 0, 0, -1],
        [-1, 0, 0, 4, -1, 0],
        [0, -1, 0, -1, 4, -1],
        [0, 0, -1, 0, -1, 4],
    ],
    dtype=float,
)

b = np.array([56, 25, 62, 41, 10, 47])


eigenvalues, _ = eig(A)

print(eigenvalues)

print(is_pos_def(A))

print("Factorización LDLt :")
print(A)
L, D, Lt = LDLt(A, 6)
print("Matriz L: ")
print(L)
print("Matriz D:")
print(D)
print("Matriz Lt:")
print(Lt)

X = solve(A, b)
print(f"X = {X}")

l1_ = choleskyllt(A)
l1 = cholesky(A)
print(l1_)
print(l1)


def sustiProg(M, n):
    x = np.zeros((n, 1))
    for i in range(n):
        aux = 0
        for j in range(i):
            aux += M[i, j] * x[j, 0]
        x[i, 0] = (M[i, n] - aux) / M[i, i]
    return x


def sustiReg(M, n):
    x = np.zeros((n, 1))
    x[n - 1, 0] = M[n - 1, n] / M[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        aux = 0
        for j in range(i + 1, n):
            aux += M[i, j] * x[j]
        x[i, 0] = (M[i, n] - aux) / M[i, i]
    return x


def chol(a):
    a = np.array(a, float)
    L = np.zeros_like(a)
    n, _ = np.shape(a)
    for j in range(n):
        for i in range(j, n):
            if i == j:
                sumk = 0
                for k in range(j):
                    sumk += L[i, k] ** 2
                L[i, j] = np.sqrt(a[i, j] - sumk)
                print("L:\n", L)
                print("------------------")
            else:
                sumk = 0
                for k in range(j):
                    sumk += L[i, k] * L[j, k]
                L[i, j] = (a[i, j] - sumk) / L[j, j]
                print("L:\n", L)
                print("------------------")
    return L


def resolver_sistema():
    L = chol(A)
    print("L:")
    print(L)
    print("--------------------")
    print("Soluciones (b):")
    LT = np.transpose(L)
    SL = np.append(L, b, axis=1)
    print("--------------------")
    print("Sistema Lz=b")
    print(SL)
    print("--------------------")
    z = sustiProg(SL, np.shape(SL)[0])
    SLT = np.append(LT, z, axis=1)
    print("Sistema (LT)x=z\n", SLT)
    print("--------------------")
    x = sustiReg(SLT, np.shape(SLT)[0])
    print("x:\n", x)
    print("--------------------")


# resolver_sistema()
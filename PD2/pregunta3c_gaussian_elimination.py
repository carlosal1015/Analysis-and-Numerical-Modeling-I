#!/usr/bin/env -S python pregunta3c_gaussian_elimination.py -v

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
from numpy.linalg import solve

"""Modelamiento matemático
|                  |  Arequipa   |     Cusco     |  Ayacucho  |    Puno     | Total  |
| :--------------- | :---------: | :-----------: | :--------: | :---------: | :----- |
| Pago por noche   | $120 x_{1}$ |  $200 x_{2}$  | $80 x_{3}$ | $100 x_{4}$ | $2020$ |
| Número de noches |   $x_{1}$   |    $x_{2}$    |  $x_{3}$   |   $x_{4}$   | $14$   |
| Relación de días |   $x_{1}$   | $x_{1}+x_{4}$ |     -      |   $x_{4}$   | -      |
| Relación de días |      -      |   $3x_{3}$    |  $x_{3}$   |      -      | -      |
"""


def RowSwap(A, k, l):
    """rows k and l swapped"""
    m = A.shape[0]  # m is number of rows in A
    n = A.shape[1]  # n is number of columns in A

    B = np.copy(A).astype("float64")

    for j in range(n):
        temp = B[k][j]
        B[k][j] = B[l][j]
        B[l][j] = temp

    return B


def RowScale(A, k, scale):
    """the entries of row k multiplied by scale"""
    m = A.shape[0]  # m is number of rows in A
    n = A.shape[1]  # n is number of columns in A

    B = np.copy(A).astype("float64")

    for j in range(n):
        B[k][j] *= scale

    return B


def RowAdd(A, k, l, scale):
    """row l added to the values of row k, multiplied by scale"""
    m = A.shape[0]  # m is number of rows in A
    n = A.shape[1]  # n is number of columns in A

    B = np.copy(A).astype("float64")

    for j in range(n):
        B[l][j] += B[k][j] * scale

    return B


np.set_printoptions(precision=3)
A = np.array([[120, 200, 80, 100], [1, 1, 1, 1], [1, -1, 0, 1], [0, 1, -3, 0]])
b = np.array([2020, 14, 0, 0])
Augmented = np.column_stack((A, b))
# Show the augmented matrix
print(Augmented, "\n")

# Divide the first row by 120
Augmented = RowScale(Augmented, 0, 1.0 / 120)
print(Augmented, "\n")


# multiply 1 row by 1 and subtract it from 2 row
Augmented = RowAdd(Augmented, 0, 1, -1)
print(Augmented, "\n")

# multiply 1 row by 1 and subtract it from 3 row
Augmented = RowAdd(Augmented, 0, 2, -1)
print(Augmented, "\n")

# divide the 2 row by -2/3
Augmented = RowScale(Augmented, 1, 1.0 / (-2.0 / 3.0))
print(Augmented, "\n")

# multiply 2 row by 5/3 and subtract it from 1 row
Augmented = RowAdd(Augmented, 1, 0, -5.0 / 3.0)
print(Augmented, "\n")

# multiply 2 row by 8/3 and add it to 3 row
Augmented = RowAdd(Augmented, 1, 2, 8.0 / 3.0)
print(Augmented, "\n")

# multiply 2 row by 1 and subtract it from 4 row
Augmented = RowAdd(Augmented, 1, 3, -1.0)
print(Augmented, "\n")

# divide the 3 row by -2
Augmented = RowScale(Augmented, 2, 1.0 / -2.0)
print(Augmented, "\n")

# multiply 3 row by 1.5 and subtract it from 1 row
Augmented = RowAdd(Augmented, 2, 0, -1.5)
print(Augmented, "\n")

# multiply 3 row by 0.5 and add it to 2 row
Augmented = RowAdd(Augmented, 2, 1, 0.5)
print(Augmented, "\n")

# multiply 3 row by 2.5 and add it to 4 row
Augmented = RowAdd(Augmented, 2, 3, 2.5)
print(Augmented, "\n")

# divide the 4 row by 0.875
Augmented = RowScale(Augmented, 3, 1.0 / 0.875)
print(Augmented, "\n")

# multiply 4 row by 0.875 and subtract it from 1 row
Augmented = RowAdd(Augmented, 3, 0, -0.875)
print(Augmented, "\n")

# multiply 4 row by 0.125 and add it to 2 row
Augmented = RowAdd(Augmented, 3, 1, 0.125)
print(Augmented, "\n")
# multiply 4 row by 0.25 and subtract it from 3 row
Augmented = RowAdd(Augmented, 3, 2, -0.25)
print(Augmented, "\n")


def BackSubstitution(U, B):
    m = U.shape[0]  # m is number of rows and columns in U
    X = np.zeros((m, 1))

    for i in range(m - 1, -1, -1):  # Calculate entries of X backward from m-1 to 0
        X[i] = B[i]
        for j in range(i + 1, m):
            X[i] -= U[i][j] * X[j]
        if U[i][i] != 0:
            X[i] /= U[i][i]
        else:
            print("Zero entry found in U pivot position", i, ".")
    return X


print("A=", Augmented[:, :-1], sep="\n")
print("b=", Augmented[:, -1], sep="\n")
print(
    "Solution by gauss elimination",
    BackSubstitution(Augmented[:, :-1], Augmented[:, -1]),
    sep="\n",
)

print("Verificación solución:", solve(A, b), sep="\n")

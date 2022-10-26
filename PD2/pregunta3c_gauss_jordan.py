#!/usr/bin/env -S python pregunta3c_gauss_jordan.py -v

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


import numpy as np
import sys


def Gauss_Jordan(A, b):
    M = A.copy()
    n = len(b)
    x = np.zeros(n)

    for i in range(len(b)):
        M[i].insert(len(b) + 1, b[i][0])

    print("Augmented matriz:")
    print(
        "\n".join(["\t\t\t".join(["{:4}".format(item) for item in row]) for row in M])
    )

    for i in range(n):
        if abs(M[i][i]) < 1e-6:
            # division by zero
            raise ZeroDivisionError
        for j in range(n):
            if i != j:
                ratio = M[j][i] / M[i][i]

                for k in range(n + 1):
                    M[j][k] = M[j][k] - ratio * M[i][k]
    print("\nMatrix after:")
    print(
        "\n".join(["\t\t\t".join(["{:2}".format(item) for item in row]) for row in M])
    )

    # Solution
    for i in range(n):
        x[i] = M[i][n] / M[i][i]

    print("\nMatrix solution: ")
    for i in range(n):
        print("X%d = %0.2f" % (i, x[i]), end="\t")


# inputs
A = [
    [120, 200, 80, 100],
    [1, 1, 1, 1],
    [1, -1, 0, 1],
    [0, 1, -3, 0],
]
b = [[2020], [14], [0], [0]]
Gauss_Jordan(A, b)

# (d) Indique que método da un mejor resultado.
# Se prefiere la eliminacion gaussiana sobre gauss jordan,
# ya que en Gauss Jordan nos da una forma de invertir la matriz,
# lo cual en general es más costoso.
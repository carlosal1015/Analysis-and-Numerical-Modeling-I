#!/usr/bin/env -S python pregunta1c.py -v

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
from numpy.linalg import cond, inv, norm, solve
from numpy.testing import assert_allclose

"""
Ejemplo en Python que ilustra el número de condición en un sistema lineal 2x2.
https://blogs.mathworks.com/cleve/2017/07/17/what-is-the-condition-number-of-a-matrix
"""


def condition_number(
    square_matrix: np.ndarray = np.eye(2, dtype=int),
    matrix_norm: float = 2,
    precision: int = 2,
):
    """Calculate the number of condition from a square matrix.
    >>> condition_number([[4.1, 2.8], [9.7, 6.6]])
    1622.9993838568262
    >>> condition_number()
    1.0
    """
    np.set_printoptions(precision=precision, suppress=False)
    square_matrix_inverse = inv(square_matrix)
    square_matrix_norm = norm(x=square_matrix, ord=matrix_norm)
    square_matrix_inverse_norm = norm(x=square_matrix_inverse, ord=matrix_norm)
    return square_matrix_norm * square_matrix_inverse_norm


if __name__ == "__main__":
    import doctest

    doctest.testmod()

A = np.array(object=[[4.1, 2.8], [9.7, 6.6]])
b = A[:, 0]
x = solve(a=A, b=b)
print("Solution:", x)
b2 = np.array(object=[4.11, 9.7])
x2 = solve(a=A, b=b2)
print("Solution:", x2)

print("Condition number of A:", condition_number(A))
assert_allclose(actual=condition_number(A), desired=cond(A))
print(
    "Upper bound on the possible change in x:",
    condition_number(A) * norm(b - b2) / norm(b),
)
print("Actual change in x:", norm(x - x2) / norm(x))
A2 = np.array([[4.1, 2.8], [9.676, 6.608]])
np.set_printoptions(precision=3)
print("A=", A, sep="\n")
print("A2=", A2, sep="\n")
A2inv = inv(A2)
print("A2inv=", A2inv, sep="\n")
print(1 / cond(A2inv))
print("Epsilon machine:", np.finfo(np.float64).eps)

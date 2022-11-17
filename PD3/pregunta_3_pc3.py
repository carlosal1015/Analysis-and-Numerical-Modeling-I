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


"""Descomposición de valores singulares para la matriz A.
"""

import numpy as np
from numpy.linalg import svd

A = np.array([[4, 11, 14], [8, 7, -2]])
U, S, V = svd(a=A)
S = np.diag(S)
print(f"Matriz A es\n{A} de tamaño {A.shape}\n")
print(f"Matriz U es\n{A} de tamaño {U.shape}\n")
print(f"Matriz S es\n{S} de tamaño {S.shape}\n")
print(f"Matriz V es\n{S} de tamaño {V.shape}\n")

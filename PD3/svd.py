#!/usr/bin/env python
from numpy.linalg import svd
import numpy as np

A = np.array([[0, 1, 0, 0], [0, 0, 2, 0], [0, 0, 0, 3], [0, 0, 0, 0]])
print(f"A = {A}", sep="")

U, S, V = svd(a=A)

print(f"U = {U.T}", sep="")
print(f"S = {S}", sep="")
print(f"V = {V}", sep="")
print(f"A = {U @ S @ V}", sep="")

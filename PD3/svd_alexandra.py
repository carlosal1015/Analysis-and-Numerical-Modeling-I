#!/usr/bin/env python
from numpy import array
from scipy.linalg import svd

# define a matrix
A = array(object=[[0, 1, 0, 0], [0, 0, 2, 0], [0, 0, 0, 3], [0, 0, 0, 0]])
print(f"A = {A}")
# singular value decomposition
U, s, VT = svd(a=A)
print(f"U = {U}")
print(f"s = {s}")
print(f"VT = {VT}")

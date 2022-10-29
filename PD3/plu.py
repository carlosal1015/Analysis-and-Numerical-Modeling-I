#!/usr/bin/env python
from scipy.linalg import lu
import numpy as np


A = np.array([[2, 2, 1], [1, 1, 1], [3, 2, 1]])
p, l, u = lu(A)

print(f"p = {p}", sep="")
print(f"l = {l}", sep="")
print(f"u = {u}", sep="")

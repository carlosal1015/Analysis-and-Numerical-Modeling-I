#!/usr/bin/env python
import numpy as np
from numpy.linalg import solve, eig

A = np.array([[4, 1, 2], [3, 1, 4], [5, 1, 3]])
b = np.array([40, 53, 51])
X = solve(A, b)
print("A.T=", A.T)
print("A=", A)
A_new = A.T @ A
print("A.T*A=", A_new)
eigenvalues, _ = eig(A_new)
print(eigenvalues)
b_new = A.T @ b
print("A.T*b=", b_new)
# print(np.shape(A.T), np.shape(b))
# print(b.T * A)
# X_new = solve(A_new, b_new)
# print(f"X={X}")
# print(X)
# print(X_new)

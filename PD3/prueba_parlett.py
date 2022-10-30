import numpy as np

P = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

A = np.array([[1, 1, 0], [1, 1, 0], [0, 0, 0]])

T = A.copy()

L = np.array([[1, 0, 0], [0, 1, 0], [0, 1, 1]])

print(P.T @ A @ P)

print(L @ T @ L.T)

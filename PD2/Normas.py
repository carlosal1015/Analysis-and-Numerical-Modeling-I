import numpy as np
from numpy import linalg as LA

b = np.array([[1, 2, 4], [4, 4, 1], [2, 3, 4]])
print(b)
# Frobenius
Nf = LA.norm(b, "fro")
print("\nLa norma frobenius es: ", Nf)
# Inf -> derecha
print("La norma Inf es: ", LA.norm(b, np.inf))
# 1 ->up
print("La norma 1 es: ", LA.norm(b, 1))

import numpy as np
from numpy.linalg import inv
from numpy import linalg as LA

a = np.array([[1, 2, 4], [4, 4, 1], [2, 3, 4]])

ai = inv(np.matrix(a))

print(ai)

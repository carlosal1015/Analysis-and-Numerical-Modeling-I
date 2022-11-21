# /usr/bin/env python

import numpy as np

A = np.array(object=[[3, -2], [0, 3], [4, 4]], dtype=np.float64)
b = np.array(object=[[3, 5, 4]], dtype=np.float64)

v_1 = A[:, 0]
v_2 = A[:, 1]

u_1 = v_1
q_1 = u_1 / np.linalg.norm(x=u_1, ord=2)
print(f"q_{1} = {q_1}\n")

u_2 = v_2 - np.dot(q_1, v_2) * q_1
q_2 = u_2 / np.linalg.norm(x=u_2, ord=2)
print(f"q_{2} = {q_2}\n")

Q = np.stack(arrays=(q_1, q_2), axis=-1)
print(f"Q = \n{Q}\n")
R = Q.T @ A
print(f"R = \n{R}\n")

print(f"Qb \n= {Q.T @ b.T}\n")

Q, R = np.linalg.qr(A)
print(f"Verificación con numpy.linalg.qr:\n Q = \n{-Q}\nR = \n{-R}\n")

overline_x = np.linalg.solve(R, Q.T @ b.T)
print(f"overline_x \n= {overline_x}\n")
minimum = np.linalg.norm(x=A @ overline_x - b, ord=2)
print(f"El mínimo es {minimum}\n")

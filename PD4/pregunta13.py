import numpy as np


def a(i, j):
    if j == 0:
        return 4
    elif (
        (j == i + 1 and i % 5 != 4)
        or (j == i - 1 and i % 5 != 0)
        or (j == i + 5 and i < 20)
        or (j == i - 5 and 4 < i < 25)
    ):
        return -1
    else:
        return 0


A = np.fromfunction(function=np.vectorize(a), shape=(25, 25), dtype=np.float64)
b = np.array(
    object=[
        1,
        0,
        -1,
        0,
        2,
        1,
        0,
        -1,
        0,
        2,
        1,
        0,
        -1,
        0,
        2,
        1,
        0,
        -1,
        0,
        2,
        1,
        0,
        -1,
        0,
        2,
    ],
    dtype=np.float64,
).T


if __name__ == "__main__":
    print(f"A = \n{A}\n")
    (i, j) = (5, 1)
    print(f"a{i}{j} = ", A[i - 1][j - 1])
    from pregunta11 import is_symmetric, is_positive_definite

    print(f"La matriz A es definida positiva: {is_positive_definite(A)}.\n")
    print(f"La matriz A es simétrica: {is_symmetric(A)}.\n")
    A_tilde = A.T @ A
    b_tile = A.T @ b.T
    print(f"La matriz A_tilde es definida positiva: {is_positive_definite(A_tilde)}.\n")
    print(f"La matriz A_tilde es simétrica: {is_symmetric(A_tilde)}.\n")

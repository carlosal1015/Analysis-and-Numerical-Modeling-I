import numpy as np


def a(i, j):
    if j == 0:
        return 4
    elif (
        (j == i + 1 and i % 4 != 3)
        or (j == i - 1 and i % 4 != 0)
        or (j == i + 4 and i < 12)
        or (j == i - 4 and 3 < i < 16)
    ):
        return -1
    else:
        return 0


A = np.fromfunction(function=np.vectorize(a), shape=(16, 16), dtype=np.float64)
b = np.array(
    object=[
        1.902207,
        1.051143,
        1.175689,
        3.480083,
        0.819600,
        -0.264419,
        -0.412789,
        1.175689,
        0.913337,
        -0.150209,
        -0.264419,
        1.051143,
        1.966694,
        0.913337,
        0.819600,
        1.902207,
    ],
    dtype=np.float64,
)
x0 = np.zeros(16, dtype=np.float64)


if __name__ == "__main__":
    print(f"A = \n{A}\n")
    from pregunta11 import (
        is_symmetric,
        is_positive_definite,
        diagonal,
        lower_inferior,
        upper_superior,
    )

    print(f"La matriz A es definida positiva: {is_positive_definite(A)}.\n")
    print(f"La matriz A es simétrica: {is_symmetric(A)}.\n")
    A_tilde = A.T @ A
    b_tilde = A.T @ b.T
    D = diagonal(A_tilde)
    L = lower_inferior(A_tilde)
    U = upper_superior(A_tilde)
    print(f"A_tilde = \n{D - L - U}\n")
    print(f"D = \n{D}\n")
    print(f"L = \n{L}\n")
    print(f"U = \n{U}\n")
    print(f"La matriz A_tilde es definida positiva: {is_positive_definite(A_tilde)}.\n")
    print(f"La matriz A_tilde es simétrica: {is_symmetric(A_tilde)}.\n")
    from descensorapido import maximo_descenso

    xk = maximo_descenso(A_tilde, b_tilde, x0, 0.0001, 2000)
    # print(np.linalg.solve(A_tilde, b_tilde))
# https://stackoverflow.com/a/24900335
# https://stackoverflow.com/a/16964006

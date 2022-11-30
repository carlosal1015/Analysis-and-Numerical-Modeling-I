import numpy as np
from scipy.sparse.linalg import cg


np.set_printoptions(suppress=True, formatter={"float_kind": "{:.2f}".format})

A = np.array(
    object=[
        [
            15000,
            20000,
            30000,
        ],
        [
            10000,
            15000,
            20000,
        ],
        [
            1,
            1,
            1,
        ],
    ],
    dtype=np.float64,
)
b = np.array(
    object=[
        [
            250000,
            175000,
            140,
        ]
    ],
    dtype=np.float64,
)

if __name__ == "__main__":
    print(f"A = \n{A}\n")
    from pregunta11 import is_positive_definite, is_symmetric

    A_tilde = A.T @ A
    b_tilde = A.T @ b.T
    print(f"¿A_tilde es definida positiva? {is_positive_definite(A_tilde)}.\n")
    print(f"¿A_tilde es simétrica? {is_symmetric(A_tilde)}.\n")
    print(A[2][2])
    print(f"A_tilde = \n{A_tilde}\n")
    print(f"b_tilde = \n{b_tilde}\n")
    x, exit_code = cg(A_tilde, b_tilde)
    print(f"Solución por el método del gradiente conjugado: {x}\n")
    # print(np.linalg.solve(A, b.T))
    # print(np.linalg.solve(A_tilde, b_tilde))

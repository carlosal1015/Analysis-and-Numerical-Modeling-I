import pprint
import numpy as np


def pivot_matrix(M):
    """Returns the pivoting matrix for M, used in Doolittle's method."""
    m = len(M)

    # Create an identity matrix, with floating point values
    id_mat = [[float(i == j) for i in list(range(m))] for j in list(range(m))]

    # Rearrange the identity matrix such that the largest element of
    # each column of M is placed on the diagonal of of M
    for j in list(range(m)):
        row = max(list(range(j, m)), key=lambda i: abs(M[i][j]))
        if j != row:
            # Swap the rows
            id_mat[j], id_mat[row] = id_mat[row], id_mat[j]

    return id_mat


def lu_decomposition(A):
    """Performs an LU Decomposition of A (which must be square)
    into PA = LU. The function returns P, L and U."""
    n = len(A)

    # Create zero matrices for L and U
    L = [[0.0] * n for i in list(range(n))]
    U = [[0.0] * n for i in list(range(n))]

    # Create the pivot matrix P and the multipled matrix PA
    P = pivot_matrix(A)
    PA = np.dot(P, A)

    # Perform the LU Decomposition
    for j in list(range(n)):
        # All diagonal entries of L are set to unity
        L[j][j] = 1.0

        # LaTeX: u_{ij} = a_{ij} - \sum_{k=1}^{i-1} u_{kj} l_{ik}
        for i in list(range(j + 1)):
            s1 = sum(U[k][j] * L[i][k] for k in list(range(i)))
            U[i][j] = PA[i][j] - s1

        # LaTeX: l_{ij} = \frac{1}{u_{jj}} (a_{ij} - \sum_{k=1}^{j-1} u_{kj} l_{ik} )
        for i in list(range(j, n)):
            s2 = sum(U[k][j] * L[i][k] for k in list(range(j)))
            L[i][j] = (PA[i][j] - s2) / U[j][j]

    return (P, L, U)


A = [[2, 2, 1], [1, 1, 1], [3, 2, 1]]
P, L, U = lu_decomposition(A)

print("A:")
pprint.pprint(A)

print("P:")
pprint.pprint(P)

print("L:")
pprint.pprint(L)

print("U:")
pprint.pprint(U)

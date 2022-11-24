A = np.array(object=[[2, 2, 4, 18], [1, 3, -2, 1], [3, 1, 3, 14]], dtype=np.float64)


e_1 = np.zeros(A.shape[0])
e_1[0] = 1.0


v_1 = A[:, 0] + np.sign(A[0][0]) * np.linalg.norm(x=A[:, 0], ord=2) * e_1

print(np.linalg.solve(R, Q.T @ b.T))

# Args:
#         A (float): matriz A.

#     Returns:
#         D (float): matriz diagonal de A.

# Args:
#     A (float): matriz A.

# Returns:
#     E (float): matriz triangular inferior sin contar la diagonal de A.

# Args:
#     A (float): matriz A.

# Returns:
#     F (float): matriz triangular superior sin contar la diagonal de A.

A = np.empty(shape=(16, 16), dtype=np.float64)


def diagonal(A):
    """Retorna la matriz diagonal de A."""
    D = np.diag(np.diag(A))
    return D


def lower_inferior(A):
    """Retorna la matriz estrictamente triangular inferior de -A."""
    E = np.zeros_like(A)
    n = len(A)
    for k in range(n):
        E[k, :k] = -A[k, :k]
    return E


def upper_superior(A):
    """Retorna la matriz estrictamente triangular superior de -A."""
    return diagonal(A) - lower_inferior(A) - A


def is_positive_definite(A):
    """Retorna verdadero si la matriz A es definida positiva."""
    return np.all(np.linalg.eigvals(A) > 0)


def is_symmetric(A, rtol=1e-5, atol=1e-8):
    """Retorna verdadero si la matriz A es simétrica."""
    return np.allclose(A, A.T, rtol=rtol, atol=atol)

    # print(f"Triangular superior:\n{-np.triu(A, 1)}\n")
    # print(f"Triangular inferior:\n{-np.tril(A, -1)}\n")


(i, j) = (5, 1)
print(f"a{i}{j} = ", A[i - 1][j - 1])

# A = np.array([[3, 4, 6], [2, 3, 4], [1, 1, 1]])
# b = np.array([[50, 35, 140]])
# print(A.T - A)
# print(f"A = \n{A}")
# print(f"b = \n{b}")
# print(f"x = \n{x}")
# from gradienteconjugado import gradienteConjugada, imprimirResultados
# import pandas as pd
# from tabulate import tabulate
# x0 = np.zeros(3)
# iteraciones = 10
# gradienteConjugada(A, b.T, x0, iteraciones)
# resultados = {"alphak": [], "rk": [], "betak": [], "pk": [], "xk": []}
# imprimirResultados(resultados)
# x, exit_code = cg(A, b.T, maxiter=1000000)

# print(f"¿A es definida positiva? {is_positive_definite(A)}.\n")
# print(f"¿A es simétrica? {is_symmetric(A)}.\n")
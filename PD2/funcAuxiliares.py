import numpy as np


def readLinearEqSystem(fileA, fileb):
    with open(fileA, mode="r") as A, open(fileb, mode="r") as b:
        A = np.array(
            [[float(Aij) for Aij in Ai.split()] for Ai in A.read().split("\n")]
        )
        b = np.array([[float(bi)] for bi in b.read().split("\n")])
    return A, b


def elementalOp1(M, i, j):
    M[[i, j]] = M[[j, i]]


def elementalOp2(M, i, k):
    if k != 0:
        M[i, :] = [k * element for element in M[i, :]]


def elementalOp3(M, i, j, k):
    if k != 0:
        M[i, :] = [el_i + k * el_j for el_i, el_j in zip(M[i, :], M[j, :])]


def elementalOpC1(M, i, j):
    M[:, [i, j]] = M[:, [j, i]]


def elementalOpC2(M, i, k):
    if k != 0:
        M[:, i] = [k * element for element in M[:, i]]


def elementalOpC3(M, i, j, k):
    if k != 0:
        M[:, i] = [el_i + k * el_j for el_i, el_j in zip(M[:, i], M[:, j])]


def dot(v1, v2):
    return float(np.sum(v1 * v2))


def matAumentada(M, b):
    return np.hstack((M, b))


def matIdentidad(n):
    I = np.zeros((n, n))
    for i in range(n):
        I[i, i] = 1
    return I


def matDiagonal(M):
    n = M.shape[0]
    D = matIdentidad(n)
    for i in range(n):
        D[i, i] = M[i, i]
    return D


def matL(M):
    n = M.shape[0]
    L = np.copy(M)
    for i in range(n - 1):
        for j in range(i + 1, n):
            L[i, j] = 0
    return L


def inversaDiag(M):
    n = M.shape[0]
    D = np.copy(M).astype(float)
    for i in range(n):
        D[i, i] = 1.0 / M[i, i]
    return D


def inversaL(M):
    n = M.shape[0]
    I = inversaDiag(matDiagonal(M))
    for j in range(n - 1):
        for i in range(j + 1, n):
            for k in range(j, i):
                I[i, j] -= M[i, k] * I[k, j]
            I[i, j] /= M[i, i]
    return I


def determinanteTriang(A):
    n = A.shape[0]
    det = 1
    for i in range(n):
        det *= A[i, i]
    return det


# ---------------------------------------------------------------------- 2021.2

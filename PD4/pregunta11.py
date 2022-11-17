#!/usr/bin/env python


# -*- coding: utf-8 -*-

import numpy as np


def get_D(A):
    """Retorna una matriz diagonal

    Args:
        A (float): matriz A.

    Returns:
        D (float): matriz diagonal de A.
    """
    D = np.diag(np.diag(A))
    return D


def get_E(A):
    """Retorna el -E

    Args:
        A (float): matriz A.

    Returns:
        E (float): matriz triangular inferior sin contar la diagonal de A.
    """
    E = np.zeros_like(A)
    n = np.shape(A)[0]
    for k in range(n):
        E[k, :k] = A[k, :k]
    return E


def get_F(A):
    """Retorna el -F

    Args:
        A (float): matriz A.

    Returns:
        F (float): matriz triangular superior sin contar la diagonal de A.
    """
    return get_D(A) - get_E(A) - A


A = np.array(
    object=[
        [4, -1, 0, -1, 0, 0],
        [-1, 4, -1, 0, -1, 0],
        [0, -1, 4, 0, 0, -1],
        [-1, 0, 0, 4, -1, 0],
        [0, -1, 0, -1, 4, -1],
        [0, 0, -1, 0, -1, 4],
    ],
    dtype=np.float64,
)

b = np.array(object=[0, 5, 0, 6, -2, 6], dtype=np.float64).T
D = get_D(A)
E = get_E(A)
F = get_F(A)

if __name__ == "__main__":
    print(A)
    print(D + E + F)

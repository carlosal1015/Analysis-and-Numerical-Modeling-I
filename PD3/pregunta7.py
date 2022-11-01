#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from numpy.linalg import solve


if __name__ == "__main__":
    A = np.array([[50, 12, 35], [12, 3, 9], [35, 9, 29]])
    b = np.array([574, 144, 445])
    X = solve(A, b)
    L = np.array([[1, 0, 0], [12 / 50, 1, 0], [35 / 50, 5, 1]])
    D = np.array([[50, 0, 0], [0, 6 / 50, 0], [0, 0, 75 / 50]])
    L_cholesky = np.array(
        [
            [5 * np.sqrt(2), 0, 0],
            [12 / (5 * np.sqrt(2)), (np.sqrt(6)) / (5 * np.sqrt(2)), 0],
            [35 / (5 * np.sqrt(2)), 6 / np.sqrt(12), np.sqrt(15) / np.sqrt(10)],
        ]
    )
    print(f"A = {A}\nb = {b}\nX={X}\n")
    print(f"LDL'= {L @ D @ L.T}")
    print(f"LL'= {L_cholesky @ L_cholesky.T}")

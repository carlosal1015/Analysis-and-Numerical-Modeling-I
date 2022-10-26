#!/usr/bin/env python
# -*- coding: utf-8 -*-


def aitken(loop=6, A=[3 / 2, 5 / 3], B=[0] * 10):
    for n in range(loop):
        div = A[0] * A[1]
        sgtvalor = 2003 - (6002 / A[1]) + 4000 / div
        B[n] = (A[0] * sgtvalor - A[1] ** 2) / (sgtvalor - 2 * A[1] + A[0])
        A[0] = A[1]
        A[1] = sgtvalor
        print(n, "\t", A[0], "\t", B[n])

    pass


if __name__ == "__main__":
    aitken()

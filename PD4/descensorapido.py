#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""DescensoRapido.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x5s46__6mTij2KROAdNdLR3z35kZIeCe
"""

"""
Created on Mon Nov  1 16:20:52 2021

@author: ....
"""

import numpy as np
import scipy.linalg as sl
import pandas as pd
from tabulate import tabulate

tabla = {"x": [], "p": [], "error": []}

np.set_printoptions(precision=2, suppress=False)


def maximo_descenso(A, b, x0, error, iteracciones):

    xk = x0
    tabla["x"].append(xk.flatten())
    tabla["p"].append("---")
    tabla["error"].append("---")

    for i in range(iteracciones):

        dk = b - np.dot(A, xk)  # $b-Ax^{\left(k\right)}$
        dkt = np.transpose(dk)  # ${r^{\left(k\right)}}^{T}$
        Adk = np.dot(A, dk)  # $A{r^{\left(k\right)}}^{T}$
        pk = np.dot(dkt, dk) / np.dot(dkt, Adk)
        # $\frac{{r^{\left(k\right)}}^{T}r^{\left(k\right)}}{{r^{\left(k\right)}}^{T}Ar^{\left(k\right)}}$
        xk1 = xk + pk * dk  # $x^{\left(k\right)} + \alpha_{k}r^{\left(k\right)}$
        comp = sl.norm(xk1 - xk, ord=np.inf) / sl.norm(xk1, ord=np.inf)
        # $\frac{\left\|x^{\left(k+1\right)}-x^{\left(k\right)}\right\|}{\left\|x^{\left(k+1\right)}\right\|}$
        tabla["x"].append(xk.flatten())
        tabla["error"].append(np.round(comp, 5))
        tabla["p"].append(dk.flatten())
        if comp < error:
            df = pd.DataFrame(tabla)
            print(tabulate(df, headers="keys", tablefmt="psql"))
            return xk1
        xk = xk1
    df = pd.DataFrame(tabla)
    print(tabulate(df, headers="keys", tablefmt="psql"))
    return xk


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
b = np.array(object=[0, 5, 0, 6, -2, 6], dtype=np.float64)
x0 = np.zeros(6, dtype=np.float64)

if __name__ == "__main__":
    # A = np.array([[4, 1, 2], [3, 1, 4], [5, 1, 3]], float)
    # b = np.array([[40], [53], [51]], float)
    # x0 = np.array([[0], [0], [0]], float)
    xk = maximo_descenso(A, b.T, x0, 0.0001, 2000)
    # print(xk)
    # print("Comprobación")
    # print(f"{A @ xk} = {b}")

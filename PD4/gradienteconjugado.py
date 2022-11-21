import numpy as np
import pandas as pd
from tabulate import tabulate

np.set_printoptions(suppress=True, formatter={"float_kind": "{:f}".format})

resultados = {"alphak": [], "rk": [], "betak": [], "pk": [], "xk": []}


def imprimirResultados(resultados):
    df = pd.DataFrame(resultados)
    print(tabulate(df, headers="keys", tablefmt="psql"))


def gradienteConjugada(A, b, x0, iteraciones):
    # k=0
    pk = b - np.dot(A, x0)
    rk = b - np.dot(A, x0)
    xk = x0

    resultados["xk"].append(xk.flatten())
    resultados["pk"].append(pk.flatten())
    resultados["rk"].append(rk.flatten())

    for i in range(iteraciones - 1):
        rkt = np.round(np.transpose(rk), 3)
        pkt = np.round(np.transpose(pk), 3)
        Apk = np.round(np.dot(A, pk), 3)

        alphak = np.dot(rkt, pk) / np.dot(pkt, Apk)
        xk1 = xk + alphak * pk
        rk1 = rk - alphak * Apk
        Ark1 = np.dot(A, rk1)
        betak = -np.dot(pkt, Ark1) / np.dot(pkt, Apk)
        pk1 = rk1 + betak * pk

        pk = pk1
        rk = rk1
        xk = xk1

        resultados["alphak"].append(alphak)
        resultados["xk"].append(xk1.flatten())
        resultados["rk"].append(rk1.flatten())
        resultados["betak"].append(betak)
        resultados["pk"].append(pk1.flatten())

    resultados["alphak"].append("----")
    resultados["betak"].append("----")


# A = np.array([[4, 3, 0], [3, 4, -1], [0, -1, 4]], float)


# # A = np.array([
# #    [0.3,0.2],
# #    [0.2,99]
# # ],float)
# # b = np.array([
# #    [0.5],
# #    [99.2]
# # ], float)


# b = np.array([[24], [30], [-24]], float)
# # x0 = np.array([
# #    [0],
# #    [0]
# # ], float)


# x0 = np.array([[0], [0], [0]], float)
# #iteraciones = 3

# iteraciones = 4
# gradienteConjugada(A, b, x0, iteraciones)
# imprimirResultados(resultados)

A = np.array([[3, 4, 6], [2, 3, 4], [1, 1, 1]])
b = np.array([[50, 35, 140]])
iteraciones = 100
x0 = np.array([[0], [0], [0]], float)
gradienteConjugada(A, b, x0, iteraciones)
imprimirResultados(resultados)

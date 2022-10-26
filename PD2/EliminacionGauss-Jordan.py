import numpy as np
import sys


def Gauss_Jordan(A, b):
    M = A.copy()
    n = len(b)
    x = np.zeros(n)

    # Eliminacion Gauss-Jordan
    for i in range(len(b)):
        M[i].insert(len(b) + 1, b[i][0])

    print("Matriz Aumentada:")
    print("\n".join(["".join(["{:4}".format(item) for item in row]) for row in M]))

    for i in range(n):
        if M[i][i] == 0.0:
            sys.exit("Division por 0 detectada")

        for j in range(n):
            if i != j:
                ratio = M[j][i] / M[i][i]

                for k in range(n + 1):
                    M[j][k] = M[j][k] - ratio * M[i][k]
    print("\nMatriz despues de Aplicar la eliminacion:")
    print("\n".join(["".join(["{:6}".format(item) for item in row]) for row in M]))

    # Solucion
    for i in range(n):
        x[i] = M[i][n] / M[i][i]

    print("\nMatriz Solucion: ")
    for i in range(n):
        print("X%d = %0.2f" % (i, x[i]), end="\t")


# MAIN
# A = [
#     [2, 2],
#     [1, -1],
# ]
A = [
    [120, 200, 80, 100],
    [1, 1, 1, 1],
    [1, -1, 0, 1],
    [0, 1, -3, 0],
]
b = [[2020], [14], [0], [0]]
# b = [
#     [64],
#     [6],
# ]
print("Eliminacion Gaussiana")
Gauss_Jordan(A, b)

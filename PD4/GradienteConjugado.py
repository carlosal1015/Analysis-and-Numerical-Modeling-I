import numpy as np


def gradiente_conjugado(A, b):

    tam = np.shape(A)
    n = tam[0]
    x = np.zeros(n)

    # Metodo
    for i in range(0, n):
        print("Iteracion: ", i)
        r = b - np.dot(A, x)
        print("r = ", r)
        if i == 0:
            p = r
        else:
            num = -1 * np.dot(np.dot(p.T, A), r)
            den = np.dot(np.dot(p.T, A), p)
            beta = num / den
            z = r + beta * p
            print("prueba: ", np.dot((np.dot(p.T, A)), z))
            p = r + beta * p
        print("p = ", p)
        num = np.dot((b - np.dot(A, x)).T, p)
        den = np.dot(np.dot(p.T, A), p)
        alpha = num / den
        x = x + alpha * p
        print("x = ", x)

        print()
    return x


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
# A = np.array([[0, 0, 1], [64, 8, 1], [256, 16, 1]], float)

# Coloca el vector solución b
# b = np.array([0, 320, 0], float)
# Si no es definida positiva
x = gradiente_conjugado(np.dot(A.T, A), np.dot(A.T, b.T))
print(x)
# Si es definida positiva
# x = gradiente_conjugado(A,b)
# print(x)

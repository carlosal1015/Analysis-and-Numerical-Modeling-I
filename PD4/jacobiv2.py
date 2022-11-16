import numpy as np


def metodoJacobi(a, x):
    TOL = 1e-3
    MAX_ITER = 100
    cambio_rel = 1
    cont = 0
    y = np.zeros_like(x)
    while (cambio_rel > TOL) and (cont < MAX_ITER):
        print("x=[" + (" " * 4).join(list(map("{:5.3f}".format, x))) + "[")
        for i in range(n):
            idx = [j for j in range(n) if j != i]
            y[i] = (b[i] - np.dot(a[i, idx], x[idx])) / a[i, i]
        cambio_rel = np.linalg.norm(x - y, np.inf) / np.linalg.norm(y, np.inf)
        x[:] = y[:]
        cont += 1
    print("x=[" + (" " * 4).join(list(map("{:5.3f}".format, x))) + "]")
    if cambio_rel <= TOL:
        print("Metodo converge")
    else:
        print("Metodo no converge")

    print(f"Metodo terminado en {cont} iteraciones. ||x-y||/||y||= {criterio:5.3f}")
    return (x, criterio, cont)


n = 2
a = np.array([10, 1, 2, 10], dtype="f4")
a = np.reshape(a, (n, n))
b = np.array([11, 12], dtype="f4")
x = np.array([0, 0], dtype="f4")

(x, criterio, cont) = metodoJacobi(a, x)

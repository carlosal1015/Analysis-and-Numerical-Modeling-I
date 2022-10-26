import numpy as np
import funcAuxiliares as aux


def sustitucionRegresiva(U, b, diag=False, dec=10):
    n = np.shape(U)[0]
    x = np.array([0.0] * n)
    if not diag:
        for i in range(n - 1, -1, -1):
            x[i] = (b[i] - aux.dot(U[i], x)) / float(U[i, i])
    else:
        for i in range(0, n):
            x[i] = b[i] / float(U[i, i])
    return np.round(np.array(x), dec)


def sustitucionProgresiva(L, b, dec=10):
    n = np.shape(L)[0]
    x = np.array([0.0] * n)
    for i in range(0, n):
        x[i] = (b[i] - aux.dot(L[i], x)) / float(L[i, i])
    return np.round(np.array(x), dec)


def LUSolver(L, U, b, dec=10):
    z = sustitucionProgresiva(L, b, dec)
    print("z:\n", z)
    x = sustitucionRegresiva(U, z, dec)
    return x


def eliminacionGaussiana(A, b, prec=10):
    M = np.copy(A)
    M_a = aux.matAumentada(M, b)
    n = np.shape(M_a)[1] - 1
    print(M_a)
    for i in range(0, n - 1):  # Paso 1
        for p in range(i, n):  # Paso 2
            if M_a[p, i] != 0:
                aux.elementalOp1(M_a, i, p)  # Paso 3
                break
        print(M_a)
        if M_a[i, i] == 0:
            return
        for j in range(i + 1, n):  # Paso 4
            k = M_a[j, i] / M_a[i, i]  # Paso 5
            aux.elementalOp3(M_a, j, i, -k)  # Paso 6
        M_a = np.round(M_a, prec)
        print(M_a)
    if M_a[n - 1, n - 1] == 0:  # Paso 7
        return
    return sustitucionRegresiva(M_a[:, :n], M_a[:, n:], dec=int(prec / 2))  # Paso 8


def gaussJordan(A, b, prec=10):
    M = np.copy(A)
    M_a = aux.matAumentada(M, b)
    n = np.shape(M_a)[1] - 1
    sol = True
    print(M_a)
    for i in range(0, n):  # Paso 1
        for p in range(i, n):  # Paso 2
            if M_a[p, i] != 0:
                aux.elementalOp1(M_a, i, p)  # Paso 3
                break
        print(M_a)
        if M_a[i, i] == 0:
            sol = False
            break
        for j in range(0, n):  # Paso 4
            if j != i:
                k = M_a[j, i] / M_a[i, i]  # Paso 5
                aux.elementalOp3(M_a, j, i, -k)  # Paso 6
        M_a = np.round(M_a, prec)
        print(M_a)
    if M_a[n - 1, n - 1] == 0 or not sol:  # Paso 7
        print("No se puede resolver.")
    else:
        return sustitucionRegresiva(
            M_a[:, :n], M_a[:, n:], True, dec=int(prec / 2)
        )  # Paso 8

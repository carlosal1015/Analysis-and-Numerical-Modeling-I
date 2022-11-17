def LDLt(A):
    dimension = np.shape(A)
    L = np.zeros(dimension)
    D = np.zeros(dimension)

    for i in range(dimension[0]):
        suma_fila = sum([L[i][j] * L[i][j] for j in range(i)])
        D[i][i] = A[i][i] - suma_fila
        for j in range(dimension[1]):
            suma_columna = sum(L[j][k] * L[j][k] * D[k][k] for k in range(i))
            L[j][i] = (A[j][i] - suma_columna) / float(D[i][i])

    return L, D


def isSDP(A):
    n = len(A)
    for i in range(0, n):
        for j in range(0, n):
            if i != j:
                if A[i][i] < 0 or A[i][i] < abs(A[i][j]):
                    return False
    return True


# https://www.emathhelp.net/calculators/linear-algebra/svd-calculator/?i=%5B%5B4%2C11%2C14%5D%2C%5B8%2C7%2C-2%5D%5D
# https://www.math.drexel.edu/~foucart/TeachingFiles/F12/M504Lect1.pdf

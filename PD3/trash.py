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
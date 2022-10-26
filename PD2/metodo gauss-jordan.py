import numpy as np

# INGRESO
A = np.array([[1, 1, 1, 30], [1, 1, -2, 0], [1, 3, -2, 20]])
print("Matriz aumentada")
print(A)
# PROCEDIMIENTO
casicero = 1e-15  # Considerar como 0

# Evitar truncamiento en operaciones
A = np.array(A, dtype=float)
# Pivoteo parcial por filas
tamano = np.shape(A)
n = tamano[0]
m = tamano[1]

# Para cada fila en A
for i in range(0, n - 1, 1):
    # columna desde diagonal i en adelante
    columna = abs(A[i:, i])
    dondemax = np.argmax(columna)

    # dondemax no está en diagonal
    if dondemax != 0:
        # intercambia filas
        temporal = np.copy(A[i, :])
        A[i, :] = A[dondemax + i, :]
        A[dondemax + i, :] = temporal

AB1 = np.copy(A)

# eliminacion hacia adelante
for i in range(0, n - 1, 1):
    pivote = A[i, i]
    adelante = i + 1
    for k in range(adelante, n, 1):
        factor = A[k, i] / pivote
        A[k, :] = A[k, :] - A[i, :] * factor
AB2 = np.copy(A)

# elimina hacia atras
ultfila = n - 1
ultcolumna = m - 1
for i in range(ultfila, 0 - 1, -1):
    pivote = A[i, i]
    atras = i - 1
    for k in range(atras, 0 - 1, -1):
        factor = A[k, i] / pivote
        A[k, :] = A[k, :] - A[i, :] * factor
    # diagonal a unos
    A[i, :] = A[i, :] / A[i, i]
X = np.copy(A[:, ultcolumna])
X = np.transpose([X])
# SALIDA
print("Pivoteo parcial por filas")
print(AB1)
print("eliminacion hacia adelante")
print(AB2)
print("eliminación hacia atrás")
print(A)
print("solución de X: ")
print(X)

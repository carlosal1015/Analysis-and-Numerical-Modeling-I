import numpy as np

A = np.array(
    object=[[15000, 20000, 30000], [10000, 15000, 20000], [1, 1, 1]], dtype=np.float64
)
A_tilde = A.T @ A


def gradienteConjugado(A, b, x0, gtol, maxiter):
    rk = b - np.dot(A, x0)
    pk = rk
    xk = x0
    print(0, "   :", xk, rk)
    for i in range(0, maxiter):
        rkt = np.transpose(rk)
        pkt = np.transpose(pk)
        Apk = np.dot(A, pk)
        alfa_k = np.dot(rkt, pk) / np.dot(pkt, Apk)
        xk = xk + alfa_k * pk
        rk = rk + alfa_k * Apk
        print(i + 1, "   :", xk, rk)
        beta_k = -(np.dot(pkt, rk) / np.dot(pkt, Apk))
        pk = rk + beta_k * pk
        if np.linalg.norm(rk) < gtol:
            break


if __name__ == "__main__":
    b = np.array([250000, 175000, 140], float)
    b_tilde = A.T @ b.T
    x0 = np.array([0, 0, 0], float)
    # gradienteConjugado(A, b, x0, 1e-5, maxiter=100)
    gradienteConjugado(A_tilde, b_tilde, x0, 1e-5, maxiter=100)

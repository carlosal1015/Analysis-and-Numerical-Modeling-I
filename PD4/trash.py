# np.random.seed(18)
# x = np.linspace(0, 2, 10)
# y = np.exp(x) + np.random.randn(10) * 0.8 * x

A = np.array(object=[[1, -6], [1, -2], [1, 1], [1, 7]], dtype=np.float64)
b = np.array(object=[[-1], [2], [1], [6]], dtype=np.float64)
x = np.linalg.lstsq(a=A, b=b, rcond=None)[0]
# print(x)
# print("Verificación")
# print(f"{A @ x} = {b}")

# A1 = np.array(object=[[2, 1], [1, 1], [2, 1]], dtype=np.float64)
# b1 = np.array(object=[[12], [6], [18]], dtype=np.float64)

a = np.random.randn(9, 6)
q, r = np.linalg.qr(a)
print(np.allclose(a, np.dot(q, r)))  # a does equal qr
r2 = np.linalg.qr(a, mode="r")
print(np.allclose(r, r2))  # mode='r' returns the same r as mode='full'
a = np.random.normal(size=(3, 2, 2))  # Stack of 2 x 2 matrices as input
q, r = np.linalg.qr(a)
print(q.shape)
print(r.shape)
print(np.allclose(a, np.matmul(q, r)))

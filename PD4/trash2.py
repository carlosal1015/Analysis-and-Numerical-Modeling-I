A = np.array(object=[[2, 2, 4, 18], [1, 3, -2, 1], [3, 1, 3, 14]], dtype=np.float64)


e_1 = np.zeros(A.shape[0])
e_1[0] = 1.0


v_1 = A[:, 0] + np.sign(A[0][0]) * np.linalg.norm(x=A[:, 0], ord=2) * e_1

print(np.linalg.solve(R, Q.T @ b.T))

# Args:
#         A (float): matriz A.

#     Returns:
#         D (float): matriz diagonal de A.

# Args:
#     A (float): matriz A.

# Returns:
#     E (float): matriz triangular inferior sin contar la diagonal de A.

# Args:
#     A (float): matriz A.

# Returns:
#     F (float): matriz triangular superior sin contar la diagonal de A.
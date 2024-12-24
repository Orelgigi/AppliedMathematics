import numpy as np


def gram_schmidt(a):
    """
    Function to perform Gram-Schmidt process
    """
    eps = 1e-14
    a = a.astype(float)
    n, m = a.shape  # n: rows, m: columns
    r = np.zeros((m, m))
    q = np.zeros_like(a, dtype=float)
    j = 0
    while j < m:
        v = a[:, j].copy()
        for i in range(j):
            r[i, j] = np.inner(q[:, i], v)
            v -= r[i, j] * q[:, i]
        # Check if the vector norm is below tolerance
        if np.linalg.norm(v) <= eps:
            a = np.delete(a, j, axis=1)
            q = np.delete(q, j, axis=1)
            r = np.delete(r, j, axis=1)
            r = np.delete(r, j, axis=0)
            m -= 1
        else:
            r[j, j] = np.linalg.norm(v)
            q[:, j] = v / r[j, j]
            j += 1
    # Validate results by checking orthogonality of Q and decomposition accuracy
    identityMatrix = np.identity(len(a[0]))
    if not np.allclose(q.T @ q, identityMatrix) and not np.allclose(q @ r, a):
        print("Error the matrix Q is not identity")
    return a, q, r


if __name__ == '__main__':
    print("*****1*****")
    a1 = np.array([[1, 1, 3], [2, 1, 4], [3, -1, 1], [2, 1, 1], [1, 0, 2]])
    # Perform Gram-Schmidt process
    a_matrix, b, c = gram_schmidt(a1)
    # Print results
    print("A: \n", a_matrix)
    print("Q: \n", b)
    print("R: \n", c)

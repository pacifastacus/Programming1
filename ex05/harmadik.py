import numpy as np


def magic(n):  # This function is not part of the task, but i leave here for practical reasons
    n = int(n)
    if n < 3:
        raise ValueError("Size must be at least 3")
    if n % 2 == 1:
        p = np.arange(1, n + 1)
        return n * np.mod(p[:, None] + p - (n + 3) // 2, n) + np.mod(p[:, None] + 2 * p - 2, n) + 1
    elif n % 4 == 0:
        J = np.mod(np.arange(1, n + 1), 4) // 2
        K = J[:, None] == J
        M = np.arange(1, n * n + 1, n)[:, None] + np.arange(n)
        M[K] = n * n + 1 - M[K]
    else:
        p = n // 2
        M = magic(p)
        M = np.block([[M, M + 2 * p * p], [M + 3 * p * p, M + p * p]])
        i = np.arange(p)
        k = (n - 2) // 4
        j = np.concatenate((np.arange(k), np.arange(n - k + 1, n)))
        M[np.ix_(np.concatenate((i, i + p)), j)] = M[np.ix_(np.concatenate((i + p, i)), j)]
        M[np.ix_([k, k + p], [0, k])] = M[np.ix_([k + p, k], [0, k])]
    return M


def isMagicSquare(mat):
    col_sum = mat.sum(axis=0)
    row_sum = mat.sum(axis=1)

    # Pick a sum value and check if all the column sums are equal
    picked_sum = col_sum[0]
    col_sum -= picked_sum
    if col_sum.any():
        return False
    # Check if all the row sums are equal with the previously picked element
    row_sum -= picked_sum
    if row_sum.any():
        return False

    return True


magicSquare = magic(10)
notMagicSquare = np.random.randint(0, 100, (10, 10))
print(magicSquare)
print(isMagicSquare(magicSquare))
print(notMagicSquare)
print(isMagicSquare(notMagicSquare))

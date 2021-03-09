import numpy as np


def sortMatrixColumn(M, col):
    M[:, col].sort()


matrix = np.random.randint(0, 50, (6, 5))
colidx = 2
print(matrix, "selected column index:", colidx)
sortMatrixColumn(matrix, colidx)
print(matrix)

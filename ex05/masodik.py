import random

import numpy as np


def sortMatrixColumn(M, col):
    M[:, col].sort()


matrix = np.random.randint(0, 50, (6, 5))
colidx = random.randint(0, 5)
print(matrix, "\nselected column index:", colidx)
sortMatrixColumn(matrix, colidx)
print(matrix)

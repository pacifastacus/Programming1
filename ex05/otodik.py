import numpy as np


def interestingElements(m):
    elements = []
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            if m[i, j] % (i + 1) == 0 and m[i, j] % (j + 1) == 0:
                elements.append((m[i, j], i + 1, j + 1))
    return elements


m, n = np.random.randint(3, 10, (2,)).tolist()
mat = np.random.randint(1, 100, (m, n))

print(mat)
for e in interestingElements(mat):
    print(e)

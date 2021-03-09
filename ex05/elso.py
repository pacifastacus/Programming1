import numpy as np


def isSorted(vec):
    idx = 1
    while idx < len(vec) and vec[idx] >= vec[idx - 1]:
        idx += 1
    return idx == len(vec)


v = (0, 2, 3, 5, 8, 10, 10, 10, 11, 15)
w = [0, 2, 3, 5, 8, 10, 9, 9, 10, 11, 15]
miniv = [5]
arr = np.array([2, 6, 8, 10, 6, 12, 20])

print(isSorted(v))
print(isSorted(w))
print(isSorted(miniv))
print(isSorted(arr))

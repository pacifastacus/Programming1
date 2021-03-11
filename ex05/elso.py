import numpy as np


# Only works in ascending order
def isSorted(vec):
    idx = 1
    while idx < len(vec) and vec[idx] >= vec[idx - 1]:
        idx += 1
    return idx == len(vec)


def isSorted2(vec):
    if len(vec) == 1:
        return True
    else:
        idx = 1
        while vec[0] == vec[idx]:  # skip the repeating elements in the begining of the array
            idx += 1

        if vec[idx] < vec[idx - 1]:  # If this is true, then MAYBE the vector is in descending order
            while idx < len(vec) and vec[idx] <= vec[idx - 1]:
                idx += 1
        else:  # The vector MAYBE in ascending order
            while idx < len(vec) and vec[idx] >= vec[idx - 1]:
                idx += 1
        return idx == len(vec)  # If the index ran through the vector, then it's sorted


def isSorted3(vec):
    vec = list(vec)
    sorted = vec.copy()
    sorted.sort()
    rev_sorted = sorted[::-1]
    return vec == sorted or vec == rev_sorted


v = (0, 2, 3, 5, 8, 10, 10, 10, 11, 15)
w = [0, 2, 3, 5, 8, 10, 9, 9, 10, 11, 15]
miniv = [5]
arr = np.array([2, 6, 8, 10, 6, 12, 20])
rev = [65, 65, 60, 40, 40, 32, 21, 10]

print("v", isSorted(v), isSorted2(v), isSorted3(v))
print("w", isSorted(w), isSorted2(w), isSorted3(w))
print("miniv", isSorted(miniv), isSorted2(miniv), isSorted3(miniv))
print("arr", isSorted(arr), isSorted2(arr), isSorted3(arr))
print("rev", isSorted(rev), isSorted2(rev), isSorted3(rev))

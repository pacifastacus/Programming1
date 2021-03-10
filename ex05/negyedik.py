import numpy as np


def indicesOfSpecialCols(m):
    listOfInd = []
    for i in range(0, m.shape[1]):
        zeros = m[:, i] == 0
        negatives = m[:, i] < 0
        if np.sum(zeros) > 0:
            if np.sum(zeros) * 2 <= np.sum(negatives):
                listOfInd.append(i)
    return listOfInd


def indicesOfInterestedCols(m):
    negatives = (m < 0).sum(axis=0)
    zeros = (m == 0).sum(axis=0)
    return np.flatnonzero((zeros > 0) * (zeros * 2 <= negatives)).tolist()


str = input('Give the shape of array:')
n, m = str.split(',')
m = np.random.randint(-5, 6, (int(n), int(m)))
print(m)
print(indicesOfSpecialCols(m))
print(indicesOfInterestedCols(m))

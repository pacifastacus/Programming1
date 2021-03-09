import numpy as np


def negative_zero_positive(array: np.ndarray):
    return (array < 0).sum(), (array == 0).sum(), (array > 0).sum()


vec = np.random.randint(-50, 50, (50,))
negative, zero, positive = negative_zero_positive(vec)
print(vec)
print("negative elements {}\npositive elements {}\nzero elements {}".format(negative, positive, zero))

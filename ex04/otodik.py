import numpy as np

v = np.arange(-5, 10)
print(v)
v[(v < 8) & (v > 3)] = v[(v < 8) & (v > 3)] * -1
print(v)

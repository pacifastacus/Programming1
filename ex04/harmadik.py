import numpy as np

v = np.random.randint(0, 100, 30)
print(v)
v[v == v.max()] = -1
print(v)

import numpy as np

x = int(input())
v = np.random.randint(0, 100, 10)
e = np.abs(v - x)
print(v)
print(v[e == e.min()])

import numpy as np

v = np.random.random(30)
print(v)
# Legjobb megoldás
# print("A tömb legkisebb elemének indexe {}. A legnagyobb elem indexe pedig {}.".format(v.argmin(),v.argmax()))

minV = v.min()
maxV = v.max()
print(minV, maxV)
ind = np.where((v == minV) | (v == maxV))
print(ind)

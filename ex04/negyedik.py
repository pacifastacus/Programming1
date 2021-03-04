import numpy as np

v = np.random.randint(0, 100, 15)
print(v)
v.sort()
print(v)

# M = np.random.randint(0,100,(4,5)) <- 4x5 mátrix
# M.sort(axis=0) <- oszlopok szerinti rendezés
# M.sort(axis=1) <- sorok szerinti rendezés
# Megjegyzés: M.sort() = M.sort(axis=-1)

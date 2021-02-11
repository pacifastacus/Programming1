import math


def dist(x1, x2, y1, y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)


p1 = input("Add meg az első pont koordinátáit:").split()
p2 = input("Add meg az második pont koordinátáit:").split()
d = dist(float(p1[0]), float(p2[0]), float(p1[1]), float(p2[1]))

print("A p1 ({:s},{:s}) és p2 ({:s},{:s}) pont távolsága: {:f}".format(p1[0], p1[1], p2[0], p2[1], d))

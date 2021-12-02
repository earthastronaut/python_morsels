#%%
from collections import namedtuple
import math


class Points(namedtuple("BasePoints", ("x", "y", "z"))):

    def __sub__(self, no):
        vector = (x1 - x2 for x1, x2 in zip(self, no))
        return self.__class__(*vector)

    def dot(self, no):
        vector = (x1 * x2 for x1, x2 in zip(self, no))
        return sum(vector)

    def cross(self, no):
        x1, y1, z1 = self
        x2, y2, z2 = no
        return self.__class__(
            x=(y1 * z2 - z1 * y2),
            y=-(x1 * z2 - z1 * x2),
            z=(x1 * y2 - y1 * x2),
        )

    def absolute(self):
        squares = sum((x1 ** 2 for x1 in self))
        return pow(squares, 0.5)


def torsional_angle(points):
    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))
    return round(math.degrees(angle), 2)


if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    angle = torsional_angle(points)
    print("%.2f" % angle)



# %%

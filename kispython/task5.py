# 1 по популярности
import math as m


def main(y, z):
    s = 0
    for i in range(2):
        s += m.atan(z[i] ** 2 + 0.01 + 77 * y[-i-1]**3) ** 5
    return s


# 2 по популярности
from math import atan


def main(y, z):
    s = 0
    for i in range(2):
        s += atan(z[i] ** 2 + 0.01 + 77 * y[-i-1]**3) ** 5
    return s


# 4 по популярности
from math import atan


def main(y, z):
    return sum(
        [atan(z[i] ** 2 + 0.01 + 77 * y[-i-1]**3) ** 5 for i in range(2)])


# 5 по популярности
from math import atan


def main(y, z):
    s = 0
    i = 0
    while i != 2:
        s += atan(z[i] ** 2 + 0.01 + 77 * y[-i - 1] ** 3) ** 5
        i += 1
    return s
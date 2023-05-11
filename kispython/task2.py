# 1 по популярности
import math as np


def main(y):
    if y < 13:
        return np.sin(y) ** 3 + 1 + 70 * y
    elif y < 69:
        return (53 * y ** 3) / 49 + 74 * (1 - y ** 3) ** 6
    elif y < 93:
        return 16 * (80 * y ** 3) ** 5
    else:
        return (32 * (34 - y ** 3 - y) ** 6 -
                44 * np.cos(0.1 - y ** 2 / 47 - 55 * y) ** 4 -
                54 * np.sin(y ** 2 / 41 - 61 - 23 * y ** 3) ** 2)


# 2 по популярности
from math import sin, cos


def main(y):
    if y < 13:
        return sin(y) ** 3 + 1 + 70 * y
    elif 13 <= y < 69:
        return (53 * y ** 3) / 49 + 74 * (1 - y ** 3) ** 6
    elif 69 <= y < 93:
        return 16 * (80 * y ** 3) ** 5
    else:
        return (32 * (34 - y ** 3 - y) ** 6 -
                44 * cos(0.1 - y ** 2 / 47 - 55 * y) ** 4 -
                54 * sin(y ** 2 / 41 - 61 - 23 * y ** 3) ** 2)


# 3 по популярности
import math as m


def main(y):
    return {
        y < 13: m.pow(m.sin(y), 3) + 1 + 70 * y,
        13 <= y < 69: (53 * m.pow(y, 3)) / 49 + 74 * m.pow((1 -
                                                            m.pow(y, 3)), 6),
        69 <= y < 93: 16 * m.pow(80 * m.pow(y, 3), 5),
        93 <= y: (32 * m.pow((34 - m.pow(y, 3) - y), 6) -
                  44 * m.pow(m.cos(0.1 - m.pow(y, 2) / 47 - 55 * y), 4) -
                  54 * m.pow(m.sin(y ** 2 / 41 - 61 - 23 * m.pow(y, 3)), 2)),
    }[True]


# 4 по популярности
def main(y):
    return {
        y < 13: sin(y) ** 3 + 1 + 70 * y,
        13 <= y < 69: (53 * y ** 3) / 49 + 74 * (1 - y ** 3) ** 6,
        69 <= y < 93: 16 * (80 * y ** 3) ** 5,
        93 <= y: (32 * (34 - y ** 3 - y) ** 6 -
                  44 * cos(0.1 - y ** 2 / 47 - 55 * y) ** 4 -
                  54 * sin(y ** 2 / 41 - 61 - 23 * y ** 3) ** 2),
    }[True]

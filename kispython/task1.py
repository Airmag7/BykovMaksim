# 1 по популярности
import math as m


def main(y, z):
    result = 63 * (m.pow(z, 2) - y) ** 7 + \
             (54 * (10 * z ** 2 + 1 + y) ** 3 + 67) \
             / (99 * (83 - 77 * y - 70 * z ** 3) ** 7)
    return result


# 2 по популярности
def main(y, z):
    a = 63 * (z ** 2 - y) ** 7
    b = 54 * (10 * z ** 2 + 1 + y) ** 3 + 67
    c = 99 * (83 - 77 * y - 70 * z ** 3) ** 7
    return a + b / c


# 3 по популярности
import math as m


def main(y, z):
    return 63 * m.pow((m.pow(z, 2) - y), 7) + \
        (54 * m.pow((10 * m.pow(z, 2) + 1 + y), 3) +
         + 67) / (99 * m.pow((83 - 77 * y - 70 * m.pow(z, 3)), 7))


# 4 по популярности
def main(y, z):
    return 63 * (z ** 2 - y) ** 7 + \
        (54 * (10 * z ** 2 + 1 + y) ** 3 + 67) / (99 * (83 - 77 * y - 70 * z ** 3) ** 7)

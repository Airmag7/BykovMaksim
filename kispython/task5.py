import math as m


def main(y, z):
    s = 0
    for i in range(2):
        s += m.atan(z[i] ** 2 + 0.01 + 77 * y[-i-1]**3) ** 5
    return s


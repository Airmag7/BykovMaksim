import math as m


def main(*lst):
    z, y = lst
    res = 0
    for i in range(len(y)):
        res += m.atan(z[i]**5 + 0.01 + 77* y[i+1])

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

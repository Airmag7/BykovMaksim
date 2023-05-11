# 1 по популярности
def main(n):
    if n == 0:
        return -0.28
    elif n == 1:
        return 0.32
    else:
        return main(n - 2) - 0.02 - main(n - 1) ** 2

# 2 по популярности
import math as m


def main(n):
    if n == 0:
        return -0.28
    elif n == 1:
        return 0.32
    else:
        return main(n - 2) - 0.02 - m.pow(main(n - 1), 2)


# 3 по популярности
def main(n):
    arr = [-0.28, 0.32]
    for i in range(2, n+3):
        k = arr[i - 2] - 0.02 - (arr[i - 1]) ** 2
        arr.append(k)
    return arr[n]

# 4 по популярности
def main(n):
    a0 = -0.28
    a1 = 0.32
    b = a0 - 0.02 - a1 * a1
    if n == 0:
        return a0
    elif n == 1:
        return a1
    else:
        for _ in range(n-2):
            a0 = a1
            a1 = b
            b = a0 - 0.02 - a1 * a1
    return b


# 5 по популярности
def main(n):
    match n:
        case 0:
            return -0.28
        case 1:
            return 0.32
        case _:
            return main(n - 2) - 0.02 - main(n - 1) ** 2


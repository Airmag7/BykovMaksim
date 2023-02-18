def main(b, n, p):
    s = 0
    for j in range(1, n + 1, 1):
        for c in range(1, b + 1, 1):
            s += 24 * (1 - j ** 2 - c) ** 5 + 75
    for j in range(1, b+1, 1):
        s += 5 * j ** 3 - (88 * p + 20 * j ** 3) ** 4 - j ** 7
    return s

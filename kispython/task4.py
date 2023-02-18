def main(n):
    if n == 0:
        return -0.28
    elif n == 1:
        return 0.32
    else:
        return main(n - 2) - 0.02 - main(n - 1) ** 2

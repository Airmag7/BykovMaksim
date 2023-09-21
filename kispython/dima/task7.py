def main(x):
    x = bin(x)[2:]
    x = '0' * (24 - len(x)) + x
    o3 = int(x[15:24], 2)
    o2 = int(x[6:11], 2)
    o1 = int(x[0:6], 2)
    return tuple((o3, o2, o1))


print(main(7589032))
print(main(2103672))

def main(x):
    x = (bin(int(str(x), 10))[2:])
    x = '0' * (20 - len(x)) + x
    u1 = x[18] + x[19]
    u2 = x[14:18]
    u3 = x[13]
    u4 = x[7:13]
    u5 = x[6]
    u6 = x[0:6]
    return str(int(u2 + u3 + u5 + u6 + u1 + u4, 2))


print(main(358353))
print(main(230276))
print(main(33081))
print(main(115909))
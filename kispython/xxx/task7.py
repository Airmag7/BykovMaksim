def main(x):
    x = (bin(int(str(x), 16))[2:])
    x = '0' * (24 - len(x)) + x
    u4 = x[0:4]
    u3 = x[4:14]
    u2 = "000"
    u1 = x[17:24]
    return int(u3 + u1 + u2 + u4, 2)


print(main('0xabaa7a'))
print(main('0x25faf8'))
print(main('0xd00693'))
print(main('0x6a4d7e'))

def main(x):
    x = (bin(int(str(x), 16))[2:])
    x = '0' * (18 - len(x)) + x
    u4 = hex(int(x[0:3], 2))
    u3 = hex(int(x[3:6], 2))
    u2 = hex(int(x[6:8], 2))
    return tuple((u2, u3, u4))


print(main('0x26793'))
print(main('0x1aca'))
print(main('0x3aa03'))
print(main('0xa696'))

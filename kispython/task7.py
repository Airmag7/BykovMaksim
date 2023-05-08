def main(s):
    s = int(s, 16)
    A1 = s & 1
    A2 = (s >> 1) & 0x1ff
    A3 = (s >> 10) & 0x0ff
    A5 = (s >> 19) & 0x3ff
    d = A1 | (A3 << 1) | (A2 << 8) | (A5 << 17)
    return hex(d)


print(main('0x5a32a2'))
print(main('0x12616be'))
print(main('0x2eaa1de'))
print(main('0x495c3b3'))

def main(s):
    s = int(s, 16)
    A5 = 2 ** 26 - 2 ** 19
    A3 = 2 ** 16 - 2 ** 10
    A2 = 2 ** 9 - 2 ** 1
    A1 = 2 ** 0
    return hex((s & A5) << 24 - 17
               | (s & A3) << 7 - 1
               | (s & A2) << 16 - 8
               | (s & A1) << 0)


print(main('0x5a32a2'))
def main(s):
    L1 = s & 0x3ff
    L2 = (s >> 2) & 0x2f
    L3 = (s >> 6) & 0x1f
    L4 = (s >> 7) & 0x0f
    L5 = (s >> 13) & 0x1f
    L6 = (s >> 14) & 0x1f
    d = L4 | (L1 << 6) | (L6 << 8) | (L5 << 14) | (L3 << 15) | (L2 << 16)
    return d


print(main(358353))
print(main(230276))
print(main(33081))
print(main(115909))

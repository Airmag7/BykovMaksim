from struct import *

FMT = dict(
    char='c',
    int8='b',
    uint8='B',
    int16='h',
    uint16='H',
    int32='i',
    uint32='I',
    int64='q',
    uint64='Q',
    float='f',
    double='d'
)


def parse(buf, offs, ty, order='<'):
    pattern = FMT[ty]
    size = calcsize(pattern)
    value = unpack_from(order + pattern, buf, offs)[0]
    return value, offs + size


def parse_a(buf, offs):
    a1, offs = parse_b(buf, offs)
    a2 = []
    for _ in range(7):
        val, offs = parse(buf, offs, 'char')
        a2.append(val)
    a2 = b''.join(a2).decode('utf-8')
    a3, offs = parse_c(buf, offs)
    a4, offs = parse(buf, offs, 'int64')
    a5 = []
    for _ in range(4):
        val, offs = parse(buf, offs, 'int32')
        a5.append(val)
    a6, offs = parse(buf, offs, 'int32')
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6), offs


def parse_b(buf, offs):
    b1, offs = parse(buf, offs, 'uint32')
    b2, offs = parse(buf, offs, 'uint32')
    b3, offs = parse(buf, offs, 'uint64')
    b4, offs = parse(buf, offs, 'int32')
    return dict(B1=b1, B2=b2, B3=b3, B4=b4), offs


def parse_c(buf, offs):
    c1, offs = parse(buf, offs, 'int16')
    c2, offs = parse(buf, offs, 'int64')
    c3, offs = parse(buf, offs, 'uint64')
    c4 = []
    for _ in range(5):
        d_offs, offs = parse(buf, offs, 'uint32')
        val, _ = parse_d(buf, d_offs)
        c4.append(val)
    return dict(C1=c1, C2=c2, C3=c3, C4=c4), offs


def parse_d(buf, offs):
    d1, offs = parse(buf, offs, 'int16')
    d2 = []
    for _ in range(5):
        val, offs = parse(buf, offs, 'uint8')
        d2.append(val)
    return dict(D1=d1, D2=d2), offs


def main(stream):
    return parse_a(stream, 4)[0]


print(main(b'EZX\xdbR2\x88\x89\xe3\xaa\xad]\xcc\xa8\xeb.Q\xd8\x1e2p\x02\xd9\xbciwjfkdp2'
 b'\xa8\x10\x9c\x87d\t\x12\x8c\xc5\x93\xdb@\xac\xf6\x1e\x89ya\x00\x00'
 b'\x00h\x00\x00\x00o\x00\x00\x00v\x00\x00\x00}\x00\x00\x00\x18 \x8bw\x8a\xce;'
 b'\x95\x97=\xc6h|n\xbb\xa4;\xaf\x18\xdb;\x0e\xf0\x95\xa4\xee\xa3\xb0\xfa\xeb5'
 b'qSI\x9f\xaf5\xc5\xdf\xa1\x18:u7\xb8\xff\x84/\x85\xc4=*rdk\x0f`\xc3F'
 b'\xc4.m\xc6'))
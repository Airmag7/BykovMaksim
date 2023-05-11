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


def parse(buf, offs, ty, order='>'):
    pattern = FMT[ty]
    size = calcsize(pattern)
    value = unpack_from(order + pattern, buf, offs)[0]
    return value, offs + size


def parse_e(buf, offs):
    e1 = []
    for _ in range(6):
        val, offs = parse(buf, offs, 'uint8')
        e1.append(val)
    e2 = []
    for _ in range(2):
        val, offs = parse(buf, offs, 'int32')
        e2.append(val)
    e3, offs = parse(buf, offs, 'uint8')
    return dict(E1=e1, E2=e2, E3=e3), offs


def parse_d(buf, offs):
    d1, offs = parse(buf, offs, 'double')
    d2, offs = parse(buf, offs, 'uint64')
    d3_size, offs = parse(buf, offs, 'uint16')
    d3_offset, offs = parse(buf, offs, 'uint32')
    d3 = []
    for _ in range(d3_size):
        e_offs, offs = parse(buf, offs, 'uint16')
        val, _ = parse_e(buf, e_offs)
        d3.append(val)
    return dict(D1=d1, D2=d2, D3=d3), offs


def parse_c(buf, offs):
    c1, offs = parse(buf, offs, 'int8')
    c2, offs = parse(buf, offs, 'uint16')
    return dict(C1=c1, C2=c2), offs


def parse_b(buf, offs):
    b1, offs = parse(buf, offs, 'uint8')
    b2, offs = parse(buf, offs, 'int8')
    b3, offs = parse(buf, offs, 'uint8')
    b4, offs = parse(buf, offs, 'float')
    b5, offs = parse(buf, offs, 'uint16')
    b6, offs = parse_c(buf, offs)
    b7, offs = parse(buf, offs, 'uint8')
    b8, offs = parse(buf, offs, 'double')
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5, B6=b6, B7=b7, B8=b8), offs


def parse_a(buf, offs):
    a1, offs = parse_b(buf, offs)
    a2, offs = parse(buf, offs, 'uint8')
    a3, offs = parse(buf, offs, 'int16')
    a4, offs = parse(buf, offs, 'double')
    a5, offs = parse(buf, offs, 'int8')
    a6_size, offs = parse(buf, offs, 'uint16')
    a6_offset, offs = parse(buf, offs, 'uint16')
    a6 = []
    for _ in range(a6_size):
        val, a6_offs = parse(buf, offs, 'char')
        a6.append(val)
    d_offset, offs = parse(buf, offs, 'uint32')
    a7, _ = parse_d(buf, d_offset)
    a8, offs = parse(buf, offs, 'uint32')
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6, A7=a7, A8=a8), offs


def main(stream):
    return parse_a(stream, 4)[0]


print(main(b'HUO\xc4$\xe5\xbf\x00bry\xb6=\xecCs?\xe3m;y\xf7>\x9e\x88\x80Y\xbf'
 b'\xea\xfc\x0bZ\xe9\xa4Zo\x00\x02\x000\x00\x00\x00\x87\xcb\x1e*Isf\xb8\xda'
 b'\xfc\xdf\x1b\xb8\xf7\xf2\xe8\x8a\xa2\xc0\xfe\xd5\xd3\xd4\xf6C'
 b'\xec\x15\x16\x1e\n5\xde6&\xac\x0baT\xdb6_r\xc5-j\x9b\xb7c\xa1\x87?Ej'
 b'\xdc\x1a9]\x9f\xb8\xb1\xd7\x9d\x85\x9b\xb5`W\x1aFH\xf4rX\x00\x86m\xf0'
 b'\x98\x99\x80(P\x002\x00A\x00P\x00_\x00n\xbf\xe2u\xe2q,2D\xe1\xb2\x11\xbeN'
 b'\xb5\xc4\xe6\x00\x05\x00\x00\x00}'))
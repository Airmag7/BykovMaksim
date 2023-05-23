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
    d3_offs, offs = parse(buf, offs, 'uint32')
    d3 = []
    for _ in range(d3_size):
        e_offs, d3_offs = parse(buf, d3_offs, 'uint16')
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
    a6_offs, offs = parse(buf, offs, 'uint16')
    a6 = []
    for _ in range(a6_size):
        val, a6_offs = parse(buf, a6_offs, 'char')
        a6.append(val)
    a6 = b''.join(a6).decode('utf-8')
    d_offset, offs = parse(buf, offs, 'uint32')
    a7, _ = parse_d(buf, d_offset)
    a8, offs = parse(buf, offs, 'uint32')
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6, A7=a7, A8=a8), offs


def main(stream):
    return parse_a(stream, 3)[0]


print(main(b'HUO\nn\xc2\xbf*(\x18\xb8\xc3D\xd4\x9d\x0e\xbf\xdea\x7f\x17\xacR\x00"\x00Y?'
 b'\xee\x80D\xd1)\x13$)\x00\x02\x000\x00\x00\x00\x87\x9a\xb6#tdx\x88jm\xd2\xbdt'
 b'\xf4\t\xe2^\xf8\xbeI\xbb\x80\xea\xf4\x7f\xec\xc2;\x15 \xdf \xfeG\xc6\x83\xc4'
 b'R(\x8e\xfeG\x9f\\a\x01\xf5q\x8d\x9dkvI\xb1\xc967\xd7\xc3\x8d\xa1\xcdk^\x9e'
 b'\xa1\xda#\x94\xd9\xf7\x95\xc4\xa2\xb6t\xcb\xb3\xb3\x1aTB\x002\x00A\x00P\x00'
 b'_\x00n?\xc5\xdc\x92B\x197\xf8\x1a\x15\xcc\xaa(\x9c8h\x00\x05\x00\x00\x00}'))

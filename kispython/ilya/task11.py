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


def parse_e(buf, offs):
    e1_size, offs = parse(buf, offs, 'uint16')
    e1_offs, offs = parse(buf, offs, 'uint32')
    e1 = []
    for _ in range(e1_size):
        val, e1_offs = parse(buf, e1_offs, 'uint8')
        e1.append(val)
    e2, offs = parse(buf, offs, 'uint16')
    e3, offs = parse(buf, offs, 'uint32')
    e4, offs = parse(buf, offs, 'int8')
    e5, offs = parse(buf, offs, 'float')
    return dict(E1=e1, E2=e2, E3=e3, E4=e4, E5=e5), offs


def parse_d(buf, offs):
    d1, offs = parse(buf, offs, 'uint16')
    d2, offs = parse(buf, offs, 'int32')
    d3, offs = parse(buf, offs, 'uint8')
    return dict(D1=d1, D2=d2, D3=d3), offs


def parse_c(buf, offs):
    d_offset, offs = parse(buf, offs, 'uint32')
    c1, _ = parse_d(buf, d_offset)
    c2, offs = parse(buf, offs, 'float')
    c3_size, offs = parse(buf, offs, 'uint32')
    c3_offset, offs = parse(buf, offs, 'uint32')
    c3 = []
    for _ in range(c3_size):
        val, c3_offset = parse(buf, c3_offset, 'uint32')
        c3.append(val)
    return dict(C1=c1, C2=c2, C3=c3), offs


def parse_b(buf, offs):
    b1, offs = parse(buf, offs, 'int16')
    b2, offs = parse(buf, offs, 'int64')
    b3_size, offs = parse(buf, offs, 'uint32')
    b3_offs, offs = parse(buf, offs, 'uint32')
    b3 = []
    for _ in range(b3_size):
        c_offs, b3_offs = parse(buf, b3_offs, 'uint32')
        val, _ = parse_c(buf, c_offs)
        b3.append(val)
    b4 = []
    for _ in range(6):
        val, offs = parse(buf, offs, 'int16')
        b4.append(val)
    b5, offs = parse(buf, offs, 'uint16')
    b6, offs = parse(buf, offs, 'float')
    b7, offs = parse(buf, offs, 'uint32')
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5, B6=b6, B7=b7), offs


def parse_a(buf, offs):
    a1, offs = parse(buf, offs, 'uint32')
    a2, offs = parse(buf, offs, 'uint32')
    a3, offs = parse(buf, offs, 'int32')
    b_offset, offs = parse(buf, offs, 'uint32')
    a4, _ = parse_b(buf, b_offset)
    a5, offs = parse(buf, offs, 'int64')
    a6, offs = parse_e(buf, offs)
    a7, offs = parse(buf, offs, 'int64')
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6, A7=a7), offs


def main(stream):
    return parse_a(stream, 4)[0]


print(main(b"xEXH\x89F\x9c\xb1\xd9\xcd\xb7\xe8Hh\xea\x16\x87\x00\x00\x00'\xbaA\x13"
 b'\xbbI:\xc2\x05\x00\xaf\x00\x00\x00\xd6\xec\x88\xc7-y2\x07\xe7\x1a?\xa7\xc7?'
 b'\r\xba\xb5b\xd1\xe6\xf4\xaa\xf4\xcf\x842\xf1\xd8q?v\x18\xff"|l\xb8\xa2'
 b'5\x00\x00\x00\xba\xdaS?\x03\x00\x00\x00<\x00\x00\x00\x97/\xc3\xd4'
 b'0\x94\xa4\xab\xd7f\xf8\x92\xb1\xe3\xca.\xbb\xa3\xf4\x16\xef\x00\xbbX'
 b'\x00\x00\x00\x8f\xefN>\x04\x00\x00\x00_\x00\x00\x00H\x00\x00\x00o'
 b'\x00\x00\x00\x07\x06\x00\xfa\xa3A\x87w\x97\x97\x02\x00\x00\x00\x7f\x00\x00'
 b'\x00\xa7\x0c\xbb\xdc|r\x89KH\x0ek\x90\xfb\xa5=\xe8e\xbe\x80\xf2\xe8+\xa9'
 b'\x9a\x16\xe6\xba'))
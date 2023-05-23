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


def parse_f(buf, offs):
    f1 = []
    for _ in range(7):
        val, offs = parse(buf, offs, 'uint8')
        f1.append(val)
    f2, offs = parse(buf, offs, 'int16')
    f3, offs = parse(buf, offs, 'double')
    f4, offs = parse(buf, offs, 'uint32')
    f5, offs = parse(buf, offs, 'uint8')
    f6, offs = parse(buf, offs, 'uint64')
    f7, offs = parse(buf, offs, 'double')
    return dict(F1=f1, F2=f2, F3=f3, F4=f4, F5=f5, F6=f6, F7=f7), offs


def parse_e(buf, offs):
    e1, offs = parse(buf, offs, 'int16')
    e2, offs = parse(buf, offs, 'double')
    return dict(E1=e1, E2=e2), offs


def parse_d(buf, offs):
    d1, offs = parse(buf, offs, 'uint32')
    d2, offs = parse(buf, offs, 'int8')
    return dict(D1=d1, D2=d2), offs


def parse_c(buf, offs):
    c1, offs = parse(buf, offs, 'uint16')
    c2, offs = parse_d(buf, offs)
    return dict(C1=c1, C2=c2), offs


def parse_b(buf, offs):
    b1, offs = parse(buf, offs, 'double')
    b2_size, offs = parse(buf, offs, 'uint16')
    b2_offs, offs = parse(buf, offs, 'uint16')
    b2 = []
    for _ in range(b2_size):
        c_offs, b2_offs = parse(buf, b2_offs, 'uint16')
        val, _ = parse_c(buf, c_offs)
        b2.append(val)
    b3_size, offs = parse(buf, offs, 'uint16')
    b3_offs, offs = parse(buf, offs, 'uint16')
    b3 = []
    for _ in range(b3_size):
        val, b3_offs = parse(buf, b3_offs, 'char')
        b3.append(val)
    b3 = b''.join(b3).decode('utf-8')
    b4_size, offs = parse(buf, offs, 'uint16')
    b4_offs, offs = parse(buf, offs, 'uint32')
    b4 = []
    for _ in range(b4_size):
        val, b4_offs = parse(buf, b4_offs, 'int64')
        b4.append(val)
    e_offset, offs = parse(buf, offs, 'uint32')
    b5, _ = parse_e(buf, e_offset)
    b6, offs = parse(buf, offs, 'float')
    b7, offs = parse_f(buf, offs)
    b8, offs = parse(buf, offs, 'uint8')
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5, B6=b6, B7=b7, B8=b8), offs


def parse_a(buf, offs):
    a1, offs = parse_b(buf, offs)
    a2, offs = parse(buf, offs, 'int8')
    return dict(A1=a1, A2=a2), offs


def main(stream):
    return parse_a(stream, 4)[0]


print(main(b'HZVJ\xbf\xee\xe0W\xd2\x8c\x84r\x00\x02\x00X\x00\x03\x00\\\x00\x04\x00\x00'
 b'\x00_\x00\x00\x00\x7f\xbfmG\x1a\xcbu\xb2\xec\xc4\xc2\xb0\xc7\xa8?'
 b'\xc3\x8b\x08_\x03\x12@H\x0e\xb0\xff\x83rp\xc0\x0f(\x0f\xb1\xe3\xbf\xe4A;'
 b'!\xe3\x1a.\xa5\xbc\xaa\x80\xd6l\xd5\x9b\x1b\x858\x06\x97p\x19\xaa\x00J\x00Q'
 b'iwl\xee\xca\xd9\xea\xff\xdd\x90U\x87\x8c\xddQ\x12TQ\x1f\xed\xf1\xd0\xa5\xb5'
 b'\xdaDl\x95=\xd3\r\xeb\x00\x92z\x1a\xb6?\x9dL\xac\x89\xc5\xd0\x80'))
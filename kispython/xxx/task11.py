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


def parse_d(buf, offs):
    d1, offs = parse(buf, offs, 'int32')
    d2, offs = parse(buf, offs, 'int8')
    d3, offs = parse(buf, offs, 'uint16')
    d4, offs = parse(buf, offs, 'uint64')
    d5, offs = parse(buf, offs, 'int8')
    return dict(D1=d1, D2=d2, D3=d3, D4=d4, D5=d5), offs


def parse_c(buf, offs):
    c1, offs = parse_d(buf, offs)
    c2, offs = parse(buf, offs, 'uint16')
    c3 = []
    for _ in range(5):
        val, offs = parse(buf, offs, 'uint8')
        c3.append(val)
    return dict(C1=c1, C2=c2, C3=c3), offs


def parse_b(buf, offs):
    b1 = []
    for _ in range(7):
        val, offs = parse(buf, offs, 'char')
        b1.append(val)
    b1 = b''.join(b1).decode('utf-8')
    b2, offs = parse(buf, offs, 'int8')
    return dict(B1=b1, B2=b2), offs


def parse_a(buf, offs):
    a1, offs = parse(buf, offs, 'double')
    b_offset, offs = parse(buf, offs, 'uint16')
    a2, _ = parse_b(buf, b_offset)
    a3, offs = parse(buf, offs, 'uint32')
    a4_size, offs = parse(buf, offs, 'uint16')
    a4_offs, offs = parse(buf, offs, 'uint16')
    a4 = []
    for _ in range(a4_size):
        c_offs, a4_offs = parse(buf, a4_offs, 'uint32')
        val, _ = parse_c(buf, c_offs)
        a4.append(val)
    a5 = []
    for _ in range(5):
        val, offs = parse(buf, offs, 'uint16')
        a5.append(val)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5), offs


def main(stream):
    return parse_a(stream, 4)[0]


print(main(b'CCX\xef\x00\x16Y-\x98U\x82\xbf \x00Of0p\x04\x00\x84\x00\xa6L\xb2.\xd7\xc5'
 b'\x89\xd5`\xa8ckmassuw\x97\xd9\xac\xbb\xbbq\xaeL\xca$:\xf9\x11\x7f\xe4\xa5'
 b'\x8e\x9c4\x08\x9b\xbd\xc8\x89\x8f\x17(\xd4\xe8\xf6\xbfwM=\xdf\xcc\xd8\xcayL'
 b'\x93\xe8\xba\xbd&\x98~\xea\xec\xaa\xa02\x02p\xca\xa6?\xc6\rh6\xeb\x11?'
 b'\xb7$qD~a\xd9\x04\x16\xb6\xaa\xda\n\x9d\x98:\xcc\xe8\xf8n\x91h\x18\x9c'
 b' \xd8\x96\x0c(\x00\x00\x00?\x00\x00\x00V\x00\x00\x00m\x00\x00\x00'))

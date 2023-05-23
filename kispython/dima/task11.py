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
    a1_size, offs = parse(buf, offs, 'uint32')
    a1_offs, offs = parse(buf, offs, 'uint32')
    a1 = []
    for _ in range(a1_size):
        val, a1_offs = parse(buf, a1_offs, 'char')
        a1.append(val)
    a1 = b''.join(a1).decode('utf-8')
    a2, offs = parse(buf, offs, 'int32')
    a3_size, offs = parse(buf, offs, 'uint32')
    a3_offs, offs = parse(buf, offs, 'uint32')
    a3 = []
    for _ in range(a3_size):
        b_offs, a3_offs = parse(buf, a3_offs, 'uint32')
        val, _ = parse_b(buf, b_offs)
        a3.append(val)
    a4, offs = parse_d(buf, offs)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4), offs


def parse_b(buf, offs):
    b1, offs = parse(buf, offs, 'uint64')
    c_offset, offs = parse(buf, offs, 'uint32')
    b2, _ = parse_c(buf, c_offset)
    b3, offs = parse(buf, offs, 'float')
    b4, offs = parse(buf, offs, 'uint32')
    b5, offs = parse(buf, offs, 'int16')
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5), offs


def parse_c(buf, offs):
    c1, offs = parse(buf, offs, 'int8')
    c2 = []
    for _ in range(6):
        val, offs = parse(buf, offs, 'int8')
        c2.append(val)
    c3, offs = parse(buf, offs, 'uint32')
    return dict(C1=c1, C2=c2, C3=c3), offs


def parse_d(buf, offs):
    d1 = []
    for _ in range(5):
        val, offs = parse(buf, offs, 'int16')
        d1.append(val)
    d2 = []
    for _ in range(4):
        val, offs = parse(buf, offs, 'float')
        d2.append(val)
    d3, offs = parse(buf, offs, 'int16')
    d4, offs = parse(buf, offs, 'int32')
    d5, offs = parse(buf, offs, 'uint8')
    d6, offs = parse(buf, offs, 'int64')
    d7, offs = parse(buf, offs, 'int32')
    d8, offs = parse(buf, offs, 'uint8')
    return dict(D1=d1, D2=d2, D3=d3, D4=d4, D5=d5, D6=d6, D7=d7, D8=d8), offs


def main(stream):
    return parse_a(stream, 5)[0]


print(main(b'UAXL[\x04\x00\x00\x00G\x00\x00\x00\x0f;\xa2\x16\x03\x00\x00\x00\xae\x00\x00'
 b'\x00l\xae\xacR\xc8.z\xbf\xb6\xc7\xb5\xe3}>\x1b\x9a\x17>\xcd\xa1\x1c\xbf\xf1'
 b'\xc0\t?5\xc7\x14\xb0\xf6\x15q-\x03\ru\xa93-m\xf6\x8e\x14}|rtod\x12'
 b'\x0b\x93\xff\xb2.p\x17\xcf`A\x9c\xfd\x04\xd3\xa3=<:K\x00\x00\x00\xdf\x92'
 b'\x1f\xbec\x93wK\r%\xb0\xdf\r\xefT\xf7\xd5\xb1\xc4\xe4\x03\xff'
 b'\x95\xe7\x86\xa4\xd7\xce\xael\x00\x00\x00t7\x86> \x9a@\xe6\x1f7\xbd\x8e\xde'
 b"\x84Xy\x1e'E\xeb\xf4\x01\xb5O\xb6\xdc\xdefl\x8d\x00\x00\x00\xc0Ok\xbf"
 b'\xb9\xf7\xce\xa3\xc8\xbaV\x00\x00\x00w\x00\x00\x00\x98\x00\x00\x00'))

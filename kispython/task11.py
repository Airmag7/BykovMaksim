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
    a1, offs = parse(buf, offs, 'uint32')
    b_offset, offs = parse(buf, offs, 'uint16')
    a2, _ = parse_b(buf, b_offset)
    a3, offs = parse(buf, offs, 'double')
    a4 = []
    for _ in range(2):
        val, offs = parse(buf, offs, 'char')
        a4.append(val)
    a4 = b''.join(a4).decode('utf-8')
    a5, offs = parse_c(buf, offs)
    a6, offs = parse(buf, offs, 'double')
    a7, offs = parse(buf, offs, 'int8')
    a8, offs = parse(buf, offs, 'float')
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6, A7=a7, A8=a8), offs


def parse_b(buf, offs):
    b1, offs = parse(buf, offs, 'int16')
    b2, offs = parse(buf, offs, 'int16')
    return dict(B1=b1, B2=b2), offs


def parse_c(buf, offs):
    c1, offs = parse(buf, offs, 'float')
    c2 = []
    for _ in range(3):
        val, offs = parse_d(buf, offs)
        c2.append(val)
    c3 = []
    for _ in range(7):
        val, offs = parse(buf, offs, 'uint8')
        c3.append(val)
    c4, offs = parse(buf, offs, 'int64')
    c5, offs = parse(buf, offs, 'double')
    c6, offs = parse(buf, offs, 'int32')
    c7, offs = parse(buf, offs, 'double')
    return dict(C1=c1, C2=c2, C3=c3, C4=c4, C5=c5, C6=c6, C7=c7), offs


def parse_d(buf, offs):
    d1, offs = parse(buf, offs, 'uint16')
    d2, offs = parse(buf, offs, 'uint64')
    d3_size, offs = parse(buf, offs, 'uint32')
    d3_offset, offs = parse(buf, offs, 'uint16')
    d3 = []
    for _ in range(d3_size):
        val, d3_offset = parse(buf, d3_offset, 'uint16')
        d3.append(val)
    d4, offs = parse(buf, offs, 'uint32')
    d5, offs = parse(buf, offs, 'int8')
    d6, offs = parse(buf, offs, 'uint8')
    return dict(D1=d1, D2=d2, D3=d3, D4=d4, D5=d5, D6=d6), offs


def main(stream):
    return parse_a(stream, 4)[0]


print(main(b'\xd2UWU-\xc0a\x0c\x8a\x00p7\x19\xd5\xb8\xe7\xd4?ec\xcc>\x1f\xbf\xcd\x0fM_'
 b'\x0e\x90\xb4\x1a\xa8]\x03\x00\x00\x00\x8e\x00\xdd\xbf\xa5(\xea\x9b^\x87'
 b'\xaak\xc3\xc6(\xd0M\xfa\x02\x00\x00\x00\x94\x00\x1b5\xb6\xb2.*\xba>\xe0\x86'
 b'\xc8ru\xb4\xbac\x02\x00\x00\x00\x98\x007o}\x86\x90\xc06j6\x03\x06\xd0'
 b'\x81\x1b\xb4\x96R\x1b^\xf7\xabVHE1\x80\x1e\xec?\xdb\xa1\xdeWX\r\x84'
 b'\x01\x08j\xcd\xbf\xf8\x00\x8aN8\xf9\xda\xbfX\xb6\xb6Y\xbfN\xd7w\xcde{'
 b')\xac\x99JO\x9d\x9b\xdc\xdd\xb9>\xc6'))
# 4.1

def generate_groups():
    for a in range(1, 9):
        yield f'ИВБО-0{a}-21'
    for b in range(1, 34):
        if b < 10:
            yield f'ИКБО-0{b}-21'
        else:
            yield f'ИКБО-{b}-21'
    for c in range(1, 3):
        yield f'ИМБО-0{c}-21'
    for d in range(1, 14):
        if d < 10:
            yield f'ИНБО-0{d}-21'
        else:
            yield f'ИНБО-{d}-21'


groups = []
for i in generate_groups():
    groups.append(i)
print(groups)

# 4.2
'''
from sys import stdout


def my_print(*args, sep='', end='\n'):
    string = []
    for x in args:
        x = str(x)
        string.append(x)
    string = sep.join(string) + end
    stdout.write(string)


my_print([1, 2, 3], 4, sep='-_-_-_', end='\n\n')
my_print("df")
'''
# 4.3
'''
from ctypes import *


def decipher(v, k):
    y = c_uint32(v[0])
    z = c_uint32(v[1])
    sum = c_uint32(0xc6ef3720)
    delta = 0x9e3779b9
    n = 32
    w = [0, 0]

    while n > 0:
        z.value -= (y.value << 4) + k[2] ^ y.value + sum.value ^ (y.value >> 5) + k[3]
        y.value -= (z.value << 4) + k[0] ^ z.value + sum.value ^ (z.value >> 5) + k[1]
        sum.value -= delta
        n -= 1

    w[0] = hex(y.value)
    w[1] = hex(z.value)
    return w[0][2:], w[1][2:]


msg = 'E3238557 6204A1F8 E6537611 174E5747
5D954DA8 8C2DFE97 2911CB4C 2CB7C66B
E7F185A0 C7E3FA40 42419867 374044DF
2519F07D 5A0C24D4 F4A960C5 31159418
F2768EC7 AEAF14CF 071B2C95 C9F22699
FFB06F41 2AC90051 A53F035D 830601A7
EB475702 183BAA6F 12626744 9B75A72F
8DBFBFEC 73C1A46E FFB06F41 2AC90051
97C5E4E9 B1C26A21 DD4A3463 6B71162F
8C075668 7975D565 6D95A700 7272E637'

v = []
k = [0, 4, 5, 1]
msg = msg.split('\n')
for m in msg:
    m = m.split()
    for i in m:
        v.append(int(i, 16))

for i in range(0, len(v), 2):
    print(decipher(v[i:], k))
'''
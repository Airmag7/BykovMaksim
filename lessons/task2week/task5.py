# 5.1
'''
def ham_dist(a, b):
    return bin(a ^ b).count('1')


def ham_dist_naive(a, b):
    a = bin(a)[2:]
    b = bin(b)[2:]
    ans = 0
    if len(a) > len(b):
        b = '0' * (len(a) - len(b)) + b
    elif len(b) > len(a):
        a = '0' * (len(b) - len(a)) + a
    print(a, b)
    for i in range(len(a)):
        if a[i] != b[i]:
            ans += 1
    return ans


print(ham_dist(0b00110, 0b11000))
print(ham_dist_naive(5, 150))
'''
# 5.2

def decode_val(a):
    a = str(bin(a))[2:]
    a = '0' * (24 - len(a)) + a
    er1 = ['011', '101', '110']
    er0 = ['001', '010', '100']
    for i in range(0, 24, 3):
        if a[i:i + 3] in er1:
            a = a[:i] + '111' + a[i + 3:]
        elif a[i:i + 3] in er0:
            a = a[:i] + '000' + a[i + 3:]
    a = a.replace('111', '1')
    a = a.replace('000', '0')
    return int(a, 2)


a = [815608, 2064837, 2093080, 2063879, 196608, 2067983, 10457031, 1830912, 2067455, 2093116, 1044928, 2064407, 6262776,
     2027968, 4423680, 2068231, 2068474, 1999352, 1019903, 2093113, 2068439, 2064455, 1831360, 1936903, 2067967,
     2068456]
# print(decode_val(10457031))
for i in a:
    print(decode_val(i))

# 5.3
'''
from functools import cache


@cache
def lev_dist(a, b, i, j):
    if i == 0 or j == 0:
        return max(i, j)
    elif a[i - 1] == b[j - 1]:
        return lev_dist(a, b, i - 1, j - 1)
    else:
        return 1 + min(lev_dist(a, b, i, j - 1), lev_dist(a, b, i - 1, j), lev_dist(a, b, i - 1, j - 1))


a, b = input(), input()
print(lev_dist(a, b, len(a), len(b)))
'''
# 5.4
'''
from functools import cache


@cache
def lev_dist(a, b, i, j):
    if i == 0 or j == 0:
        return max(i, j)
    elif a[i - 1] == b[j - 1]:
        return lev_dist(a, b, i - 1, j - 1)
    else:
        x = lev_dist(a, b, i, j - 1)
        y = lev_dist(a, b, i - 1, j)
        z = lev_dist(a, b, i - 1, j - 1)
        if x == min(x, y, z):
            print("del")
            return 1 + min(x, y, z)
        elif y == min(x, y, z):
            print("paste")
            return 1 + min(x, y, z)
        else:
            print("remove")
            return 1 + min(x, y, z)


print(lev_dist("столб", "слон", 5, 4))
'''

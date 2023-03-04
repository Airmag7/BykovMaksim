# Задание 1
"""
x = int(input())
x = x + x + x
x = x + x
x = x + x
print(x)
"""
# Задание 2
'''
x = int(input())
x = x + x
x = x + x
x = x + x
x = x + x
print(x)
'''
# Задание 3
'''
x = int(input())
y = x
x = x + x
x = x + x
x = x + x
y = y - x
y = x - y
print(y)
'''

# Задание 4
'''
def naive_mul(x, y):
    r = 1
    for i in range(1, y - 1):
        x = x + x
    return x


def test():
    assert naive_mul(3, 4) == 3 * 4
    print("True")


test()
'''
# Задание 5
'''
def fast_mul(x,y):
    s = 0
    while x != 0:
        if x%2 != 0:
            s = s + y
        x = x//2
        y = y*2
    return s
def test(x,y):
    assert fast_mul(x,y) == x*y
    print("True")
test(3,4)
'''
# Задание 6
'''
def fast_pow(x, n):
    s = 1
    for _ in range(n):
        s1 = 0
        a = x
        b = s
        while a != 0:
            if a % 2 != 0:
                s1 = s1 + b
            a = a // 2
            b = b * 2
        s = s1

    return s


print(fast_pow(2, 5))


def test(x, n):
    assert fast_pow(x, n) == x ** n
    print("True")


test(3, 4)
'''

# Задание 7
'''
def mul_bits(x, y, bits):
    x &= (2 ** bits - 1)
    y &= (2 ** bits - 1)
    return x * y


def mul_16(x, y):
    xh = x >> 8
    yh = y >> 8
    return mul_bits(x, y, 8) + (mul_bits(xh, y, 8) + mul_bits(x, yh, 8) << 8) + (mul_bits(xh, yh, 8) << 16)
'''

# Задание 8
'''
def mul16k(k, l):
    a = k // 256
    b = k % 256
    c = l // 256
    d = l % 256
    x = 2 ** 8
    return ((a * c) << 16) + (((a + b) * (c + d) - a * c - b * d) << 8) + b * d


print(mul16k(72, 36))
'''

# Задание 9
'''
def fast_mul_gen(y):
    print("def f(x): \n    x = y")
    for _ in range(y - 1):
        print("    y += x")
    print("    return (x)")


fast_mul_gen(8)

'''


# Задание 10
'''
def fast_pow_gen(y):
    print("def f(x): \n    x = y")
    print("    fast_mul_gen(y)")
    for _ in range(y - 1):
        print("    x = f(y)")
    print("    return (x)")


fast_pow_gen(8)
'''

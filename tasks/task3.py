#Задание 1
'''
x = int(input())
x = x + x + x
x = x + x
x = x + x
print(x)
'''
#Задание 2
'''
x = int(input())
x = x + x
x = x + x
x = x + x
x = x + x
print(x)
'''
#Задание 3
'''
x = int(input())
x = x
x = x
x = x
print(x)
'''
#Задание 4
'''
def naive_mul(x, y):
    r = 1
    for i in range(1, y-1):
        x = x + x
    return x
def test():
    assert naive_mul(3,4) == 3*4
    print("True")
test()
'''
#Задание 5
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
#Задание 6
'''
def fast_pow(x,n):
    s = 0
    d = x
    for i in range(1, n-1):
        x = s
        y = d
        while x != 0:
            if x % 2 != 0:
                s = s + y
            x = x // 2
            y = y * 2
    return s
print(fast_pow(3,4))
def test(x,n):
    assert fast_pow(x,n) == x**n
    print("True")
test(3,4)
'''


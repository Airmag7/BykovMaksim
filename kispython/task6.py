# 1 по популярности
"""
x = {('ABNF', 1959, 1979, 1965): 0,
     ('ABNF', 2019, 1979, 1965): 1,
     ('ABNF', 1964, 1979, 1965): 2,
     ('M', 1959, 1994, 1965): 7,
     ('M', 2019, 1994, 1965): 8,
     ('M', 1964, 1994, 1965): 9,
     ('ABNF', 1994, 1965): 3,
     ('ABNF', 2008, 1965): 4,
     ('M', 2008, 1965): 10,
     ('M', 1979, 1965): 6}


def main(arr):
    arr.pop(2)
    if arr[3] == 2013:
        return 11
    if arr[3] == 1969:
        return 12
    if arr[0] == 'PUG':
        return 5
    if ((arr[0] == 'ABNF' and arr[2] != 1979) or
            (arr[0] == 'M' and arr[2] != 1994)):
        arr.pop(1)
    arr = tuple(arr)
    return x[arr]


print(main(['M', 2019, 'LESS', 1994, 1965]))
"""

# 3 по популярности
"""
def four(items, left, middle, right):
    match items[4]:
        case 1965:
            return left
        case 2013:
            return middle
        case 1969:
            return right


def zero(items, left, middle,  right):
    match items[0]:
        case 'ABNF':
            return left
        case 'PUG':
            return middle
        case 'M':
            return right


def three(items, left, middle, right):
    match items[3]:
        case 1979:
            return left
        case 1994:
            return middle
        case 2008:
            return right


def one(items, left, middle, right):
    match items[1]:
        case 1959:
            return left
        case 2019:
            return middle
        case 1964:
            return right


def main(items):
    result = four(items,
                  zero(items,
                       three(items,
                             one(items,
                                 0,
                                 1,
                                 2),
                             3,
                             4),
                       5,
                       three(items,
                             6,
                             one(items,
                                 7,
                                 8,
                                 9),
                             10)),
                  11,
                  12)

    return result


print(main(['PUG', 2019, 'LESS', 2008, 1965]))
print(main(['ABNF', 2019, 'FREGE', 1979, 2013]))
print(main(['M', 2019, 'LESS', 1994, 1965]))
print(main(['M', 1959, 'LESS', 1994, 1969]))
print(main(['M', 1959, 'FREGE', 2008, 1965]))
"""

# 5 по популярности

"""
class Tree:
    items = []

    def __init__(self, items):
        self.items = items

    def four(self, left, middle, right):
        if self.items[4] == 1965:
            return left
        elif self.items[4] == 2013:
            return middle
        elif self.items[4] == 1969:
            return right

    def zero(self, left, middle, right):
        if self.items[0] == 'ABNF':
            return left
        elif self.items[0] == 'PUG':
            return middle
        elif self.items[0] == 'M':
            return right

    def three(self, left, middle, right):
        if self.items[3] == 1979:
            return left
        elif self.items[3] == 1994:
            return middle
        elif self.items[3] == 2008:
            return right

    def one(self, left, middle, right):
        if self.items[1] == 1959:
            return left
        elif self.items[1] == 2019:
            return middle
        elif self.items[1] == 1964:
            return right

    def solve(self):
        return self.four(self.zero(self.three(self.one(0, 1, 2),
                                              3,
                                              4),
                                   5,
                                   self.three(6,
                                              self.one(7, 8, 9),
                                              10)),
                         11, 12)


def main(items):
    t = Tree(items)
    res = t.solve()
    return res


print(main(['PUG', 2019, 'LESS', 2008, 1965]))
print(main(['ABNF', 2019, 'FREGE', 1979, 2013]))
print(main(['M', 2019, 'LESS', 1994, 1965]))
print(main(['M', 1959, 'LESS', 1994, 1969]))
print(main(['M', 1959, 'FREGE', 2008, 1965]))
"""

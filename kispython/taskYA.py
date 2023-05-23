"""
def month(n, lan):
    dict1 = {1: "January",
             2: "February",
             3: "March",
             4: "April",
             5: "May",
             6: "June",
             7: "July",
             8: "August",
             9: "September",
             10: "October",
             11: "November",
             12: "December"}

    dict2 = {1: "Январь",
             2: "Февраль",
             3: "Март",
             4: "Апрель",
             5: "Май",
             6: "Июнь",
             7: "Июль",
             8: "Август",
             9: "Сентябрь",
             10: "Октябрь",
             11: "Ноябрь",
             12: "Декабрь"}
    if lan == 'en':
        return dict1[n]
    else:
        return dict2[n]


print(month(7, "ru"))
"""

"""
def can_eat(a, b):
    if a[0] + 1 == b[0] and a[1] + 2 == b[1]:
        return True
    elif a[0] - 1 == b[0] and a[1] + 2 == b[1]:
        return True
    elif a[0] - 1 == b[0] and a[1] - 2 == b[1]:
        return True
    elif a[0] + 1 == b[0] and a[1] - 2 == b[1]:
        return True
    elif a[0] - 2 == b[0] and a[1] + 1 == b[1]:
        return True
    elif a[0] - 2 == b[0] and a[1] - 1 == b[1]:
        return True
    elif a[0] + 2 == b[0] and a[1] + 1 == b[1]:
        return True
    elif a[0] + 2 == b[0] and a[1] - 1 == b[1]:
        return True
    return False

print(can_eat((5, 5), (6, 6)))
"""


def is_palindrome(a):
    if type(a) is int:
        a = str(a)
        return a == a[::-1]
    else:
        ans = ''
        for i in a:
            ans += str(i)
        return a == a[::-1]


print(is_palindrome([1, 3]))
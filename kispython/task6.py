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
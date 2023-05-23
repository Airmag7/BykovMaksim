def remove_duplicates(x):
    output = []
    control = set()
    for row in x:
        if row[0] in control:
            continue
        control.add(row[0])
        output.append(row)
    return output


def form(res):
    rr = []
    for row in res:
        r = []
        r1 = row[0][6:8] + '-' + row[0][3:5] + '-' + row[0][0:2]
        r2 = row[1].replace(' ', '-')
        r3 = row[2].replace('[at]', '@')
        r4 = "%.4f" % float(row[3])
        r.append(r1)
        r.append(r2)
        r.append(r3)
        r.append(r4)
        rr.append(r)
    return rr


def main(x):
    res = remove_duplicates(x)
    res = form(res)
    return res


print(main([['12.02.99', '586 755-4910', 'zomitidi33[at]yandex.ru', '0.8', 'zomitidi33[at]yandex.ru'], ['19.11.99', '065 270-9550', 'zabozman20[at]gmail.com', '0.1', 'zabozman20[at]gmail.com'], ['19.09.04', '477 463-2004', 'miroslav3[at]yandex.ru', '0.7', 'miroslav3[at]yandex.ru']]))
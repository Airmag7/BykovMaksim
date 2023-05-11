def remove_duplicates(x):
    output = []
    control = set()
    for row in x:
        if row[0] in control:
            continue
        control.add(row[0])
        output.append(row)
    return output


def transpose(A):
    C = []
    for i in range(len(A[0])):
        ci = []
        for j in range(len(A)):
            a = A[j][i]
            ci.append(a)
        C.append(ci)
    return C


def form(res):
    for row in res:
        row[0] = row[0].split('@')[0]
        row[1] = row[1].split(':')[0]
        row[1] = row[1].replace('1', 'да').replace('0', 'нет')
        s = row[1][1]
        s = s[2:5] + ' ' + s[5:8] + '-' + s[8:]
        res.append(s)
    return res


def main(x):
    res = remove_duplicates(x)
    res = form(res)
    res = transpose(res)
    return res


print(main([['vladislav7@gmail.com', '1:+70102810576'], ['gedizin22@yahoo.com', '1:+77158862030'], ['gedizin22@yahoo.com', '1:+77158862030'], ['gedizin22@yahoo.com', '1:+77158862030'], ['valerij16@mail.ru', '0:+70837169805']]))
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
    rr = []
    for row in res:
        r = []
        r1 = str(int(float(row[0])*100)) + '%'
        r2 = row[1][6:10] + '.' + row[1][3:5] + '.' + row[1][0:2]
        r3 = row[2].replace('true', '1').replace('false', '0')
        r4 = row[3].replace('+7(', '').replace(')', '').replace('-', '')
        r.append(r1)
        r.append(r2)
        r.append(r3)
        r.append(r4)
        rr.append(r)
    return rr


def sort(x):
    x.sort(key=lambda i: i[3])
    return x


def main(x):
    res = form(x)
    res = sort(res)
    res = transpose(res)
    return res


print(main([['0.9', '05.05.2002', 'true', '+7(407)093-24-88'], ['0.9', '01.03.2001', 'true', '+7(238)951-88-38'], ['0.8', '28.05.2001', 'false', '+7(904)725-92-92']]))
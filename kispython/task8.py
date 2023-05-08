'''
def main(string):
    string = string.replace('.do', '')
    string = string.replace('equ', '')
    string = string.replace('.end', '')
    string = string.replace('#', '')
    key = []
    val = []
    now1 = ''
    for i in range(len(string)):
        if string[i].isalpha() or string[i].isnumeric() or string[i] == '-' or string[i] == '_':
            now1 += string[i]
        elif string[i] == '=':
            nval = []
            key.append(now1)
            now1 = ''
        elif string[i] == ',':
            if now1 != '':
                nval.append(int(now1))
            now1 = ''
        elif string[i] == ')':
            if now1 != '':
                nval.append(int(now1))
            val.append(nval)
            now1 = ''
    return new_dict(key, val)


def new_dict(key, val):
    for k in key:
        if k == '':
            key.remove(k)

    dct = dict(zip(key, val))
    ans = []
    for item in dct.items():
        ans.append(item)
    return ans
'''
import re


def main(x):
    r = r"\(\(\s*.do\s*equ\s*([^, ]*)\s*=#\(\s*([^)]*)\)\s*.end"
    z = re.findall(r, x)
    ls2 = []
    str = ''
    for key, ints in z:
        ls = []
        for i in ints.split():
            str = str + i
        str = str.replace('#', '')
        str = str.replace(',', ' ')
        for i in str.split():
            ls.append(int(i))
        p = (key, ls)
        ls2.append(p)
    return ls2


print(main('(( .do equ isen =#( #-4023 ,#-1353 ,#-4971) .end .do equ ramabe=#(#1913 , #2963 , #6725 ) .end .do equ cere= #( #6776 ,#8103 , #8396 ,#3532) .end ))'))

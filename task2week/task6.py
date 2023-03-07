import pandas as pd
import random
#6.1
'''
str = pd.read_csv("лаб666.csv")
text = "Коллеги, " + str["2"][random.randint(0, 7)] + str["3"][random.randint(0, 7)]\
       + str["4"][random.randint(0, 7)] + str["5"][random.randint(0, 7)] + '\n'

len_text = random.randint(0, 20)
for i in range(len_text):
    for cl in str:
        a = random.randint(0, 7)
        text += str[cl][a] + " "
    text += '\n'
    abz = random.randint(0, 6)
    if abz >= 5:
        text += '\n'
print(text)
'''
#6.2
'''
f = open("текст.txt", encoding='utf-8')
a = f.read()
a = a.replace('\n', "")
a = a.split('.')
arr = [[] for _ in range(3)]
for x in a:
    x = x.split()
    s = len(x) // 3 + random.randint(-2, 2)
    arr[0].append(' '.join(x[:s]))
    arr[1].append(' '.join(x[s:s+s]))
    arr[2].append(' '.join(x[s+s:]))
print(arr[0], arr[1], arr[2], sep='\n')

for j in range(7):
    a, b, c = random.randint(0, len(arr[0])-1), random.randint(0, len(arr[0])-1), random.randint(0, len(arr[0])-1)
    print(f'{arr[0][a]} {arr[1][b]} {arr[2][c]}.')
'''
#6.3
'''
def gen_name():
    names
    otch
    name = names[random.randint(0, len(names)-1)]
    ot = otch[random.randint(0, len(otch)-1)].upper()
    len_surname = random.randint(2, 4)
    gl_cnt = 0
    sogl_cnt = 0
    surname = ''
    for _ in range(len_surname):
        a = random.randint(0, len(bukv)-1)
        if bukv[a] in gl:
            gl_cnt += 1
            sogl_cnt = 0
            surname += bukv[a]
        else:
            sogl_cnt += 1
            gl_cnt = 0
            surname += bukv[a]
        if gl_cnt >= 2:
            surname = surname + sogl[random.randint(0, len(sogl)-1)]
        if sogl_cnt >= 2:
            surname = surname + gl[random.randint(0, len(gl) - 1)]
    if surname[-1] in gl:
        surname = surname + fam_end_gl[random.randint(0, len(fam_end_gl)-1)]
    else:
        surname = surname + fam_end_sogl[random.randint(0, len(fam_end_sogl) - 1)]
    for b in bukv:
        surname = surname.replace(b*2, b)
    return f'{name} {ot}. {surname[0].upper() + surname[1:]}'


otch = 'абвгдежзиклмнопрстуфхцчш'
gl = "аиеоуэюя"
sogl = "бвгджзйклмнпрстфхцчш"
bukv = 'цукенгшздлорпавфячсмитбю'
fam_end_sogl = ["ин", "ев", "ин", "ян", "ев", "ов", "ини", "он", "ун"]
fam_end_gl = ["ли", "ски", "швили", "ску", "ских", "джи", "пулос"]
names = open("names.txt", encoding='utf-8').readlines()
for n in range(len(names)):
    names[n] = names[n].replace('\n', '')

for j in range(100):
    print(gen_name())
'''


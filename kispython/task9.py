from copy import *


def main(a):
    ans = []
    n = deepcopy(a)
    for i in range(len(a)):
        s = []
        n1 = n[i][0].split(';')
        n2 = n[i][0].split(' ')
        n3 = n[i][2].replace('@', '[at]')
        s.append(n2[1])
        s.append(n[i][1].replace(' ', '-'))
        s.append(f'{round(float(n1[0]), 1)}')
        s.append(n3)
        ans.append(s)
    return ans


print(main([['0.4781;Лев Татин', '204 582-7565', 'tatin88@yandex.ru'], ['0.0589;Борис Фумичко', '398 929-1969', 'fumicko59@gmail.com'], ['0.1908;Артемий Зенянц', '980 766-6681', 'artemij43@mail.ru'], ['0.9056;Данил Момебук', '240 238-2948', 'momebuk62@yahoo.com']]))

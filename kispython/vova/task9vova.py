from copy import *


def main(a):
    ans = []
    n = deepcopy(a)
    for i in range(len(a)):
        s = []
        del n[i][3]
        del n[i][2]
        n1 = n[i][0] + '0'
        n2 = n[i][1].replace('Y', 'Да').replace('N', 'Нет')
        n3 = n[i][2].split('.')
        n4 = n3[2].split('-')

        s.append(n1)
        s.append(n2)
        s.append(n3[0] + '.')
        s.append(n4[2])
        ans.append(s)
    return ans


print(main([['0.63', 'Y', None, 'Y', 'Табуфук Г.А.!18-10-1999'], ['0.43', 'N', None, 'N', 'Фифулин Р.Ц.!18-08-2001'], ['0.49', 'N', None, 'N', 'Зафибов С.К.!07-07-1999']]))
import math as m
# Электричество
start1 = 17949.0
end1 = 18030.0
k1 = 6.43
# ГВС
start2 = 352.926
end2 = 353.718
k2 = 243.16
# ХВС
start3 = 452.441
end3 = 455.157
k3 = 50.93

cost1 = (end1 - start1)*k1
cost2 = (end2 - start2)*k2
cost3 = (end3 - start3)*k3
print('Электричество: ', cost1, ' Округление: ', m.ceil(cost1))
print('ГВС: ', cost2, ' Округление: ', m.ceil(cost2))
print('ХВС: ', cost3, 'Округление: ', m.ceil(cost3))
print('Сумма: ', m.ceil(cost1) + m.ceil(cost2) + m.ceil(cost3))

'''
x = ''
var = [0xf or x in 'abc']
print(var)
'''

'''
i = 0 
print('muchcodewow'[:i+4])

'''

s = ['1', '2', 12, 2]
x = 2
a = 0

s = [int(s[i]) for i in range(len(s))]
print(s)

print(len(set(s)))

print(s[::-1])

s = ['sdsdbadva', 'evaa', 'avu,bd']
print(max(len(s[i]) for i in range(len(s))))
###########
s = 'AAABBCCCDEFA'
lst = set([x for x in s])
lst_dictionary = dict.fromkeys(lst, 0)
for x in s:
    lst_dictionary[x] += 1
print(lst_dictionary)

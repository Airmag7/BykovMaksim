arr = input('1.txt')
disp = 0
sr = 0
for i in range(0, len(arr)):
    sr += arr[i]
sr = sr/len(arr)
for i in range(0, len(arr)):
    disp += (arr[i]-sr)**2
disp = disp/(len(arr) - 1)

arr = sorted(arr)
if len(arr) % 2 == 1:
    med = arr[len(arr)//2 - 1]
else:
    med = (arr[len(arr)//2 - 1] + arr[len(arr)//2])/2
print('Выборочное среднее: ', sr)
print('Дисперсия: ', disp)
print('Среднеквадратическое отклонение: ', disp**0.5)
print('Медиана: ', med)
print('Коэффициент вариации: ', disp**0.5/sr)

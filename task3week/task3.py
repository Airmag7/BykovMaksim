import csv
import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from collections import defaultdict


def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')


def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))


# id, task, variant, group, time
mesages = load_csv('messages (3).csv')

# id, message_id, time, status
checks = load_csv('checks (1).csv')
#print(checks)

# task, variant, group, time, status, achievements
statuses = load_csv('statuses (1).csv')
#print(statuses)

games = load_csv('GAMES.csv')


for i in range(len(mesages)):
    mesages[i][4] = parse_time(mesages[i][4])
    mesages[i][2] = int(mesages[i][2]) + 1
    mesages[i][1] = int(mesages[i][1]) + 1
    mesages[i][0] = int(mesages[i][0])

for j in range(1, len(checks)):
    checks[j][3] = int(checks[j][3])
    checks[j][1] = int(checks[j][1])
    checks[j][0] = int(checks[j][0])

for k in range(len(statuses)):
    statuses[k][0] = int(statuses[k][0]) + 1
    statuses[k][1] = int(statuses[k][1]) + 1
    statuses[k][3] = parse_time(statuses[k][3])
    statuses[k][4] = int(statuses[k][4])
    statuses[k][5] = statuses[k][5].replace('"', '').replace('[', '').replace(']', '').split(',')

for t in range(len(games)):
    games[t] = games[t][0].split(';')
    games[t][1] = games[t][1].replace('"', '')
    games[t][3] = games[t][3].replace('"', '')
    if games[t][3] == "не издана":
        games[t][3] = None
    else:
        games[t][3] = int(games[t][3])

# Задание 1
'''
labels = ["Понедельник",
          "Вторник",
          "Среда",
          "Четверг",
          "Пятница",
          "Суббота",
          "Воскресенье"]

dotw = [0, 0, 0, 0, 0, 0, 0]
for msg in mesages:
    dotw[datetime.datetime.weekday(msg[4])] += 1
fig1, ax1 = plt.subplots()
ax1.pie(dotw, labels=labels, autopct='%1.2f%%')
plt.show()
'''

# Задание 2
'''
hours = [f'{i}:00' for i in range(24)]
hours_work = [0] * 24
for msg in mesages:
    hours_work[msg[4].hour] += 1

plt.bar(hours, hours_work)
plt.show()
'''


# Задание 3
'''
student = defaultdict(list)
sum_student = 0
for st in statuses:
    student[st[2]].append(st[1])
for key in student:
    student[key] = set(student[key])
for stdnt in student:
    sum_student += len(student[stdnt])
tasks = [i for i in range(1, 9)]
tasks_info = [0] * 8
for msg in mesages:
    tasks_info[msg[1]-1] += 1
tasks_info = [ti / sum_student for ti in tasks_info]
plt.bar(tasks, tasks_info)
plt.show()
'''

# Задание 4
# Ось x - дни, Ось y - кол-во сообщений по заданию
'''
fig, axs = plt.subplots(2, 4)
task_day = defaultdict(int)
x = [i for i in range(1, 33)]
for msg in mesages:
    a = msg[1]
    b = msg[4]
    if b.month == 2:
        b = b.day - 7
    else:
        b = b.day - 7 + 28
    task_day[(a, b)] += 1
y = [[] for _ in range(8)]

for i in range(8):
    for j in range(1, 33):
        y[i].append(task_day[(i+1), j])
axs[0, 0].plot(x, y[0])
axs[0, 0].set_title('Задание 1')
axs[0, 1].plot(x, y[1])
axs[0, 1].set_title('Задание 2')
axs[0, 2].plot(x, y[2])
axs[0, 2].set_title('Задание 3')
axs[0, 3].plot(x, y[3])
axs[0, 3].set_title('Задание 4')
axs[1, 0].plot(x, y[4])
axs[1, 0].set_title('Задание 5')
axs[1, 1].plot(x, y[5])
axs[1, 1].set_title('Задание 6')
axs[1, 2].plot(x, y[6])
axs[1, 2].set_title('Задание 7')
axs[1, 3].plot(x, y[7])
axs[1, 3].set_title('Задание 8')

plt.show()
'''

# Задание 5
'''
student = defaultdict(int)
for msg in mesages:
    student[msg[3]] += 1
labels = []
values = []
for key, val in student.items():
    labels.append(key)
    values.append(val)
print(values, labels)
plt.barh(labels, values)
plt.show()
'''

# Задание 6
'''
groups = defaultdict(int)
for st in statuses:
    if st[4] == 2:
        groups[st[2]] += 1
labels = []
values = []
for key, val in groups.items():
    labels.append(key)
    values.append(val)
print(values, labels)
plt.barh(labels, values)
plt.show()
'''

# Задание 7
# (Метрика сложности - отношение правильный решений к неправильным)
'''
tasks = [i for i in range(1, 9)]
tasks_info = defaultdict(int)
tasks_info2 = defaultdict(int)
for st in statuses:
    if st[4] == 3:
        tasks_info2[st[0]] += 1
    elif st[4] == 2:
        tasks_info[st[0]] += 1
ans = [tasks_info[i]/tasks_info2[i] for i in tasks]
fig1, ax1 = plt.subplots()
ax1.pie(ans, labels=tasks, autopct='%1.2f%%')
plt.show()
'''

# Задание 8
'''
groups = defaultdict(int)
for st in statuses:
    if st[5] != ['']:
        groups[st[2]] += len(st[5])
labels = []
values = []
for key, val in groups.items():
    labels.append(key)
    values.append(val)
print(values, labels)
plt.barh(labels, values)
plt.show()
'''

# Задание 9
'''
student_achievement = defaultdict(int)
for st in statuses:
    a = st[1]
    b = st[2]
    if st[5] != ['']:
        student_achievement[(a, b)] += len(st[5])
ans = sorted(student_achievement.items(), key = lambda i: i[1], reverse=True)[:10]
labels = []
values = []
for a in ans:
    labels.append(f'{a[0][0]} вар.\n {a[0][1]}')
    values.append(a[1])
plt.bar(labels, values)
plt.show()
'''

# Задание 10
'''
groups = defaultdict(int)
for st in statuses:
    if st[5] != [''] and len(st[5]) > 1:
        groups[st[2]] += 1
labels = []
values = []
for key, val in groups.items():
    labels.append(key)
    values.append(val)
print(values, labels)
plt.barh(labels, values)
plt.show()
'''

# Задание 11
'''
years = [i for i in range(1981, 2009)]
values = [0] * 28
for g in games:
    if g[3] != None:
        values[g[3]-1981] += 1

fig, ax = plt.subplots()
ax.plot(years, values)
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
plt.show()
'''

# Задание 12
'''
jenres = defaultdict(dict)
years = [i for i in range(1981, 2009)]
del years[years.index(2006)]
for g in games:
    if g[1] in jenres[g[3]]:
        jenres[g[3]][g[1]] += 1
    else:
        jenres[g[3]][g[1]] = 1
del jenres[None]
popular = defaultdict(int)
values = []
label = ''
for key in jenres:
    ans = ''
    max_ans = 0
    for k in jenres[key]:
        if jenres[key][k] > max_ans:
            max_ans = jenres[key][k]
            ans = k
    popular[ans] += 1
    label += ans[:3] + '    '
    values.append(max_ans)
print(popular)
plt.plot(years, values)
plt.xlabel(label)
plt.show()
'''
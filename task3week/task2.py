'''
import matplotlib.pyplot as plt
import random
import math

a = 8
b = 8
data = [[0 for i in range(a)] for i in range(b)]
for i in range(a):
    for j in range(math.ceil(a / 2)):
        x = random.randint(0, 1)
        data[i][j] = x
        data[i][b - 1 - j] = x
plt.imshow(data, cmap="Greys_r")
plt.show()
'''

import matplotlib.pyplot as plt
import random
import math

a = 8
b = 8
c = 100
d = 150
data = [[0 for i in range(a)] for i in range(b)]
data1 = [[0 for i in range(c)] for i in range(d)]
for k in range(c):
    for h in range(d):
        for i in range(a):
            for j in range(math.ceil(a / 2)):
                x = random.randint(0, 1)
                data[i][j] = x
                data[i][b - 1 - j] = x
        data1[k][h] = data
plt.imshow(data1, cmap="Greys_r")
plt.show()

import numpy as np
import random
m = int(input('Введіть значення m: '))
n = int(input('Введіть значення n: '))
masiv1 = np.zeros((m, n))
for i in range(m):
    for j in range(n):
        masiv1[i][j] = random.randint(1,31)
masiv2 = np.zeros((m, n))
for a in range(m):
    for b in range(n):
        masiv2[a][b] = random.randint(31,51)
print(masiv1 + masiv2.min())
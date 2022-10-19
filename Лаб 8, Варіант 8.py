from array import *
import random
import math
a = int(input("Введіть розмір масиву: "))
b= 1
v = 1
k = 0
masiv = array('i', [])
for i in range(a):
    x = random.randint(1,10)
    masiv.append(x)
print(masiv)
for c in masiv:
    if c%2 == 0:
        print("Масив має парні числа: ", c)
        b = b*c
        k +=1
if k>0:
    v = math.pow(b,(1./k))
    print("Середне геометричне", str(v))
else:
    print("Неможливо становити середне геометричне")


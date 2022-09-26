import math
a = float(input("Введіть значення a: "))
b = float(input("Введіть значення b: "))
h = float(input("Введіть значення h: "))
list_items = []
while a < b:
    list_items.append(math.log(3, math.fabs(a + math.e**a)))
    a += h
m = 0
while m != len(list_items):
    print(list_items[m])
    m += 1
d = 0
for k in range(0,len(list_items)):
    d += list_items[k]
print("Середне арифметичне = " + str(d/len(list_items)))
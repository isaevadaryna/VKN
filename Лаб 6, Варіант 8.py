import math
a = float(input("Введіть значення a: "))
b = float(input("Введіть значення b: "))
h = float(input("Введіть значення h: "))
for v in range(1, 100):
    w = math.log(3, math.fabs(v + math.e**v))
    v = v + h
    print(w)
    if v >= b:
        break

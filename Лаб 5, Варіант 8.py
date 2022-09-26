import math
x = float(input("Введіть значня x: "))
y = 0.0
if x>=7.2:
    y = math.log(4, math.fabs(x+1))
    print(y)
elif x>5.11:
    y = (math.log2(math.fabs(math.cos(x))))**(1./2.)
    print(y)
else:
    y = math.pow(x,2)+4*math.fabs(x-4)+math.e**x
    print(y)



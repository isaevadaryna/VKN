import math
def func1(x1,x2,x3):
    z = (math.pow(x1,3))**(1./2.) + math.pi**2 + math.e**x2+1 + x3 + (math.tan(x3))**(1./2.)
    return(z)
x = float(input("Введіть значення x: "))
y = float(input("Введіть значення y: "))
m = float(input("Введіть значення m: "))
w = func1(x, y, m)
print(w)
input()

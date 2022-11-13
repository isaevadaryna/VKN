import math
def area_cylinder():
    R = int(input("Введіть радіус циліндра: "))
    H = int(input("Введіть висоту циліндра: "))
    Sb = 2*math.pi*R*H
    So = math.pi*(R^2)
    Spp= (2*So) + Sb
    V = math.pi*(R^2)*H
    return (Sb, Spp, V)
a = area_cylinder()
print(a)

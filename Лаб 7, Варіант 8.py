s1 = input("Введіть рядок: ")
s2 = input("Введіть рядок: ")
for i in s1:
    if not i in s2:
        s1 += i
        print(s1)
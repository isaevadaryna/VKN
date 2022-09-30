s = input('Введіть цілі числа:  ')
s1 = ''
a = 0
while True:
    s1 += 'x=' + s[a] + ' '
    a += 2
    if a > len(s):
        break
print(s1)
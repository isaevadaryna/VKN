T = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
a = input("Введіть велику англ. літеру: ")
N = int(input("Введіть кількість літер, N = "))
r = []
N1 = T.index(a)
N2 = N1+N*4
if a in T:
    if N2<27:
        r = T[N1:N2]
        for i in range(4):
            T1 = r[i*4:i*4+N]
            print('Сторона квадрата:', i + 1, ' ', T1)
    else:
        r = T[N1:27]+T[0:N2-27]
        for i in range(4):
            T2 = r[i*4:i*4+N]
            print('Сторона квадрата:', i+1, ' ', T2)



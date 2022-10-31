A = set()
B = set()
C = set()
for i in range(1,201):
    if i%4 == 0:
        A.add(i)
print(A)

for x in range(1,201):
    if x%3 == 0:
        B.add(x)
print(B)

for y in range(1,201):
    if y%5 == 0:
        C.add(y)
print(C)
K12 = A.union(B) #ті елементи множини А, які є  множині В
print(K12)
F = B.union(C)
print(F)
V = A.union(C)
print(V)
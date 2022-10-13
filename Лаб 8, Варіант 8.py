from array import *
import random
a = int(input("Введіть розмір масиву: "))
masiv = array('i', [a])
for i in range(a):
    masiv1 = random.randint(1,10)
    print(masiv1)
for c in masiv:
    if c/2 in masiv:
        b = (c*c)**(1./len(c*c))
    print("Середне геометричне", str(b))


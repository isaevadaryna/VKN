import random
def choice(a,b,c):
    return (a+b+c)

if __name__ =="__main__":
    for i in range(1,11):
        num1 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        num2 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        num3 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        print("Номери з рандомних букв: ", num1+num2+num3)
if __name__ =="__main__":
    for x in range(1,13):
        letter1 = "Q"
        letter2 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        letter3 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        print("Номер з Q:", letter1+letter2+letter3)
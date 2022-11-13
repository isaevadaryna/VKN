def countVowels():
   vowels = ['а','о','у','и','і','е']
   total = 0
   string = input("Введіть речення українською: ")
   for s in string:
      if s in vowels:
         total += 1
   return total
a = countVowels()
print(a)




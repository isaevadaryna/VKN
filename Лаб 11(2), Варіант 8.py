import json
data = {}
a = int(input('len of word = '))
x = 'book.txt'
f = open(x, "rt")
with open('book.txt', 'rt') as file:
   text = file.read()
   line = text.split()
   for word in line:
       word.replace('.', ' ').replace(',', ' ').replace(':', ' ').replace(';', ' ').replace('?', ' ')
       if len(word) == a:
           with open('words.json', 'w') as f:
               json.dump(word, f)

print('Запис виконано')

file.close()

            #читається як звичайний файл, але записується у json файл
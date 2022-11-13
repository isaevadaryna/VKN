import csv
import random
with open('quest.csv', newline='') as f:
    reader = csv.reader(f)
    spisok = list(reader)
    random.shuffle(spisok)
    print(spisok)
f.close()

import os
import shutil
count = 0
os.mkdir("west")
source = "C:\\ICS-ІсаєваДарина"
dest = 'C:\\ICS-ІсаєваДарина/west'
file = files = os.listdir(source)
for f in files:
    if f.startswith("w"):
        shutil.move(f, dest)
for path in os.listdir(dest):
    if os.path.isfile(os.path.join(dest, path)):
        count += 1
        print("Кількість файлів:", count)
print("Виконано")
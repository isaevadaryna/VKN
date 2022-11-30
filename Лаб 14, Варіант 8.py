import requests
from bs4 import BeautifulSoup
a = input("Введіть посилання: ")
r = requests.get(a)
if r.status_code == 200:
    wbs = BeautifulSoup(r.text, 'html.parser')
    with open('URL-посилання.txt', 'w') as file:
        for link in wbs.find_all("a"):
                if 'href' in link.attrs:
                    #with open('URL-посилання.txt', 'w') as file:
                        file.write(link['href'])
    file.close()
print("Запис виконано")
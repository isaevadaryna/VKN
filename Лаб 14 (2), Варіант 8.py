import json
import re
import requests
from bs4 import BeautifulSoup

r = requests.get('http://tpgnpu.ho.ua')
data = r.text
soup = BeautifulSoup(data, "html.parser")

for i in soup.find_all(href=re.compile("mailto")):
    with open('електроні адреси.json', 'w') as f:
        a = i.string
        json.dump(a, f)
    print('Done')
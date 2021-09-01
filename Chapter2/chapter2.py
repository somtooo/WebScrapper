from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')

nameList = bs.find_all('span', {'class': 'green'})
for name in nameList:
    print(name.get_text())

# Navigating Trees

# Theres a difference btw descendants and children note beautiful soup only looks at descendants

# Code for finding children
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

for child in bs.find('table', {'id': 'giftList'}).children:
    print(child)


for sibling in bs.find('table', {'id':'giftList'}).tr.next_siblings:
    print(sibling)
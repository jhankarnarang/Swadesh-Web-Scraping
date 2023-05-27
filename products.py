from bs4 import BeautifulSoup , NavigableString
import requests
import csv
import pandas as pd

source = requests.get('https://www.merinolaminates.com/en/design/10002-mangfall-beech/?cat=65')
soup = BeautifulSoup(source.content, 'lxml')


prod_name = soup.find('div',class_='Name').h1.text.replace('\n','')
print(prod_name)
prod_colour = soup.find('div',class_='Name').p.text
print(prod_colour)

prod_img = soup.find('div',class_='ProductImage').img['src']
print(prod_img)

for table in soup.select_one('div>div.accordion__content_inner'):
    print(table)


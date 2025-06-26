from bs4 import BeautifulSoup as bs
import requests

URL = 'https://news.ycombinator.com'
respons = requests.get(URL)
html = respons.text
soup = bs(html,'lxml')

names = soup.find_all('td',class_ = 'title')

for name in names:
    titell = soup.find('span', class_='titleline').find('a').get('href')
    print(titell)
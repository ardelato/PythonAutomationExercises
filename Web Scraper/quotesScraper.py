import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'
response = requests.get(url)

# Will retrieve the text information from the website, and will parse it with lxml format
soup = BeautifulSoup(response.text,'lxml')
quotes = soup.find_all('span',class_='text')
authors = soup.find_all('small',class_='author')
tags = soup.findAll('div',class_='tags')


for i in range(0,len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    quoteTags = tags[i].find_all('a',class_='tag')

    for quoteTag in quoteTags:
        print(quoteTag.text)
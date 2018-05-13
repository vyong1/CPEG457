from newsapi import NewsApiClient
from bs4 import BeautifulSoup
import urllib
import requests
import json

newsapi = NewsApiClient(api_key='6e1a2d3c4b0b449d9e76fb7b297c25d4')



cat = "business"
categoryTitle = (cat[0].upper() + cat[1:]) + "Titles.txt"
categoryCollection = (cat[0].upper() + cat[1:]) + "Collection.txt"


collectionFile = open(categoryCollection,"a", encoding='utf-8')


titles = {}
titleFile = open(categoryTitle,"r",encoding='utf-8')
for line in titleFile:
    titles[line] = 0
titleFile.close()

titleFile = open(categoryTitle,"a", encoding='utf-8')


top_headlines = newsapi.get_top_headlines(country='us',category= cat, language='en')

articles = top_headlines["articles"]

for article in articles:
    title = article["title"]
    print(title)
    if not((title + "\n") in titles):
        print("***" + title)
        url = article["url"]
        headers = {'User-Agent':'Mozilla/5.0'}
        #html = urllib.request.urlopen(url)
        html = requests.get(url)
        soup = BeautifulSoup(html.text,'html.parser')

        text = title + "\n"

        p_tags = soup.find_all("p")
        for tag in p_tags:
            text += " " + tag.get_text()

        titleFile.write(title + "\n")
        collectionFile.write("\n" + text)

titleFile.close()
collectionFile.close()

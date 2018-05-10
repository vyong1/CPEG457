# python lib imports
import urllib
import os
# local imports
from HtmlElement import HtmlElement
# aylien news api imports
import aylien_news_api
from aylien_news_api.rest import ApiException
# nltk imports
import nltk
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
# beatiful soup import
from bs4 import BeautifulSoup


# Establish the path to java
java_path = "C:/Program Files/Java/jdk-10.0.1/bin/java.exe"
os.environ['JAVAHOME'] = java_path

# Configure API key authorization: app_id
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = '59793aeb'
# Configure API key authorization: app_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = '6557890cdc6ffabe3203700616bcb1fb'

# create an instance of the API class
#api_instance = aylien_news_api.DefaultApi()

# This needs to be changed to match your NER directory
#st = StanfordNERTagger('C:/Users/Frank/My Documents/Search and Data Mining/CPEG457/WebApp/python/Aylien_api/NER/classifiers/english.all.3class.distsim.crf.ser.gz',
 #                        'C:/Users/Frank/My Documents/Search and Data Mining/CPEG457/WebApp/python/Aylien_api/NER/stanford-ner.jar',
  #                       encoding='utf-8')

input_url = "http://www.foxnews.com/politics/2018/05/10/trumps-summit-with-kim-jong-un-set-for-june-12-in-singapore-president-says.html"

# tagged_text = Aylien_api.getStories.createTags(Aylien_api.getStories.createRawText(input_url))
# possible_authors = Aylien_api.getStories.createPossibleAuthor(tagged_text)
# print(possible_authors)

html = urllib.request.urlopen(input_url)
soup = BeautifulSoup(html, 'html.parser')
raw_text = soup.get_text()
#print(soup)
byline_index = str(soup).find('author-byline')
byline = ''
for i in range(0, 50):
    byline += str(soup)[byline_index + i]

print(byline)
author_dict = {}

# for author in possible_authors:
#     if author in author_dict.keys():
#         author_dict[author] += 1
#     else:
#         author_dict[author] = 1

#for author in author_dict:
#    print(author + ':' + str(author_dict[author]))
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
# Regular Expression import
import re


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

input_url = "https://www.cnn.com/2018/05/11/politics/donald-trump-foreign-policy/index.html"

# tagged_text = Aylien_api.getStories.createTags(Aylien_api.getStories.createRawText(input_url))
# possible_authors = Aylien_api.getStories.createPossibleAuthor(tagged_text)
# print(possible_authors)

html = urllib.request.urlopen(input_url)
soup = BeautifulSoup(html, 'html.parser')
raw_text = soup.get_text()
#print(soup)
def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

def getByline(inputSoup):
    byline_index = str(inputSoup).find('by')
    htmlLine = ''
    byline = ''
    flag = False

    for i in range(-20, 20):
        htmlLine += str(inputSoup)[byline_index + i]

    for j in htmlLine:
        if(j == '"'):
            flag = not flag
        elif(flag):
            byline += j
    print(byline)
    output = inputSoup.find(class_ = byline)
    return output

def searchAuthor(inputSoup, possibleAuthor):
    author_indexes = find_all(str(inputSoup), possibleAuthor)
    allLines = []
    currentLine = '' 
    line_count = 0
    for element in author_indexes:
        for i in range(-30, 30):
            currentLine += str(inputSoup)[element + i]
        allLines.append(currentLine)
        currentLine = ''
    return allLines

print(searchAuthor(soup, 'Stephen Collinson'))
author_dict = {}

# for author in possible_authors:
#     if author in author_dict.keys():
#         author_dict[author] += 1
#     else:
#         author_dict[author] = 1

#for author in author_dict:
#    print(author + ':' + str(author_dict[author]))
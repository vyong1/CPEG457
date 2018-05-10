# python lib imports
import urllib
import os
import json
# local imports
from HtmlElement import HtmlElement
from Wikipedia_api.WikipediaAPI import *
from PipeFile import PipeFile
import CardBuilder
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
java_path = "C:/ProgramData/Oracle/Java/javapath/java.exe"
os.environ['JAVAHOME'] = java_path

# Configure API key authorization: app_id
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = '59793aeb'
# Configure API key authorization: app_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = '6557890cdc6ffabe3203700616bcb1fb'

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()

# This needs to be changed to match your NER directory
st = StanfordNERTagger('python/Aylien_api/NER/classifiers/english.all.3class.distsim.crf.ser.gz',
                         'python/Aylien_api/NER/stanford-ner.jar',
                         encoding='utf-8')


def authorDict():
    input_url = "https://www.cnn.com/2018/05/05/politics/trump-nra-speech-angers-french/index.html"

    tagged_text = Aylien_api.getStories.createTags(Aylien_api.getStories.createRawText(input_url))
    possible_authors = Aylien_api.getStories.createPossibleAuthor(tagged_text)
    print(possible_authors)

    html = urllib.request.urlopen(input_url)
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.h1)

    author_dict = {}

    for author in possible_authors:
        if author in author_dict.keys():
            author_dict[author] += 1
        else:
            author_dict[author] = 1

    for author in author_dict:
        print(author + ':' + str(author_dict[author]))
    
def wikiApiTest():
    print(CardBuilder.buildWikipediaCard('Will Smith'))

wikiApiTest()

from py_html.HtmlElement import HtmlElement
import aylien_news_api
import urllib
import nltk
from aylien_news_api.rest import ApiException
from bs4 import BeautifulSoup
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
import os
import Aylien_api.getStories
java_path = "C:/ProgramData/Oracle/Java/javapath/java.exe"
os.environ['JAVAHOME'] = java_path

# Only need to run this once
# nltk.download('punkt')


# Configure API key authorization: app_id
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'c45042a9'
# Configure API key authorization: app_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = 'a9270fe1446fc3fb7c8e8196ed52e626'

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()

# This needs to be changed to match your NER directory
st = StanfordNERTagger('python/Aylien_api/NER/classifiers/english.all.3class.distsim.crf.ser.gz',
                         'python/Aylien_api/NER/stanford-ner.jar',
                         encoding='utf-8')

input_url = "https://www.cnn.com/2018/05/05/politics/trump-nra-speech-angers-french/index.html"

tagged_text = Aylien_api.getStories.createTags(Aylien_api.getStories.createRawText(input_url))
possible_authors = Aylien_api.getStories.createPossibleAuthor(tagged_text)
print(possible_authors)

html = urllib.request.urlopen(input_url)
soup = BeautifulSoup(html, 'html.parser')
print(soup.h1)

author_dict = {}

for author in possible_authors:
    if author in author_dict.keys():
        author_dict[author] += 1
    else:
        author_dict[author] = 1

for author in author_dict:
    print(author + ':' + str(author_dict[author]))
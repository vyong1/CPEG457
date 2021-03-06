import aylien_news_api
import urllib
import nltk
from aylien_news_api.rest import ApiException
from bs4 import BeautifulSoup
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
import os
java_path = "C:/Program Files/Java/jdk-10.0.1/bin/java.exe"
os.environ['JAVAHOME'] = java_path
default_count = 10
# Only need to run this once
# nltk.download('punkt')


# Configure API key authorization: app_id
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'f780bd2f'
# Configure API key authorization: app_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = '43157cd86a0c9ef77da72df2450d5da0'

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()

# This needs to be changed to match your NER directory
st = StanfordNERTagger('python/StanfordNER/classifiers/english.all.3class.distsim.crf.ser.gz',
                         'python/StanfordNER/stanford-ner.jar',
                         encoding='utf-8')

################################################

# Function Declarations

################################################

def getStories(author_name, count=default_count):
    # Takes in authors name, sets it as an option for the api
    opts = {
      'author_name': author_name,
      'per_page': count
    }

    try:
        # Creates an associative array of the stories
        api_response = api_instance.list_stories(**opts)
        return api_response
    except ApiException as e:
        print("Exception when calling DefaultApi->list_stories: %sn" % e)
        
def createRawText(url):
    # takes in the url and creates the raw HTML text
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    raw_text = soup.get_text()
    return raw_text

def createTags(raw_text):
    tokenized_text = word_tokenize(raw_text)
    classified_text = st.tag(tokenized_text)
    return classified_text

def createPossibleAuthor(tags):
    author_list = []
    x = 0
    while x < len(tags):
        if (tags[x][1] == 'PERSON'):
            name = tags[x][0]
            if (tags[x + 1][1] == 'PERSON'):
                name += " " + tags[x + 1][0]
                x += 1
            author_list.append(name)
        x += 1
    return author_list
           
def showMore():
    global default_count
    default_count += 10
    return

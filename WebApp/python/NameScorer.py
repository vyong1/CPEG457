# python lib imports
import urllib
import os
# local imports
from PipeFile import *
# aylien news api
import aylien_news_api
from aylien_news_api.rest import ApiException
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'f780bd2f'
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = '43157cd86a0c9ef77da72df2450d5da0'
# nltk
import nltk
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
# beatiful soup import
from bs4 import BeautifulSoup
# Regular Expression import
import re
# Establish the path to java
os.environ['JAVAHOME'] = "C:/Program Files/Java/jdk-10.0.1/bin/java.exe"

# Create an aylien news api instance
AYLIEN_INSTANCE = aylien_news_api.DefaultApi()

class NameScorer:
    '''Scores names in an article'''
    def __init__(self, url: str):
        self.url = url
        self.authorDict = {}

    def requestArticle(self) -> BeautifulSoup:
        '''Requests the raw HTML from the url then converts
        it to bs4 soup'''
        html = urllib.request.urlopen(self.url)
        return BeautifulSoup(html, 'html.parser').prettify(formatter="html")
    
    def parseText(self, soup: BeautifulSoup) -> dict:
        '''Parses text for authors with the help
        of bs4 and Stanford NER'''
        
        pass
        
    def findAuthorOccurrences(self):
        '''Find occurrences of author text'''
        pass

    ###
    # Entry point of the API - make everything else private later
    #
    def score(self, url: str) -> dict:
        '''Given a url, request the html and score the possibility
        that each person mentioned in the article is an author'''
        # Request the article
        # Extract the raw text using bs4
        # Find occurrences of the author name, and the surrounding text
        # Parse surrounding text to score
        pass
    
class Occurrence:
    '''Indicates an occurrence of an author in text'''
    def __init__(index: int, surroundingText: str):
        self.index = index
        self.surroundingText = surroundingText

class Author:
    '''An author class with score and occurrences
    in the text'''
    def __init__(self, name: str):
        self.name
        self.score = 0
        self.occurrences = []
    
    def addOccurrence(self, occurrence) -> Author:
        self.occurrences.append(occurrence)
        return self
    
    def setScore(self, score: int) -> Author:
        self.score = score
        return self

class AuthorDict:
    '''A wrapper for a dictionary of authors (name : author)'''
    def __init__(self):
        self._authors = {}

    def __getitem__(self, authorName: str) -> Author:
        '''Indexer method'''
        return self._authors[authorName]

    def addAuthor(self, auth: Author):
        '''Adds an author (with no occurrences)'''
        if auth.name in self._authors:
            return
        else:
            self._authors[auth.name] = author
    


# TEST CODE STARTS HERE
scorer = NameScorer("http://www.foxnews.com/world/2018/05/15/gave-us-trucks-and-ammunition-to-al-qaeda-chaotic-us-effort-to-arm-syrian-rebels.html")
print(scorer.requestArticle())
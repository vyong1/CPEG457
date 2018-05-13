# python lib imports
import urllib
import os
# local imports
import HtmlElement
import getStories
import NameStats
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
default_count = 10

# Configure API key authorization: app_id
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = '59793aeb'
# Configure API key authorization: app_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = '6557890cdc6ffabe3203700616bcb1fb'

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()
author_dict = {}


def checkLine(line, author):
    if(line.find(author) == -1):
        return False
    else:
        return True

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

def getByline(inputSoup):
    # Finds the first use of by in the html. Results are inconsistent
    byline_index = str(inputSoup).find('byline')
    htmlLine = ''
    if (byline_index < 0):
        byline_index = str(inputSoup).find('by')
        for i in range(-40, 40):
            htmlLine += str(inputSoup)[byline_index + i]
    else:
        for i in range(-100, 100):
            htmlLine += str(inputSoup)[byline_index + i]
    return htmlLine

def searchAuthor(inputSoup, possibleAuthor):
    authorIndexes = find_all(str(inputSoup), possibleAuthor)
    allLines = []
    currentLine = '' 
    for element in authorIndexes:
        for i in range(-100, 30):
            currentLine += str(inputSoup)[element + i]
        allLines.append(currentLine)
        currentLine = ''
    return allLines

def findAuthor(inputSoup, author):
    # Simple way to look for author. Needs fine tuning
    byline = getByline(inputSoup)
    if(checkLine(byline, author)):
        return True
    else:
        authorOccurrences = searchAuthor(inputSoup, author)
        for line in authorOccurrences:
            if(checkLine(line, 'author') or checkLine(line, 'byline')):
                return True
    return False


def createAuthorDict(authorList):
    # Creates a dictionary for the possible authors in the article. 
    global author_dict
    author_dict = {}
    for author in authorList:
        if author in author_dict.keys():
            author_dict[author] += 1
        else:
            author_dict[author] = 1
    return


def compileAuthors(url):
    # Gathers and Refines the author search
    rawText = getStories.createRawText(url)
    tags = getStories.createTags(rawText)
    authorList = getStories.createPossibleAuthor(tags)
    createAuthorDict(authorList)
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    refinedList = restrictAuthors(soup)
    print(refinedList)
    return max(refinedList, key=refinedList.get)

def restrictAuthors(inputSoup):
    # Restricts the author list based on different criteria. Currently just by count
    newAuthorList = {}
    location = 0
    global author_dict
    title = str(inputSoup.find('h1'))
    for author in author_dict:
        if(title.find(author) == -1):
            if(author_dict[author] < 5 and author.find(' ') > 0):
                newAuthorList[author] = 30 - location
            elif(author_dict[author] < 7 and author.find(' ') > 0):
                newAuthorList[author] = 25 - location
        location += 1
    for element in newAuthorList:
        if (newAuthorList[element] > 20):
            if(findAuthor(inputSoup, element)):
                newAuthorList[element] += 30
    return newAuthorList

def storyList(author):
    result = getStories.getStories(author)
    return result
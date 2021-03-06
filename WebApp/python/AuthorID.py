# python lib imports
import urllib
import os
# local imports
import HtmlElement
import getStories
from PipeFile import *  
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
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'f780bd2f'
# Configure API key authorization: app_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = '43157cd86a0c9ef77da72df2450d5da0'

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()



def __checkLine(line, author):
    # Checks if the author's name is in the current line of text
    if(line.find(author) == -1):
        return False
    else:
        return True

def __findAll(a_str, sub):
    # Finds all instances of author in the text
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

def __getByline(inputSoup):
    # Finds the first use of by in the html. Results are inconsistent
    byline_index = str(inputSoup).find('byline')
    if (byline_index < 0): # byline not found
        byline_index = str(inputSoup).find('by')
    # Extract text after 'byline' or 'by'
    byline = str(inputSoup)[byline_index: byline_index + 200]
    return byline

def __searchAuthor(inputSoup):
    # Returns the lines of text that contain 'author'
    authorIndexes = __findAll(str(inputSoup), 'author')
    allLines = []
    for element in authorIndexes:
        currentLine = '' 
        for i in range(-60, 60):
            currentLine += str(inputSoup)[element + i]
        allLines.append(currentLine)
        currentLine = ''
    return allLines

def __findAuthor(inputSoup, author, byline, authorOccurrences):
    # Looks for the author in the lines of text that contain 'author'
    if(__checkLine(byline, author)):
        return True
    else:
        for line in authorOccurrences:
            if(__checkLine(line, author)):
                return True
    return False


def __createAuthorDict(authorList):
    # Creates a dictionary for the possible authors in the article. 
    author_dict = {}
    for author in authorList:
        if(author.find(' ') > 0):
            if author in author_dict.keys():
                author_dict[author] += 1
            else:
                author_dict[author] = 1
    return author_dict


def compileAuthors(url):
    # Gathers and Refines the author search
    # Get the raw html of the url
    rawText = getStories.createRawText(url)
    # Create the NER tagged list of potential author names
    tags = getStories.createTags(rawText)
    # Refine the tagged list to get full names
    authorList = getStories.createPossibleAuthor(tags)
    # Create a dictionary of those author names
    authorDict = __createAuthorDict(authorList)
    # Open the url with Beautiful Soup
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    # Restrict and score the author list
    refinedList = __restrictAuthors(soup, authorDict)
    # Return the author name with the max score
    return max(refinedList, key=refinedList.get)

def __restrictAuthors(inputSoup, author_dict):
    # Restricts the author list and score the remaining authors based on occurences, location, and the byline
    newAuthorList = {}
    location = 0
    title = str(inputSoup.find('h1'))
    byline = __getByline(inputSoup)
    authorOccurrences = __searchAuthor(inputSoup)
    # Create a refined list of author names. Score based on location and occurences
    for author in author_dict:
        # Ensure the author's name is not in the title
        if(title.find(author) == -1):
            newAuthorList[author] = 30 - location - 2 * author_dict[author]
        location += 1
    # Loop through the refined list. Add a substantial score if the author's name is near 'author' or in a byline
    for element in newAuthorList:
        if (newAuthorList[element] > 15):
            if(__findAuthor(inputSoup, element, byline, authorOccurrences)):
                newAuthorList[element] += 30
                break
    return newAuthorList

def storyList(author):
    # Calling the getStories to get the Aylien API Response
    result = getStories.getStories(author)
    return result
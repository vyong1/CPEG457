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


def buildCardWithLink(title, text, link_url, link_text):
    outerWrapper = HtmlElement(
        tag='div', 
        attrs={'class' : '"card margin10"'}
    )
    cardBody = HtmlElement(
        tag='div',
        attrs={'class' : 'card-body'}
    )
    cardTitle = HtmlElement(
        tag='h5',
        content= title,
        attrs={'class' : 'card-subtitle mb-2 text-muted'}
    )
    cardText = HtmlElement(
        tag='p',
        content= text,
        attrs={'class' : 'card-text'}
    )
    cardLink = HtmlElement(
        tag='a',
        content= link_text,
        attrs={'href' : link_url, 'class' : 'card-link'}
    )

    cardBody.addContent(cardTitle)
    cardBody.addContent(cardText)
    cardBody.addContent(cardLink)
    outerWrapper.addContent(cardBody)
    return str(outerWrapper)

def buildCard(title, text):
    outerWrapper = HtmlElement(
        tag='div', 
        attrs={'class' : '"card margin10"'}
    )
    cardBody = HtmlElement(
        tag='div',
        attrs={'class' : 'card-body'}
    )
    cardTitle = HtmlElement(
        tag='h5',
        content= title,
        attrs={'class' : 'card-subtitle mb-2 text-muted'}
    )
    cardText = HtmlElement(
        tag='p',
        content= text,
        attrs={'class' : 'card-text'}
    )

    cardBody.addContent(cardTitle)
    cardBody.addContent(cardText)
    outerWrapper.addContent(cardBody)
    return str(outerWrapper)

def buildWikipediaCard(authorName):
    request = WikipediaAPI.queryLatest(authorName)
    pageID = WikipediaAPI.getPageID(request)
    
    if (not WikipediaAPI.pageExists(pageID)):
        return '' # Page doesn't exist

    pageURL = WikipediaAPI.getURLFromPageID(pageID)
    wikiArticleHtml = urllib.request.urlopen(pageURL)
    articleSoup = BeautifulSoup(wikiArticleHtml, 'html.parser')
    introParagraph = str(
        HtmlElement(
        tag='p',
        content= 'Fetched from Wikipedia.org',
    )) + str(articleSoup.find('p'))
    return buildCardWithLink(authorName, introParagraph, pageURL, "Link to Wikipedia Article")
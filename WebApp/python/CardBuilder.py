# python lib imports
import urllib
import os
import json
# local imports
from HtmlElement import HtmlElement
from WikipediaAPI import *
from PipeFile import *
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
        html = '' # Page doesn't exist
    else:
        hasPulitz = "Yes"
        if(WikipediaAPI.hasPulitzer(str(request.json())) is False):
            hasPulitz = "No"

        pageURL = WikipediaAPI.getURLFromPageID(pageID)
        wikiArticleHtml = urllib.request.urlopen(pageURL)
        articleSoup = BeautifulSoup(wikiArticleHtml, 'html.parser')
        introParagraph = str(
            HtmlElement(
            tag='p',
            content= 'Fetched from Wikipedia.org',
        )) + str(articleSoup.find('p'))
        html = buildCardWithLink(authorName, introParagraph, pageURL, "Link to Wikipedia Article")
        html += CardBuilder.buildCard('Pulitzer Prize?', hasPulitz)
    return html

def buildArticleCards(resp):
    if(len(resp.stories) == 0):
        print("No articles found")
        return buildCard(
            title=":(",
            text="Sorry, we couldn't find any articles by this author"
        )
    else:
        html = ""
        for story in resp.stories:
            body = str(story.body)
            if len(body) < 500:
                body = body[0:len(body)]
            else:
                body = body[0:500]
            body += "..."
            # Replace non-html characters
            body = body.replace("'", "&#39;")
            body = body.replace("’", "&#39;")
            body = body.replace("'", "&#39;")
            body = body.replace("—", "-")

            # Add the domain's logo
            # <img src="url">
            logoURL = str(story.source.logo_url)
            if not (logoURL == "None"):
                imgTag = '<div><img src="' + logoURL + '"></div>'
                body = imgTag + body

            html += buildCardWithLink(
                title=str(story.title),
                text=body,
                link_url=str(story.links.permalink),
                link_text="Read More"
            )
            
        return html
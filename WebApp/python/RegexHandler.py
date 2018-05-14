# python lib imports
import urllib
import os
from subprocess import call
# local imports
import HtmlElement
import getStories
import NameStats
import test
from PipeFile import *
# beatiful soup import
from bs4 import BeautifulSoup

def __buildRegExp(authorDict):
    regExp = ''
    for author, value in authorDict.items():
        regExp += '(' + author + ")|"
    regExp = regExp[0:len(regExp) - 1] # Cut off last '|'
    return regExp


def getAuthorMatches(authorDict, rawHtmlText):
    # read content from pipe to store in buffer
    oldContent = PipeFile.read()
    # Build expression
    regExp = __buildRegExp(authorDict)
    # Pass to pipe2
    PipeFile2.write(regExp)
    # Pass rawtext to pipe
    PipeFile.write(rawHtmlText)
    # execute php
    call(["php", "regexEx.php"])
    # get matches from pipe
    matches = PipeFile.read()
    # rewrite pipe's old content
    PipeFile.write(oldContent)
    # return matches
    return matches

url = "https://www.cnn.com/2018/05/12/politics/us-embassy-mideast-tensions-policy-changes/index.html"
authorDict = {'Chris Cillizza': 1, 'Fareed Zakaria': 1, 'Hunter Schwarz': 1, 'Kate Bennett': 1, 'Dylan Byers': 1, 'Nicole Gaouette': 2, 'Ben Wedeman': 10, 'Benjamin Netanyahu': 6, 'Nikki Haley': 8, 'Donald Trump': 15, 'Oren Liebermann': 4, 'Ian Lee': 4, 'Thomas Friedman': 4, 'Rex Tillerson': 4, 'Nir Barkat': 4, 'Donald TrumpConfusion': 1, 'Bruce Riedel': 1, 'Dennis Ross': 1, 'David Friedman': 1, 'Victoria Coates': 1, 'Javad Zarif': 1, 'Vladimir Putin': 1, 'Antonio Guterres': 1, 'Emmanuel Macron': 1, 'Jamie Crawford': 1, 'Hamdi Alkhshali': 1, 'Mike Schwartz': 1, 'Elise Labott': 1, 'Nadine Schmidt': 1, 'Nada Bashir': 1, 'Mary Ilyushina': 1, 'Kristina Sgueglia': 1, 'Richard Roth': 1}
print(__buildRegExp(authorDict))
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

getAuthorMatches(authorDict, str(soup))
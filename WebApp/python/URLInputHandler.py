from PipeFile import PipeFile
import POSTParser
from Wikipedia_api.WikipediaAPI import *
import CardBuilder
import sys
import test

# Parse the POST and extract the URL
POST = POSTParser.parse()
url = POST['url_input']

# TODO Extract the name of the author
# Assume the name is 'John Archibald' for now
authorName = test.compileAuthors(url)

# TODO Enter the author's name into the Aylien-Api


# TODO Fetch a bunch of relevant articles and put them into cards

# Check for pulitzer
r = WikipediaAPI.queryLatest(authorName)
hasPulitz = "Yes"
if(WikipediaAPI.hasPulitzer(str(r.json())) is False):
    hasPulitz = "No"

# Output some helpful html
PipeFile.clear()
PipeFile.append("<h1 class='margin10'>Here's What We Found:</h1>")
PipeFile.append(CardBuilder.buildCard('Article URL', url))
PipeFile.append(CardBuilder.buildCard('Author', authorName))
PipeFile.append(CardBuilder.buildCard('Does the Author have a Pulitzer?', hasPulitz))
PipeFile.append(CardBuilder.buildCardWithLink('Article', 'Some Article Text Some Article Text Some Article Text Some Article Text ', 'haha', 'This a Link'))
PipeFile.append(CardBuilder.buildWikipediaCard(authorName))
PipeFile.append(CardBuilder.buildArticleCards(test.storyList(authorName)))

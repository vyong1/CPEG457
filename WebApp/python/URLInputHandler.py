from PipeFile import PipeFile
import POSTParser
from Wikipedia_api.WikipediaAPI import *
import CardBuilder
import sys

# Parse the POST and extract the URL
POST = POSTParser.parse()
url = POST['url_input']

# TODO Extract the name of the author
# Assume the name is 'John Archibald' for now
name = 'John Archibald'

# TODO Enter the author's name into the Aylien-Api


# TODO Fetch a bunch of relevant articles and put them into cards

# Check for pulitzer
r = WikipediaAPI.queryLatest(name)
hasPulitz = "Yes"
if(hasPulitzer(str(r.json())) is False):
    hasPulitz = "No"


# Output some helpful html
PipeFile.clear()
PipeFile.append(CardBuilder.buildCard('Article URL', url))
PipeFile.append(CardBuilder.buildCard('Author', name))
PipeFile.append(CardBuilder.buildCard('Does the Author have a Pulitzer?', hasPulitz))
PipeFile.append(CardBuilder.buildCardWithLink('Article', 'Some Article Text Some Article Text Some Article Text Some Article Text ', 'haha', 'This a Link'))
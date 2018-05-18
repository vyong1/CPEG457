from PipeFile import PipeFile
import POSTParser
from Wikipedia_api.WikipediaAPI import *
import CardBuilder
import sys
import AuthorID

# Parse the POST and extract the URL
POST = POSTParser.parse()
url = POST['url_input']

# Extract the name of the author
authorName = AuthorID.compileAuthors(url)
print(authorName)

# Output some helpful html
PipeFile.clear()
PipeFile.append("<h1 class='margin10'>Here's What We Found:</h1>")
PipeFile.append(CardBuilder.buildCard('Article URL', url))
PipeFile.append(CardBuilder.buildCard('Author', authorName))
# Make card for wikipedia
PipeFile.append(CardBuilder.buildWikipediaCard(authorName))
# Make cards for articles
PipeFile.append(CardBuilder.buildArticleCards(AuthorID.storyList(authorName)))

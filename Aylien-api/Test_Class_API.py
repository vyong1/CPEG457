
from API import NewsAPI

api = NewsAPI()

author = "Kif Leswing"
response = api.getStories(author)

for article in response:
    print("Source.domain: ", article.source.domain)
    print("Source.locations: ", article.source.locations)
    print("Published: ", article.source.name)
    print("Title: ", article.title,"\n")

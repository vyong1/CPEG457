import aylien_news_api
from aylien_news_api.rest import ApiException

# Configure API key authorization: app_id
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = '59793aeb'
# Configure API key authorization: app_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = '6557890cdc6ffabe3203700616bcb1fb'

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()

category = "Politics"

code = {"Politics": 'IAB11',
        "Business":'IAB3',
        "Entertainment":'IAB1',
        "Sports":'IAB17',
        "Science":'IAB15',
        "Technology":'IAB19',
        }


opts = {
  'categories_taxonomy': 'iab-qag',
  'categories_id': [code[category]],
  'categories_confident' : True,
  'language': ['en'],
  'source_locations_country': ['US'],
  'published_at_start': 'NOW-1YEAR',
  'published_at_end': 'NOW'
}

categoryTitle = category + "Titles2.txt"
categoryCollection = category + "Collection2.txt"


collectionFile = open(categoryCollection,"a", encoding='utf-8')


titles = {}
titleFile = open(categoryTitle,"r")
for line in titleFile:
    titles[line] = 0

titleFile.close()
#print(titles)
titleFile = open(categoryTitle,"a", encoding='utf-8')



try:
    # List stories
    api_response = api_instance.list_stories(**opts)
    for story in api_response.stories:
        title = story.title
        #print("category id: ", story.categories[0].id)
        print(title)
        found = (title + "\n") in titles
        if not((title + "\n") in titles):
            print("***",title)
            titles[title] = 0
            #p = input("Do you want o add article to collection Y for yes: ")
            #print(p)
            #if(p == 'y'):
            titleFile.write(title + "\n")
            body = story.body
            article = title + "\n" + body + "\n"
            collectionFile.write(article)
        print("ArticleTitle found: ", found)
    collectionFile.close()
    titleFile.close()
except ApiException as e:
    print("Exception when calling DefaultApi->list_stories: %sn" % e)

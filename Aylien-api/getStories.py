import aylien_news_api
import urllib
from aylien_news_api.rest import ApiException
from bs4 import BeautifulSoup

# Configure API key authorization: app_id
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'c45042a9'
# Configure API key authorization: app_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = 'a9270fe1446fc3fb7c8e8196ed52e626'

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()

url = "https://www.cnn.com/2018/04/24/politics/melania-trump-white-house/index.html"
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
raw_text = soup.get_text()

def getStories(author_name):
    # Takes in authors name, sets it as an option for the api
    opts = {
      'author_name': author_name
    }

    try:
        # Creates an associative array of the stories
        api_response = api_instance.list_stories(**opts)
        return api_response
    except ApiException as e:
        print("Exception when calling DefaultApi->list_stories: %sn" % e)
        
        
author = "Kevin Liptak"
api_response = getStories(author)
for element in api_response.stories:
        print(element.title)
        print(element.links.permalink)
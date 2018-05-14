import aylien_news_api
from aylien_news_api.rest import ApiException

class NewsAPI:
    #attributes that all NewsAPI instance will share
    def __init__(self):
        self.aylien_news_api = aylien_news_api
        self.ApiException = ApiException
        self.aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = '43157cd86a0c9ef77da72df2450d5da0'
        self.aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'f780bd2f'
        self.api_instance = aylien_news_api.DefaultApi()

    def getStories(self, author_name):
        opts = {
          'author_name': author_name
        }

        try:
            # get a response
            api_response = self.api_instance.list_stories(**opts)
            #return the list of stories
            return api_response.stories
        except ApiException as e:
            print("Exception when calling DefaultApi->list_stories: %sn" % e)

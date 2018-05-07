# Documentation https://www.mediawiki.org/wiki/API:Main_page
import requests
import re

class WikipediaAPI:
    '''
    Wrapper for the Wikipedia API
    '''
    Endpoint = 'https://en.wikipedia.org/w/api.php?'

    def get(params):
        return requests.get(WikipediaAPI.Endpoint, params)

    def queryLatest(query):
        # Queries API For the latest revision in JSON format
        params = {
            # Submit a json query
            'action' : 'query',
            'titles' : query,
            'format' : 'json',

            # Get the contents of the latest revision
            'prop' : 'revisions',
            'rvprop' : 'content'
        }
        return WikipediaAPI.get(params)

def hasPulitzer(stringData):
    return (str.find(stringData, 'Pulitzer') >= 0)


r = WikipediaAPI.queryLatest('John Archibald')
print(hasPulitzer(str(r.json()))) 

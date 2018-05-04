# Code from https://newsapi.org/docs/get-started

import requests
url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=1473d5d8b9b54099940acc059d5cb4be')
response = requests.get(url)
print(response.json())
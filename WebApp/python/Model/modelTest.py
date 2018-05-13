from bs4 import BeautifulSoup
import urllib.request
import requests
from Classification_Model import PoliticsModel
from Classification_Model import BusinessModel
from Classification_Model import EntertainmentModel
from Classification_Model import SportsModel
from Classification_Model import ScienceModel
from Classification_Model import TechnologyModel

#from EntertainmentModel import EntertainmentModel
#from ScienceModel import ScienceModel

#url = "https://www.cnn.com/2018/05/12/politics/trump-jerusalem-embassy-cost/index.html"
url = "http://www.businessinsider.com/apple-ceo-tim-cook-commencement-speech-duke-university-2018-5"
#headers = {'User-Agent':'Mozilla/5.0'}

#html = requests.get(url)
#soup = BeautifulSoup(html.text,'html.parser')
#soup.a.extract()
#soup.img.extract()
#body = soup.body.extract()


html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
p_tags = soup.find_all("p")
text = soup.find("body").get_text()
# for tag in p_tags:
#     print(tag)
#     text += tag.get_text() + " "

string = text.strip(".")
arrayText = string.split()
words = []
for word in arrayText:
    if(word.isalnum()):
        words.append(word)
string = ""
for word in words:
    string += word + " "

#print(string)

PoliticsModel = PoliticsModel()
print("Politics Score: ", PoliticsModel.getProbability(words))

BusinessModel = BusinessModel()
print("Business Score: ", BusinessModel.getProbability(words))

EntertainmentModel = EntertainmentModel()
print("Entertainment Score: ", EntertainmentModel.getProbability(words))

SportsModel = SportsModel()
print("Sports Score: ", SportsModel.getProbability(words))

ScienceModel = ScienceModel()
print("Science Score: ", ScienceModel.getProbability(words))

TechnologyModel = TechnologyModel()
print("Technology Score: ", TechnologyModel.getProbability(words))

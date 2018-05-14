from bs4 import BeautifulSoup
import urllib.request
import requests
from Classification_Model import PoliticsModel
from Classification_Model import BusinessModel
from Classification_Model import EntertainmentModel
from Classification_Model import SportsModel
from Classification_Model import ScienceModel
from Classification_Model import TechnologyModel


global PoliticsModel
global BusinessModel
global EntertainmentModel
global SportsModel
global ScienceModel
global TechnologyModel

def __getTextArray(url):

    print(url)
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.find("body").get_text()
    #text = ""
    # p_tags = soup.find_all("p")
    # for tag in p_tags:
    #      #print(tag)
    #      text += tag.get_text() + " "

    # string1 = text.lower()
    # string2 = string1.replace(".","")
    # string3 = string2.replace(",","")
    # string4 = string3.replace('"',"")
    # string5 = string4.replace("?","")
    # string6 = string5.replace("!","")
    # string7 = string6.replace(":","")
    # string8 = string7.replace(";","")
    # string9 = string8.replace("(","")
    # string10 = string9.replace(")","")
    # string11 = string10.replace("@","")
    # string12 = string11.replace("#","")
    # string13 = string12.replace("$","")
    # string14 = string13.replace("%","")
    # string15 = string14.replace("^","")
    # string16 = string15.replace("&","")
    # string17 = string16.replace("*","")
    # string18 = string17.replace("+","")
    # string19 = string18.replace("{","")
    # string20 = string19.replace("}","")
    # string21 = string20.replace("[","")
    # string22 = string21.replace("]","")
    # string23 = string22.replace("|","")
    # string24 = string23.replace("/","")
    # string25 = string24.replace(">","")
    # string26 = string25.replace("<","")

    #text2 = text.lower()
    text3 = text.strip(".")
    arrayText = text3.split()
    words = []
    for word in arrayText:
        if(word.isalnum()):
            words.append(word)
    return words


def getLabel(url):
    labels = {}
    words = __getTextArray(url)

    Politics = PoliticsModel()
    labels["Politics"] = Politics.getProbability(words)
    print("Politics Score: ", labels["Politics"])

    Business = BusinessModel()
    labels["Business"] = Business.getProbability(words)
    print("Business Score: ", labels["Business"])

    Entertainment = EntertainmentModel()
    labels["Entertainment"] = Entertainment.getProbability(words)
    print("Entertainment Score: ", labels["Entertainment"])

    Sports = SportsModel()
    labels["Sports"] = Sports.getProbability(words)
    print("Sports Score: ", labels["Sports"])

    Science = ScienceModel()
    labels["Science"] = Science.getProbability(words)
    print("Science Score: ", labels["Science"])

    Technology = TechnologyModel()
    labels["Technology"] = Technology.getProbability(words)
    print("Technology Score: ", labels["Technology"])

    return max(labels, key=labels.get)

url = "https://www.washingtonpost.com/"
#url = "https://www.washingtonpost.com/national/after-his-family-died-he-threatened-to-kill-himself-so-the-police-took-his-guns/2018/03/17/38e3138e-26e6-11e8-874b-d517e912f125_story.html?utm_term=.ba3dd93bd906"#science
#url = "http://money.cnn.com/2018/03/30/technology/google-clips-photography/index.html"#technology
#url = "http://money.cnn.com/2018/05/11/technology/amazon-echo-dot-kids-lawmaker-concerns/index.html"#business
#url = "http://money.cnn.com/2018/05/11/technology/elon-musk-boring-company-tunnel/index.html" #business
#url = "https://www.buzzfeed.com/susancheng/carla-hool-coco-narcos-casting-director-latino-actors?utm_term=.cop1Ke38v#.wcjdzk0py"#entertainment
#url = "https://www.buzzfeed.com/nicolenguyen/amazon-fake-review-problem?utm_term=.shRO4Wk2Q#.vrJE0AB4m"#business
#url = "https://www.buzzfeed.com/ingaspringe/a-former-aide-to-two-of-the-senates-biggest-russia-hawks-is?utm_term=.qcLkB7RWX#.ukxgXmrp7"#business
#url = "https://www.buzzfeed.com/tylerkingkade/privacy-laws-students-sexual-assault-harassment-ferpa?utm_term=.abPOgdGXk#.lr2be9jnB"#business
#url = "https://www.buzzfeed.com/darrensands/stacey-abrams-kamala-harris-black-women-democrats?utm_term=.bqaxM4NAX#.usA6R9Z8Q"#business
#url = "https://www.buzzfeed.com/nidhiprakash/at-least-13-people-dead-in-indonesia-church-bombings?utm_term=.vyOKwgZEV#.ekAB0yGQX"#business
#url = "https://www.buzzfeed.com/pdominguez/christina-aguilera-comeback-accelerate-liberation?bfsplash&utm_term=.kqxrYAKvm#.atyZqaNe8"#entertainment
#url = "https://www.washingtonpost.com/news/the-switch/wp/2018/05/11/i-was-team-deleteuber-can-ubers-new-boss-change-my-mind/?utm_term=.e63d011c91fc"#business
#url = "https://www.nytimes.com/2018/05/13/sports/baseball/yankees-giancarlo-stanton.html?rref=collection%2Fsectioncollection%2Fsports&action=click&contentCollection=sports&region=rank&module=package&version=highlights&contentPlacement=1&pgtype=sectionfront"#sports
#url = "http://www.foxnews.com/tech/2018/04/07/speed-up-internet-find-forgotten-passwords-convert-vhs-tapes-and-more.html"#technology
#url = "http://www.foxnews.com/politics/2018/05/13/bizarre-anti-trump-mothers-day-ad-launched-by-liberal-activist-tom-steyer.html"#business
#url = "http://www.foxnews.com/entertainment/2018/05/11/big-bang-star-mayim-bialik-says-didnt-feel-beautiful-during-season-finale-wedding-episode.html"#entertainment
#url = "https://www.foxbusiness.com/politics/trump-on-china-trade-be-cool-it-will-all-work-out"#business
#url = "http://money.cnn.com/2018/05/11/technology/google-lookout-app/index.html"#business
#url = "http://money.cnn.com/2018/05/10/technology/spacex-falcon-9-block-5-launch/index.html"#business
#url = "http://money.cnn.com/2018/05/04/technology/deliveroo-growth/index.html"#business
#url = "https://www.msn.com/en-us/sports/nba/celtics-ambush-cavs-early-on-way-to-game-1-rout/ar-AAxdcTh"#sports
#url = "https://www.cnn.com/2018/05/12/politics/trump-jerusalem-embassy-cost/index.html"#business
#url = "http://www.businessinsider.com/apple-ceo-tim-cook-commencement-speech-duke-university-2018-5"#technology
#url = "http://www.businessinsider.com/netflix-and-others-warn-about-the-end-of-the-net-neutrality-rules-2018-5"#business
#headers = {'User-Agent':'Mozilla/5.0'}

print(getLabel(url))

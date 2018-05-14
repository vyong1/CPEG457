import math

class PoliticsModel:
    #attributes that all NewsAPI instance will share
    def __init__(self):
        self.name = "Politics"
        self.wordStats = {}
        file = open( "python/Model/" + self.name+ "Model.txt","r")
        self.readFirstLine = False
        for line in file:
            if(not self.readFirstLine):
                self.collectionProbability = float(line)
                self.readFirstLine = True
            else:
                statistics = line.split()
                self.wordStats[statistics[0]] = float(statistics[1])
        file.close()
    #takes in an array of strings (words) and return the probability
    def getProbability(self, words):
        probability = 0
        for word in words:
            if (word in self.wordStats):
                probability += math.log(self.wordStats[word])
            else:
                probability += math.log(1/100000000)
        # return probability * self.collectionProbability
        return probability + math.log(self.collectionProbability)


class BusinessModel:
    #attributes that all NewsAPI instance will share
    def __init__(self):
        self.name = "Business"
        self.wordStats = {}
        file = open("python/Model/" + self.name+ "Model.txt","r", encoding = "ISO-8859-1")
        self.readFirstLine = False
        for line in file:
            if(not self.readFirstLine):
                self.collectionProbability = float(line)
                self.readFirstLine = True
            else:
                statistics = line.split()
                self.wordStats[statistics[0]] = float(statistics[1])
        file.close()
    #takes in an array of strings (words) and return the probability
    def getProbability(self, words):
        probability = 0
        for word in words:
            if (word in self.wordStats):
                probability += math.log(self.wordStats[word])
            else:
                probability += math.log(1/100000000)
        # return probability * self.collectionProbability
        return probability + math.log(self.collectionProbability)

class EntertainmentModel:
    #attributes that all NewsAPI instance will share
    def __init__(self):
        self.name = "Entertainment"
        self.wordStats = {}
        file = open("python/Model/" + self.name+ "Model.txt","r", encoding = "ISO-8859-1")
        self.readFirstLine = False
        for line in file:
            if(not self.readFirstLine):
                self.collectionProbability = float(line)
                self.readFirstLine = True
            else:
                statistics = line.split()
                self.wordStats[statistics[0]] = float(statistics[1])
        file.close()
    #takes in an array of strings (words) and return the probability
    def getProbability(self, words):
        probability = 0
        for word in words:
            if (word in self.wordStats):
                probability += math.log(self.wordStats[word])
            else:
                probability += math.log(1/100000000)
        # return probability * self.collectionProbability
        return probability + math.log(self.collectionProbability)


class SportsModel:
    #attributes that all NewsAPI instance will share
    def __init__(self):
        self.name = "Sports"
        self.wordStats = {}
        file = open("python/Model/" + self.name+ "Model.txt","r", encoding = "ISO-8859-1")
        self.readFirstLine = False
        for line in file:
            if(not self.readFirstLine):
                self.collectionProbability = float(line)
                self.readFirstLine = True
            else:
                statistics = line.split()
                self.wordStats[statistics[0]] = float(statistics[1])
        file.close()
    #takes in an array of strings (words) and return the probability
    def getProbability(self, words):
        probability = 0
        for word in words:
            if (word in self.wordStats):
                probability += math.log(self.wordStats[word])
            else:
                probability += math.log(1/100000000)
        # return probability * self.collectionProbability
        return probability + math.log(self.collectionProbability)


class ScienceModel:
    #attributes that all NewsAPI instance will share
    def __init__(self):
        self.name = "Science"
        self.wordStats = {}
        file = open("python/Model/" + self.name+ "Model.txt","r", encoding = "ISO-8859-1")
        self.readFirstLine = False
        for line in file:
            if(not self.readFirstLine):
                self.collectionProbability = float(line)
                self.readFirstLine = True
            else:
                statistics = line.split()
                self.wordStats[statistics[0]] = float(statistics[1])
        file.close()
    #takes in an array of strings (words) and return the probability
    def getProbability(self, words):
        probability = 0
        for word in words:
            if (word in self.wordStats):
                probability += math.log(self.wordStats[word])
            else:
                probability += math.log(1/100000000)
        # return probability * self.collectionProbability
        return probability + math.log(self.collectionProbability)


class TechnologyModel:
    #attributes that all NewsAPI instance will share
    def __init__(self):
        self.name = "Technology"
        self.wordStats = {}
        file = open("python/Model/" + self.name+ "Model.txt","r", encoding = "ISO-8859-1")
        self.readFirstLine = False
        for line in file:
            if(not self.readFirstLine):
                self.collectionProbability = float(line)
                self.readFirstLine = True
            else:
                statistics = line.split()
                self.wordStats[statistics[0]] = float(statistics[1])
        file.close()
    #takes in an array of strings (words) and return the probability
    def getProbability(self, words):
        probability = 0
        for word in words:
            if (word in self.wordStats):
                probability += math.log(self.wordStats[word])
            else:
                probability += math.log(1/100000000)
        # return probability * self.collectionProbability
        return probability + math.log(self.collectionProbability)

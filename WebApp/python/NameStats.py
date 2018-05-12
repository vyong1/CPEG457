class NameStats():
    def __init__(self, TF, nameIsInTitle, nameIsInLink, preceededByKeyWord, firstOccurence):
        self.TF = TF
        self.nameIsInTitle = nameIsInTitle
        self.nameIsInLink = nameIsInLink
        self.preceededByKeyWord = preceededByKeyWord
        self.firstOccurence = firstOccurence

    def calculateProbability(self):
        raise Exception("Not Implemented Exception")
    


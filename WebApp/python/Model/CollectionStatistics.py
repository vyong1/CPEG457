categories = ["Politics", "Business", "Entertainment", "Science", "Sports", "Technology"]
categoryTitleFiles = {}
categoryCollectionFiles = {}
numberOfDoc = {}
total_number_documents = 0

#dictionary for the files
for category in categories:
    categoryTitle = category + "Titles.txt"
    categoryTitleFiles[category] = categoryTitle
    categoryCollection = category + "Collection.txt"
    categoryCollectionFiles[category] = categoryCollection

#count the number of documents in each collection
for category in categoryTitleFiles:
    try:
        file = open(categoryTitleFiles[category],"r",encoding='utf-8')
        linesInFile = 0
        for line in file:
            total_number_documents += 1
            linesInFile += 1
        print(category, "Title lines: ", linesInFile)
        numberOfDoc[category] = linesInFile
        file.close()
    except:
        file = open(categoryTitleFiles[category],"r")
        linesInFile = 0
        for line in file:
            total_number_documents += 1
            linesInFile += 1
        print(category, "Title lines: ", linesInFile)
        numberOfDoc[category] = linesInFile
        file.close()
print(total_number_documents)

def punct_remove(input_string):
  string = input_string
  string = string.lower()
  string = string.replace(".","")
  string = string.replace(",","")
  string = string.replace('"',"")
  string = string.replace("?","")
  string = string.replace("!","")
  string = string.replace(":","")
  string = string.replace(";","")
  string = string.replace("(","")
  string = string.replace(")","")
  string = string.replace("@","")
  string = string.replace("#","")
  string = string.replace("$","")
  string = string.replace("%","")
  string = string.replace("^","")
  string = string.replace("&","")
  string = string.replace("*","")
  string = string.replace("+","")
  string = string.replace("{","")
  string = string.replace("}","")
  string = string.replace("[","")
  string = string.replace("]","")
  string = string.replace("|","")
  string = string.replace("/","")
  string = string.replace(">","")
  string = string.replace("<","")
  return string


for category in categories:
    try:
        file = open(categoryCollectionFiles[category],"r")
        text = file.read()
        #print(text)
        text2 = punct_remove(text)
        textArray = text2.split()
        #print(textArray)
        total_words_collection = len(textArray)
        #print(total_words_collection)
        words = set(textArray)
        #print(words)
        wordStats = {}
        for word in words:
            TF = textArray.count(word)
            wordStats[word] = TF/total_words_collection

        wFile = open(category+"Model.txt","w")
        wFile.write(str(numberOfDoc[category]/total_number_documents) + "\n") # calculate the P(C)
        for word in wordStats:
            wFile.write(word + " " + str(wordStats[word]) + "\n")
    except:
        file = open(categoryCollectionFiles[category],"r", encoding = "ISO-8859-1")
        text = file.read()
        #print(text)
        text2 = punct_remove(text)
        textArray = text2.split()
        #print(textArray)
        total_words_collection = len(textArray)
        #print(total_words_collection)
        words = set(textArray)
        #print(words)
        wordStats = {}
        for word in words:
            TF = textArray.count(word)
            wordStats[word] = TF/total_words_collection

        wFile = open(category+"Model.txt","w", encoding = "ISO-8859-1")
        wFile.write(str(numberOfDoc[category]/total_number_documents) + "\n") # calculate the P(C)
        for word in wordStats:
            wFile.write(word + " " + str(wordStats[word]) + "\n")

# category = "Sports"
# file = open(categoryCollectionFiles[category],"r", encoding = "ISO-8859-1")
# text = file.read()
# #print(text)
# text2 = punct_remove(text)
# textArray = text2.split()
# #print(textArray)
# total_words_collection = len(textArray)
# #print(total_words_collection)
# words = set(textArray)
# #print(words)
# wordStats = {}
# for word in words:
#     TF = textArray.count(word)
#     wordStats[word] = TF/total_words_collection
#
# wFile = open(category + "Model.txt","w",encoding = "ISO-8859-1")
# wFile.write(str(numberOfDoc[category] /total_number_documents) + "\n")
# for word in wordStats:
#     wFile.write(word + " " + str(wordStats[word]) + "\n")

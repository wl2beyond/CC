import os
import re

def word(inputFile):   # word: clean the text and store every word into a list
    paper=inputFile.read()
    paper=paper_clean(paper)
    lists = paper.split()
    return lists

def wordCount(wordList): # wordCount: for word in wordList, count how many times it appears and set it into the dictionary
    dic = {}
    for key in wordList:
        if key in dic:
            dic[key] +=1
        else:
            dic[key] = 1
    return dic

def paper_clean(paper): #paper_clean: clean all the special characters and make all letters into lower case
    paper = paper.lower()
    paper = re.sub('[^a-zA-Z0-9]', ' ', paper)
    return paper

path = "./wc_input"  #filepath of input files
dirs = os.listdir(path)
wordList = [] #make a list for all the words

for fl in dirs:
    inputFile = open("./wc_input/"+fl,"r")
    lists = word(inputFile)
    wordList = wordList + lists
    inputFile.close()

outputFile=open("./wc_output/wc_result.txt","w")

dic = wordCount(wordList)

sortedKey = sorted(dic, key=dic.get)
sortedKey.sort()

for key in sortedKey:
    print "%s\t%d\n"%(key,dic[key])
    outputFile.write("%s\t%d\n"%(key, dic[key]))
    

outputFile.close()

import os
def word(fileRead):
    paper=fileRead.read()
    paper=paper_clean(paper)
    lists = paper.split()
    return lists

def wordCount(wordList):
    dic = {}
    for key in wordList:
        if key in dic:
            dic[key] +=1
        else:
            dic[key] = 1
    return dic

def paper_clean(paper):
    paper = paper.lower()
    paper = paper.replace(',',' ')
    paper = paper.replace('.',' ')
    paper = paper.replace('_',' ')
    paper = paper.replace('!',' ')
    paper = paper.replace('?',' ')
    paper = paper.replace('~',' ')
    paper = paper.replace('@',' ')
    paper = paper.replace('#',' ')
    paper = paper.replace('%',' ')
    paper = paper.replace('^',' ')
    paper = paper.replace('&',' ')
    paper = paper.replace('*',' ')
    paper = paper.replace('{',' ')
    paper = paper.replace('}',' ')
    paper = paper.replace('[',' ')
    paper = paper.replace(']',' ')
    paper = paper.replace(':',' ')
    paper = paper.replace(';',' ')
    paper = paper.replace('(','')
    paper = paper.replace(')','')
    paper = paper.replace('"','')
    paper = paper.replace('\'','')
    paper = paper.replace('$','')
    print paper
    return paper


path = "./wc_input"
dirs = os.listdir( path )
wordList = []
for fl in dirs:
    print fl
    fileRead = open("./wc_input/"+fl,"r")
    lists = word(fileRead)
    wordList = wordList + lists
    fileRead.close()
    print wordList

w=open("./wc_output/wc_result.txt","w")

dic = wordCount(wordList)

sortedKey = sorted(dic, key=dic.get)
sortedKey.sort()

for key in sortedKey:
    print "%s\t%d\n"%(key,dic[key])
    w.write("%s\t%d\n"%(key, dic[key]))
    

w.close()

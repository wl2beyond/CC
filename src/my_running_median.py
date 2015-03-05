import os
import re

def main():
    path = "./wc_input"  #filepath of input files
    dirs = os.listdir(path)
    totalNum = []      #make a list for all the numbers of words in every line of all file
    for fl in dirs:
        inputFile=open("./wc_input/"+fl,"r")
        num = wordsinLine(inputFile)
        totalNum =totalNum + num
        inputFile.close()

    median = medList(totalNum)    
    outputFile=open("./wc_output/med_result.txt","w") #create a output file and write result into it
    for i in median:
        print i
        outputFile.write(str(i)+'\n')
    outputFile.close()
    
def med(num):  #med: find the median of a list of numbers
    num.sort()
    if len(num)%2 == 0:
        return float((num[int(len(num) / 2.0)] + num[int(len(num)/2.0 - 1)]) / 2.0)
    else:
        return float(num[int((len(num)-1)/2.0)])
    
def wordsinLine(fl): #WordsinLine: find number of words per line in a file
    num=[]
    for line in fl.readlines():
        line=paper_clean(line)
        num.append(len(line.split()))       
    return num

def medList(num):  #medList: find each meadian number line by line
    median = []
    for i in range(len(num)):
        median.append(med(num[:(i+1)]))
    return median

def paper_clean(paper): #paper_clean: clean all the special characters and make all letters into lower case
    paper = paper.lower()
    paper = re.sub('[^a-zA-Z0-9]', ' ', paper)
    return paper
    
if __name__ == '__main__':
    main()
    

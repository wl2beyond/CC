import os
def med(num):
    num.sort()
    if len(num)%2 == 0:
        return float((num[int(len(num) / 2.0)] + num[int(len(num)/2.0 - 1)]) / 2.0)
    else:
        return float(num[int((len(num)-1)/2.0)])
    
def WordsinLine(fl):
    num=[]
    for line in fl.readlines():
        print line
        line=paper_clean(line)
        num.append(len(line.split()))       
    print num
    return num

def medList(num):
    median = []
    for i in range(len(num)):
        median.append(med(num[:(i+1)]))
    return median

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
totalNum = []
print totalNum
for fl in dirs:
    print fl
    m=open("./wc_input/"+fl,"r")
    num = WordsinLine(m)
    totalNum =totalNum + num
    print totalNum
    m.close()

median = medList(totalNum)
print median
    
w=open("./wc_output/med_result.txt","w")
for i in median:
    print i
    w.write(str(i)+'\n')
    

w.close()

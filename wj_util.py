import re

def getTagsFromEntry(string):
    tags = string.replace(' ','').lstrip('@').split('@')
    if(len(tags)==1 and tags[0]==''):
        return set()
    else:
        return set(tags)

def readFile(fname):
    dateDict = {}
    dateRE = re.compile('\d\d\d\d-\d\d-\d\d')
    entryRE = re.compile('\A- ')
    with open(fname,'r') as f:
        for line in f:
            l = line.rstrip()
            if dateRE.match(l):
                dateDict[l] = []
                lastDate = l
            if entryRE.match(l):
                bothSides = l.strip('- ').split('.')
                tags = getTagsFromEntry(bothSides[1])
                dateDict[lastDate].append((bothSides[0],tags))
    return dateDict

def tags2str(tags):
    str = ''
    for tag in tags:
        str = str + ' @'+tag
    return str

def writeFile(fname,dateDict):
    with open(fname,'w') as f:
        for date in sorted(dateDict.keys()):
            print(date+'\n',file=f)
            for (entry,tags) in dateDict[date]:
                print('- '+entry+'.'+tags2str(tags),file=f)
            print(file=f)

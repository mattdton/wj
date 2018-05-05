import re
import datetime
from collections import Counter
from pint import UnitRegistry
ureg = UnitRegistry()

def getTagsFromEntry(string):
    tags = string.replace(' ','').lstrip('@').split('@')
    if(len(tags)==1 and tags[0]==''):
        return set()
    else:
        return set(tags)

def tags2str(tags):
    str = ''
    for tag in tags:
        str = str + ' @'+tag
    return str

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

def writeFile(fname,dateDict):
    with open(fname,'w') as f:
        for date in sorted(dateDict.keys()):
            print(date+'\n',file=f)
            for (entry,tags) in dateDict[date]:
                print('- '+entry+'.'+tags2str(tags),file=f)
            print(file=f)

def addNewEntry(entry,dateDict):
    bothSides = entry.split('.')
    if(len(bothSides)==1):
        print("Can't split on full stop.")
        return
    today = datetime.date.today().isoformat()
    if today not in dateDict.keys():
        dateDict[today] = []
    tags = getTagsFromEntry(bothSides[1])
    dateDict[today].append((bothSides[0],tags))

def countTags(dateDict):
    c = Counter()
    for date,val in dateDict.items():
        for entry,tags in val:
            for tag in tags:
                c[tag] += 1
    return c

def printTags(dateDict):
    tags = countTags(dateDict)
    print('File contains entries which use the following tags:')
    for tag in tags.keys():
        print('    '+tag)

def printEntriesWithTag(tag,dateDict):
    tmpDict = {}
    for date,val in dateDict.items():
        for entry,tags in val:
            if tag in tags:
                if date not in tmpDict.keys():
                    tmpDict[date] = []
                tmpDict[date].append(entry)
    for date in sorted(tmpDict):
        for entry in tmpDict[date]:
            print(date+' '+entry+'.')

def printTotalEffort(tag,dateDict):
    total = None
    for date,val in dateDict.items():
        for entry,tags in val:
            if tag in tags:
                splitEntry = entry.split(';')
                if len(splitEntry)==2:
                    if total is None:
                        total = ureg(splitEntry[1])
                    else:
                        total += ureg(splitEntry[1])
    if total.dimensionality=={'[time]':1.0}:
        print('{0:.2f} '.format(total))
    else:
        print(total)

def printEntriesForDate(date,dateDict):
    if date in dateDict.keys():
        for (entry,tags) in dateDict[date]:
            print('- '+entry+'.'+tags2str(tags))

def printDateRange(startDate,endDate,dateDict):
    d = startDate
    delta = datetime.timedelta(days=1)
    while d <= endDate:
        if d.isoformat() in dateDict.keys():
            print(d.isoformat())
            printEntriesForDate(d.isoformat(),dateDict)
            print()
        d+=delta

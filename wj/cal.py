import datetime

_dayName = {1:'Mo',2:'Tu',3:'We',4:'Th',5:'Fr',6:'Sa',7:'Su'}

def _lineHead(nday=37):
    out = ''
    for i in range(nday):
        out = out+' '+_dayName[i%7+1]
    return out

def _month2str(year,month):
    date = datetime.date(year,month,1)
    inc = datetime.timedelta(days=1)
    offset = (date.isoweekday()-1)*3
    out = offset*' '
    while date.month == month:
        out = out + '{0: >3}'.format(date.day)
        date = date + inc
    return out

def _chopMonthString(s):
    return [s[20*start:20*(start+1)] for start in range(5)]

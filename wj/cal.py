import datetime

from enum import Enum
class Escape(Enum):
    BEGIN = '\033\033[92m'
    END   = '\033[0m'

_dayName = {1:'Mo',2:'Tu',3:'We',4:'Th',5:'Fr',6:'Sa',7:'Su'}

def _title(year,month):
    date = datetime.date(year,month,1)
    return '{0:^21}'.format(date.strftime('%B'))

def _dayHead(nday=37):
    out = ''
    for i in range(nday):
        out = out+' '+_dayName[i%7+1]
    return out

def _month2str(year,month,dates=set()):
    date = datetime.date(year,month,1)
    inc = datetime.timedelta(days=1)
    offset = (date.isoweekday()-1)*3
    out = offset*' '
    while date.month == month:
        if date in dates:
            out = out + Escape.BEGIN.value+'{0: >3}'.format(date.day)+Escape.END.value
        else:
            out = out + '{0: >3}'.format(date.day)
        if date.isoweekday()==7:
            out = out + '\n'
        date = date + inc
    return out

def _chopMonthString(s):
    t = s.split('\n')
    out = ['{0:<21}'.format(i) for i in t]
    while len(out) < 6:
        out = out + [21*' ']
    return out

def composeMonth(year,month,dates=set()):
    """Format the dates in a month as a small block of text with a line
    for each week. Returns a list where each item is one of the lines.
    """
    output = [_title(year,month),_dayHead(7)]
    output.extend(_chopMonthString(_month2str(year,month,dates)))
    return output

def printYear(year,dates=set()):
    """Print the calendar for a year with four months on each row."""
    months = [composeMonth(year,month,dates) for month in range(1,13)]
    for group in range(3):
        index = 4*group
        for line in range(8):
            print(months[index][line],end='  ')
            print(months[index+1][line],end='  ')
            print(months[index+2][line],end='  ')
            print(months[index+3][line],end='\n')
        print('\n')

import datetime

_dayName = {1:'Mo',2:'Tu',3:'We',4:'Th',5:'Fr',6:'Sa',7:'Su'}

def _title(year,month):
    date = datetime.date(year,month,1)
    return '{0:^21}'.format(date.strftime('%B'))

def _dayHead(nday=37):
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
    return ['{0: <21}'.format(s[21*i:21*(i+1)]) for i in range(6)]

def composeMonth(year,month):
    """Format the dates in a month as a small block of text with a line
    for each week. Returns a list where each item is one of the lines.
    """
    output = [_title(year,month),_dayHead(7)]
    output.extend(_chopMonthString(_month2str(year,month)))
    return header

def printYear(year):
    """Print the calendar for a year with four months on each row."""
    months = [composeMonth(year,month) for month in range(1,13)]
    for group in range(3):
        index = 4*group
        for line in range(8):
            print(months[index][line],end='  ')
            print(months[index+1][line],end='  ')
            print(months[index+2][line],end='  ')
            print(months[index+3][line],end='\n')
        print('\n')

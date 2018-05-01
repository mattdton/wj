import wj_util as wj
import sys,os
import datetime
from argparse import ArgumentParser

fname = os.environ["WJ_FILENAME"]

def parse_args():
    parser = ArgumentParser()
    subparsers = parser.add_subparsers(help='commands')

    add_parser = subparsers.add_parser('add',
                                       help='Add a new entry for today.')

    add_parser.add_argument('entry',
                            action='store',
                            type=str,
                            help="New entry in the form: 'Sentence. @tag1 @tag2'")
    add_parser.set_defaults(func=addEntry)

    tags_parser = subparsers.add_parser('tags',
                                        help='Print the list of used tags.')
    tags_parser.set_defaults(func=printTags)

    tag_parser = subparsers.add_parser('tag',
                                      help='Print entries for a given tag.')
    tag_parser.add_argument('tag',
                            action='store',
                            type=str,
                            help='tag to print')
    tag_parser.set_defaults(func=printTagEntries)

    recent_parser = subparsers.add_parser('recent',
                                          help='Print entries for last fortnight.')
    recent_parser.set_defaults(func=printRecent)

    today_parser = subparsers.add_parser('today',
                                         help='Print entries for today.')
    today_parser.set_defaults(func=printTodayEntries)
    
    yesterday_parser = subparsers.add_parser('yesterday',
                                             help='Print entries for yesterday.')
    yesterday_parser.set_defaults(func=printYesterdayEntries)

    args = parser.parse_args()
    return args

def addEntry(args,dateDict):
    wj.addNewEntry(args.entry,dateDict)
    wj.writeFile(fname,dateDict)
    return

def printTags(args,dateDict):
    wj.printTags(dateDict)
    return

def printTagEntries(args,dateDict):
    wj.printEntriesWithTag(args.tag,dateDict)
    return

def printRecent(args,dateDict):
    delta=datetime.timedelta(days=-14)
    endDate = datetime.date.today()
    startDate = endDate+delta
    wj.printDateRange(startDate,endDate,dateDict)

def printTodayEntries(args,dateDict):
    date = datetime.date.today()
    wj.printEntriesForDate(date.isoformat(),dateDict)
    return

def printYesterdayEntries(args,dateDict):
    date = datetime.date.today() - datetime.timedelta(1)
    wj.printEntriesForDate(date.isoformat(),dateDict)
    return

def main():
    print('Opening %s'%fname)
    dateDict = wj.readFile(fname)

    args = parse_args()
    args.func(args,dateDict)

if __name__ == '__main__':
    main()

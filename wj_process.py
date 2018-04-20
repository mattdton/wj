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

    tag_parser = subparsers.add_parser('tag',
                                      help='Print entries for a given tag.')
    tag_parser.add_argument('tagID',
                            action='store',
                            type=str,
                            help='tag to print')
    tag_parser.set_defaults(func=printTagEntries)

    today_parser = subparsers.add_parser('today',
                                         help='Print entries for today.')
    today_parser.set_defaults(func=printTodayEntries)
    
    yesterday_parser = subparsers.add_parser('yesterday',
                                             help='Print entries for yesterday.')
    yesterday_parser.set_defaults(func=printYesterdayEntries)

    args = parser.parse_args()
    return args

def addEntry():
    return

def printTagEntries():
    return

def printTodayEntries():
    return

def printYesterdayEntries():
    return

def main():
    print('Opening %s'%fname)
    dateDict = wj.readFile(fname)
    print(dateDict)

if __name__ == '__main__':
    main()

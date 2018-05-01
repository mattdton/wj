# wj

`wj` is a simple tool for keeping track of task progress. All entries
are stored in a plain text file, so they can easily be read or edited
and are grouped by date.

The format is simple:

1. Dates are in YYYY-MM-DD format on a single line starting at the
   first character.

2. Entries start with "- " are followed by a *single* sentence which
   ends in a full stop and can have any number of tags (which start
   with an @).

So a file might look like:

    2018-04-20
    
    - Got wj working. @python @opensource
    
    2018-04-23
    
    - Fixed the README file. @opensource

The python package provides a simple command line interface that can
be used to add entries and produce reports on these files.

## Adding entries

Use `add`:

    wj add 'Worked on paper. @research'

## Producing simple reports

All entries with a particular tag:

    wj tag research

Everything for the last two weeks:

    wj recent

Everything that you've done today:

    wj today

Everything that you did yesterday:

    wj yesterday

Print a list of tags:

    wj tags


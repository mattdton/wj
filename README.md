# wj

`wj` is a simple tool for keeping track of progress on different
tasks. All entries are stored in a plain text file that's kept in a
central place. Entries are grouped by date so they can easily be read
or edited.

The format of the file is simple:

1. Dates are in YYYY-MM-DD format on a single line starting at the
   first character.

2. Entries start with "- " are followed by a *single* sentence which
   ends in a full stop. They can be followed by any number of tags
   starting with an @.

So a file might look like:

    2018-04-20
    
    - Got wj working. @python @opensource
    
    2018-04-23
    
    - Fixed the README file. @opensource

The python package provides a simple command line interface that can
be used to add entries and produce basic reports.

### Installing and using

To install, clone the repository and use pip:

    git clone git@github.com:tdm-dev/wj.git
    cd wj
    pip install .
    
`wj` uses an environment variable to find the journal. To set this
with bash call:

    export WJ_FILENAME=<path-to-journal>

To get a list of available commands call `wj --help` or `wj -h`:

    > wj --help
    usage: wj [-h] {add,tags,tag,recent,today,yesterday} ...
    
    positional arguments:
      {add,tags,tag,recent,today,yesterday}
                            commands
        add                 Add a new entry for today.
        tags                Print the list of used tags.
        tag                 Print entries for a given tag.
        recent              Print entries for last fortnight.
        today               Print entries for today.
        yesterday           Print entries for yesterday.
    
    optional arguments:
      -h, --help            show this help message and exit

### Adding entries

Use `add`:

    wj add 'Worked on paper. @research'

### Producing simple reports

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


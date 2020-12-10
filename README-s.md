# Scripts

`python3 -m pip install --user -r requirements.txt`

install requirements

## Auto Commit

insert in prepare.py

use argument `-c` to disable commit function

use argument `-m [your message]` to change commit message

## Scripts

prepare for commit

`python3 prepare.py`

use argument `-p` to set the work path

use argument `-s` to disable auto word statics and word cloud

use argument `-w` to assign the file to draw word cloud

use argument `-d` to format files

use argument `-t` for online mode

### Word Statistics

mystat.py

default sorting is by file name

use argument `-o` to sort by last changed time

### Word Cloud Picture

wc.py

s for save, p for perform, r for remove. Multiple using supported.

list of key words in file name parameter supported.

### Format Change Into MarkDown

doc.py

support doc, docx, txt

### Search All Files For Key Word

search.py

`python3 search.py [keyword]`

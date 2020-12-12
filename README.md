# My Stories

This project is used as an archive for all of my stories.

Release版本是纯代码，对所有人开放。建议的使用方法，在项目下建立工作文件夹，在工作文件夹内进行写作。（P.S.请手动修改prepare.py中-path一项的缺省值，将其调整为主要的工作目录）

# files changed at last commit

no file is changed.

# Scripts

`python3 -m pip install --user -r requirements.txt`

install requirements

## Auto Commit

insert in prepare.py

use argument `-c` to disable commit function

use argument `-m [your message]` to change commit message

use argument `-p` to disable push

## Scripts

prepare for commit

`python3 prepare.py`

use argument `-path` to set the work path

use argument `-s` to disable auto word statics and word cloud

use argument `-w` to assign the file to draw word cloud

use argument `-d` to format files

use argument `-t` for online mode

### Word Statistics

mystat.py

default sorting is by last changed time

use argument `-o` to sort by file name

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

### Format Files

formatter.py

support plaintext, markdown, python

`python3 formatter.py`

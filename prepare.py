import os
import mystat
import doc
import wc

myPath=os.getcwd()+'/DC'

mystat.WordStat(myPath)

# wc.WordPic(path=myPath,job='p',file=['赐福'])

# doc.getAllFiles(myPath)
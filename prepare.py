import os
import mystat
import doc
import wc

myPath=os.getcwd()+'/DC'

mystat.WordStat(myPath)

wc.WordPic(path=myPath,job='p')

# doc.getAllFiles(myPath)
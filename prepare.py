import os
import mystat
import doc
import wc

myPath=os.getcwd()

mystat.WordStat(myPath+'/DC')

wc.WordPic(myPath,'rp')

# doc.getAllFiles(myPath)
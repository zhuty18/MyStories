import os
import mystat
import doc
import wc

myPath=os.getcwd()

mystat.WordStat(myPath+'/DC')

wc.WordPic(path=myPath,job='p',file=['发现'])

# doc.getAllFiles(myPath)
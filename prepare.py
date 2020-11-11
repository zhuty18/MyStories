import os
import mystat
import wc

myPath=os.getcwd()+'/DC'

mystat.WordStat(myPath)

wc.WordPic(path=myPath,job='p')

# import doc

# doc.getAllFiles(myPath)
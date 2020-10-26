import os
import mystat
import doc
import wc

myPath=os.getcwd()

mystat.WordStat(myPath+'/DC')

wc.WordPic(path=myPath,job='p',file=['电影之夜','玫瑰'])

# doc.getAllFiles(myPath)
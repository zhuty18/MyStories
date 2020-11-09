import os
import mystat
import doc
import wc

myPath=os.getcwd()+'/DC'

mystat.WordStat(myPath)

wc.WordPic(path=myPath,job='p',file=['玫瑰','与生俱来'])

# doc.getAllFiles(myPath)
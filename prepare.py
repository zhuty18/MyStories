import os
import time
import argparse
import mystat
import wc

def autoCommit(message):
    mes=time.strftime("%m.%d %H:%M", time.localtime())+' '
    mes+=message
    mes='git commit -m \"'+mes+'\"'
    print(mes)
    os.system('git add .')
    os.system(mes)
    os.system('git push')

def terminal():
    parser=argparse.ArgumentParser()
    parser.add_argument('-n','--ncommit',type=bool,default=True,nargs='?')
    parser.add_argument('-m','--message',default='update')
    args=parser.parse_args()
    if args.ncommit:
        autoCommit(args.message)

myPath=os.getcwd()+'/DC'
mystat.WordStat(myPath)
wc.WordPic(path=myPath,job='p')
terminal()

# import doc
# doc.getAllFiles(myPath)
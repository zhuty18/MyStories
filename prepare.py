import os
import time
import argparse


def autoCommit(message):
    mes = time.strftime("%m.%d %H:%M", time.localtime())+' '
    mes += message
    mes = 'git commit -m \"'+mes+'\"'
    os.system('git add .')
    os.system(mes)
    os.system('git push')


def terminal():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--autocommit', type=bool,
                        default=True, nargs='?', const=False)
    parser.add_argument('-m', '--message', default='update')
    parser.add_argument('-p', '--workpath', type=str,
                        default='DC', nargs='?', const='')
    parser.add_argument('-s', '--statics', type=bool,
                        default=True, nargs='?', const=False)
    parser.add_argument('-w', '--wordcloud', type=str,
                        default='')
    parser.add_argument('-d', '--doc', type=bool,
                        default=False, nargs='?', const=True)
    args = parser.parse_args()
    return args


args = terminal()
# print(args)
myPath = os.getcwd() + '/' + args.workpath
if args.doc:
    import doc
    doc.getAllFiles(myPath)
if args.statics:
    import mystat
    import wc
    mystat.WordStat(myPath)
    if args.wordcloud == '':
        wc.WordPic(path=myPath, job='p')
    else:
        wc.WordPic(path=myPath, job='p', file=[args.wordcloud])
if args.autocommit:
    autoCommit(args.message)

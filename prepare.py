# coding=utf-8
import sys
sys.path.append('./scripts')
import os
import time
import argparse
import prefer as me


otherorder = ''
if me.order == 'time':
    otherorder = 'name'
elif me.order == 'name':
    otherorder = 'time'


def autoCommit(message):
    os.system('git add .')
    if not args.online:
        os.system('git pull')
    mes = time.strftime("%m.%d %H:%M", time.gmtime(time.time()+8*3600))+' '
    mes += message
    mes = 'git commit -m \"'+mes+'\"'
    os.system(mes)
    if args.push:
        os.system('git push')


def terminal():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--autocommit', type=bool,
                        default=me.commit, nargs='?', const=(not me.commit))
    parser.add_argument('-m', '--message', default=me.message)
    parser.add_argument('-path', '--workpath', type=str,
                        default=me.myPath, nargs='?', const='')
    parser.add_argument('-s', '--statistic', type=bool,
                        default=me.wordStat, nargs='?', const=(not me.wordStat))
    parser.add_argument('-w', '--wordcloud', type=str,
                        default=me.wordCloud)
    parser.add_argument('-o', '--sortorder', type=str,
                        default=me.order, nargs='?', const=otherorder)
    parser.add_argument('-p', '--push', type=bool,
                        default=me.push, nargs='?', const=(not me.push))
    parser.add_argument('-t', '--online', type=bool,
                        default=False, nargs='?', const=True)
    args = parser.parse_args()
    return args


args = terminal()
path = os.getcwd() + '/' + args.workpath
if args.online:
    import online
    change = online.Online(os.getcwd())
    change = change.total
    autoCommit('last change '+str(change))
else:
    if args.autocommit:
        autoCommit(args.message)
    if args.statistic:
        import mystat
        import wc
        mystat.Statistic(path, args.sortorder)
        if args.wordcloud == '':
            wc.WordPic(path=path, job=me.wordCloudJob)
        elif args.wordcloud == 'none':
            pass
        else:
            wc.WordPic(path=path, job=me.wordCloudJob, file=[args.wordcloud])

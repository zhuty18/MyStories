# coding=utf-8
import os
import time
import argparse
import prefer as me


otherorder = ''
if me.order is 'time':
    otherorder = 'name'
elif me.order is 'name':
    otherorder = 'time'


def autoCommit(message):
    mes = time.strftime("%m.%d %H:%M", time.gmtime(time.time()+8*3600))+' '
    mes += message
    mes = 'git commit -m \"'+mes+'\"'
    os.system('git add .')
    os.system(mes)
    if not args.online:
        os.system('git pull')
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
                        default='')
    parser.add_argument('-o', '--sortorder', type=str,
                        default=me.order, nargs='?', const=otherorder)
    parser.add_argument('-p', '--push', type=bool,
                        default=me.push, nargs='?', const=(not me.push))
    parser.add_argument('-t', '--online', type=bool,
                        default=False, nargs='?', const=True)
    args = parser.parse_args()
    return args


args = terminal()
# print(args)
path = os.getcwd() + '/' + args.workpath
if args.online:
    import online
    online.Online(os.getcwd())
    # import mystat
    # mystat.WordStat(myPath, 'time')
    autoCommit('update readme')
else:
    if args.statistic:
        import mystat
        import wc
        mystat.WordStat(path, args.sortorder)
        if args.wordcloud == '':
            wc.WordPic(path=path, job=me.wordCloudJob)
        else:
            wc.WordPic(path=path, job=me.wordCloudJob, file=[args.wordcloud])
    if args.autocommit:
        autoCommit(args.message)

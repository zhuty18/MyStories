import os
import time
import wc


class WordStat:
    dirs = []
    log = ['# online statistic result']

    def __init__(self, path, order, online=False):
        WordStat.dirs.append(Statistic(path, order))
        if online:
            f = open(os.getcwd()+'/README.md', 'a', encoding='utf-8')
            f.write('\n\n'.join(self.log))
            f.close()
        else:
            for i in self.dirs:
                i.writeResults()


class Statistic:
    def __init__(self, path, order):
        self.finish = []
        self.unfinished = []
        self.other = []
        self.path = path
        self.sort = order
        self.dir = path.replace(os.getcwd(), '')
        self.dir = self.dir.replace('\\', '/')
        self.dir = self.dir[1:]
        self.readHistory()
        self.getAllFiles(path)

    def readHistory(self):
        if os.path.exists(self.path+'/README.md'):
            f = open(self.path+'/README.md', 'r', encoding='utf-8')
            l = f.readlines()
            f.close()
            self.former = {}
            for i in l:
                if i.__contains__('.md'):
                    t = self.getStat(i)
                    self.former[t[0]] = t[1]

    def getStat(self, str):
        t = str.split('|')
        res = ['', 0]
        res[0] = t[1].split('[')[1]
        res[0] = res[0].split(']')[0]
        res[1] = int(t[2])
        return res

    def compareStat(self, k):
        t = self.getStat(k)
        before = 0
        if t[0] in self.former.keys():
            before = self.former[t[0]]
        if before != t[1]:
            WordStat.log.append(t[0]+'\t'+str(before)+'->'+str(t[1]))
            wc.files.append(t[0])

    def length(self, str):
        res = 0
        t = False
        for i in str:
            if i.isascii():
                t = True
                if i == ' ':
                    res += 1
            else:
                res += 1
                if t:
                    res += 1
                    t = False
        if t:
            res += 1
        return res

    def writeResults(self):
        if len(self.unfinished)+len(self.finish)+len(self.other) > 0:
            f = open(self.path+'/README.md', 'w', encoding='utf-8')
            f.write('# Word Stat Result\n\n')
            if self.sort == 'name':
                str = '|名称|字数|\n'
                str += '|:-|:-|\n'
            else:
                str = '|名称|字数|修改时间|\n'
                str += '|:-|:-|:-|\n'
            if len(self.unfinished) > 0:
                f.write('## To Be Continued\n\n')
                f.write(str)
                for i in self.unfinished:
                    f.write(i+'\n')
            if len(self.finish) > 0:
                f.write('\n## Finished\n\n')
                f.write(str)
                for i in self.finish:
                    f.write(i+'\n')
            if len(self.other) > 0:
                f.write('\n## Others\n\n')
                f.write(str)
                for i in self.other:
                    f.write(i+'\n')
            f.close()

    def write(self, info, type):
        self.compareStat(info)
        if type == 'fin':
            self.finish.append(info)
        elif type == 'unfinished':
            self.unfinished.append(info)
        else:
            self.other.append(info)

    def changeTime(self, path):
        t = os.path.getmtime(path)
        t = time.localtime(t)
        res = str(t.tm_mon).zfill(2)+'.'+str(t.tm_mday).zfill(2) + \
            ' '+str(t.tm_hour).zfill(2)+':'+str(t.tm_min).zfill(2)
        return res

    def stat(self, path, name):
        if name.endswith('.md') and (not name.__contains__('README')):
            file = open(path, 'r', encoding='utf-8')
            type = ''
            num = 0
            info = ''
            for i in file.readlines():
                num += self.length(i.strip())
                if i.__contains__('END'):
                    type = 'fin'
            file.close()
            if name.__contains__('摘抄'):
                type = 'other'
            if type == '':
                type = 'unfinished'
            info = '|['+name[0:-3]+']('+name+')|'
            info += str(num)+'|'
            if self.sort == 'time':
                info += self.changeTime(path)+'|'
            self.write(info, type)

    def getAllFiles(self, path):
        list = os.listdir(path)
        result = []
        if self.sort == 'name':
            from xpinyin import Pinyin
            pin = Pinyin()
            for item in list:
                result.append((pin.get_pinyin(item), item))
            result.sort()
        elif self.sort == 'time':
            for item in list:
                subdir = os.path.join(path, item)
                time = os.path.getmtime(subdir)
                result.append((time, item))
            result.sort()
            result.reverse()
        for i in range(len(result)):
            list[i] = result[i][1]
        for i in list:
            subdir = os.path.join(path, i)
            if os.path.isdir(subdir) and not subdir.__contains__('参考'):
                WordStat.dirs.append(Statistic(subdir, self.sort))
            else:
                self.stat(subdir, i)

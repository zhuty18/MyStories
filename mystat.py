# coding=utf-8
import os
import time
from wc import files
from utils import length


def changeTime(timestamp):
    t = time.gmtime(timestamp+8*3600)
    res = str(t.tm_mon).zfill(2)+'.'+str(t.tm_mday).zfill(2) + \
        ' '+str(t.tm_hour).zfill(2)+':'+str(t.tm_min).zfill(2)
    return res


class Statistic:
    initialized = False

    def staticInit(self):
        import git
        Statistic.repo = git.Repo('./')
        Statistic.initialized = True

    def __init__(self, path, order):
        self.finish = []
        self.unfinished = []
        # self.other = []
        self.former = {}
        self.path = path
        self.sort = order
        self.dir = path.replace(os.getcwd(), '')
        self.dir = self.dir.replace('\\', '/')
        self.dir = self.dir[1:]
        if not Statistic.initialized:
            self.staticInit()
        self.readHistory()
        self.getAllFiles(path)
        self.writeResults()

    def readHistory(self):
        if os.path.exists(self.path+'/README.md') and self.path != os.getcwd()+'/':
            f = open(self.path+'/README.md', 'r', encoding='utf-8')
            l = f.readlines()
            f.close()
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
            print(t[0]+'\t'+str(before)+'->'+str(t[1]))
            files.append(t[0])

    def writeResults(self):
        if len(self.unfinished)+len(self.finish) > 0:
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
                f.write('\n'.join(self.unfinished))
                f.write('\n')
            if len(self.finish) > 0:
                f.write('\n## Finished\n\n')
                f.write(str)
                f.write('\n'.join(self.finish))
                f.write('\n')
            f.close()

    def write(self, info, type):
        self.compareStat(info)
        if type == 'fin':
            self.finish.append(info)
        else:
            self.unfinished.append(info)

    def stat(self, path, name, timestamp):
        if name.endswith('.md') and (not name.__contains__('README')):
            file = open(path, 'r', encoding='utf-8')
            type = 'unfinished'
            num = 0
            info = ''
            for i in file.readlines():
                num += length(i.strip())
                if i.__contains__('END'):
                    type = 'fin'
            file.close()
            info = '|['+name[0:-3]+']('+name+')|'
            info += str(num)+'|'
            if self.sort == 'time':
                info += changeTime(timestamp)+'|'
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
                file = subdir.replace(os.getcwd(), '.')
                file = file.replace('\\', '/')
                print(file)
                # print(repo.ignored(file))
                if not file.__contains__('.git') and not self.repo.ignored(file):
                    commit = self.repo.iter_commits(
                        paths=file, max_count=1).__next__()
                    t = commit.committed_date
                    result.append((t, item))
            result.sort()
            result.reverse()
            # print(result)
        for i in range(len(result)):
            list[i] = (result[i][1], result[i][0])
        for i in list:
            subdir = os.path.join(path, i[0])
            if os.path.isdir(subdir) and not subdir.__contains__('参考') and not subdir.__contains__('/.'):
                Statistic(subdir, self.sort)
            else:
                self.stat(subdir, i[0], i[1])

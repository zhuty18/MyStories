# coding=utf-8
import os
from utils import length


class Online:
    log = []

    def __init__(self, path):
        self.history = {}
        self.exist = {}
        self.total = 0
        self.readHistory()
        self.statFiles(path)
        self.writeResult()
        self.updateHistory()

    def readHistory(self):
        if os.path.exists('history.txt'):
            with open('history.txt', 'r', encoding='utf-8') as f:
                for i in f.readlines():
                    h = i.strip()
                    h = h.split('\t')
                    self.history[h[0]] = int(h[1])

    def statFiles(self, path):
        list = os.listdir(path)
        list.sort()
        for i in list:
            subdir = os.path.join(path, i)
            if os.path.isdir(subdir):
                self.statFiles(subdir)
            else:
                self.stat(subdir, i)

    def stat(self, path, name):
        if (name.endswith('.md') and (not name.__contains__('README'))) or name == "note.txt":
            file = open(path, 'r', encoding='utf-8')
            num = 0
            for i in file.readlines():
                num += length(i.strip())
            file.close()
            before = 0
            if name in self.history.keys():
                before = self.history[name]
            if before != num:
                self.log.append('|'+name.replace('.md', '') + '|' +
                                str(before)+'|'+str(num)+'|'+str(num-before)+'|')
                if num > before:
                    self.total += num-before
                else:
                    self.total += before-num
            self.history[name] = num
            self.exist[name] = True

    def writeResult(self):
        f = open(os.getcwd()+'/README.md', 'w', encoding='utf-8')
        f1 = open('README-o.md', 'r', encoding='utf-8')
        f.writelines(f1.readlines())
        f1.close()
        if len(self.log) != 0:
            f.write('\n# files changed at last commit\n\n')
            f.write('|文件名|上次提交时字数|本次提交字数|字数变化|\n')
            f.write('|:-|:-|:-|:-|\n')
            f.write('\n'.join(self.log))
            f.write('\n')
        f.write('\n')
        f2 = open('README-s.md', 'r', encoding='utf-8')
        f.writelines(f2.readlines())
        f2.close()
        f.close()

    def updateHistory(self):
        with open('history.txt', 'w', encoding='utf-8') as f:
            for i in self.exist.keys():
                f.write(i+'\t'+str(self.history[i])+'\n')

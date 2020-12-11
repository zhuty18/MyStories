# coding=utf-8
import os
import sys


class Searcher:
    def __init__(self, path, keyword):
        self.key = keyword
        self.pth = path
        self.searchDir(path)

    def searchDir(self, path):
        list = os.listdir(path)
        for i in list:
            subdir = os.path.join(path, i)
            if os.path.isdir(subdir):
                self.searchDir(subdir)
            elif subdir.endswith('.md'):
                self.searchOne(subdir)

    def searchOne(self, file):
        with open(file, 'r', encoding='utf-8') as f:
            have = False
            for i in f.readlines():
                if i.__contains__(self.key):
                    if not have:
                        print(file.replace(self.pth, ''))
                        have = True
                    print(i.strip())
            if have:
                print()


key = sys.argv[1]
Searcher(os.getcwd()+'/DC', key)

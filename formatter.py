# coding=utf-8
import os


def formatter(path):
    list = os.listdir(path)
    for i in list:
        subdir = os.path.join(path, i)
        if os.path.isdir(subdir):
            formatter(subdir)
        elif subdir.endswith('.md') or subdir.endswith('.txt') or subdir.endswith('.py'):
            f = open(subdir, 'r', encoding='utf-8')
            content = f.readlines()
            f.close()
            f = open(subdir, 'w', encoding='utf-8')
            # print(content)
            for i in content:
                if subdir.endswith('.py'):
                    f.write(i.strip('\n')+'\n')
                else:
                    f.write(i.strip()+'\n')
            f.close()
            # if os.path.exists(subdir+'(1)'):
            #     os.remove(subdir+'(1)')


formatter('./')

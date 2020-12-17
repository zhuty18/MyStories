# coding=utf-8
import os
import platform
import docx
import argparse
import prefer
try:
    from win32com import client as wc
except ImportError:
    print('This script is only runnable on Windows OS.')
    print('Your are on '+platform.system()+' OS!')


def toMD(path, name, rm):
    if name.startswith('~'):
        pass
    elif name.endswith('.docx'):
        print(name)
        file = docx.Document(path)
        outfile = open(path.replace('.docx', '.md'), 'w', encoding='utf-8')
        outfile.write("# ")
        for p in file.paragraphs:
            outfile.write(p.text+'\n\n')
        outfile.close()
    elif name.endswith('.doc'):
        word = wc.Dispatch('Word.Application')
        doc = word.Documents.Open(path)        # 目标路径下的文件
        doc.SaveAs(path+'x', 12, False, "", True, "",
                   False, False, False, False)  # 转化后路径下的文件
        doc.Close()
        word.Quit()
        toMD(path+'x', name+'x', rm)
    elif name.endswith('.txt'):
        print(name)
        fi = open(path, 'r', encoding='utf-8')
        fo = open(path.replace('.txt', '.md'), 'w', encoding='utf-8')
        for i in fi.readlines():
            fo.write(i+'\n')
        fi.close()
        fo.close()
    if rm:
        os.remove(path)


def getAllFiles(path, rm):
    list = os.listdir(path)
    list.sort()
    for i in list:
        subdir = os.path.join(path, i)
        if os.path.isdir(subdir) and not subdir.__contains__('.git'):
            getAllFiles(subdir, rm)
        else:
            toMD(subdir, i, rm)


parser = argparse.ArgumentParser()
parser.add_argument('-r', '--remove', type=bool,
                    default=False, nargs='?', const=True)
args = parser.parse_args()
getAllFiles(os.getcwd()+'/'+prefer.myPath, args.remove)

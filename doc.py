import docx
import os
from win32com import client as wc

def stat(path,name):
    if name.endswith('.docx'):
        print(name)
        file=docx.Document(path)
        fout=open(path.replace('.docx','.md'),'w',encoding='utf-8')
        fout.write("# ")
        for p in file.paragraphs:
            fout.write(p.text+'\n\n')
        os.remove(path)
        fout.close()
    elif name.endswith('.doc'):
        word = wc.Dispatch('Word.Application')
        doc = word.Documents.Open(path)        # 目标路径下的文件
        doc.SaveAs(path+'x', 12, False, "", True, "", False, False, False, False)  # 转化后路径下的文件    
        doc.Close()
        word.Quit()
        os.remove(path)
        stat(path+'x',name+'x')
    elif name.endswith('.txt'):
        print(name)
        fi=open(path,'r')
        fo=open(path.replace('.txt','.md'),'w',encoding='utf-8')
        fo.write(fi.read())
        fi.close()
        fo.close()
        os.remove(path)

def getAllFiles(path):
    list=os.listdir(path)
    list.sort()
    for i in list:
        subdir=os.path.join(path,i)
        if os.path.isdir(subdir):
            getAllFiles(subdir)
        else:
            stat(subdir,i)

path=os.getcwd()
getAllFiles(path+'\\'+"O\\")
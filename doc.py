import docx
import os

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


def getAllFiles(path):
    list=os.listdir(path)
    list.sort()
    for i in list:
        subdir=os.path.join(path,i)
        if os.path.isdir(subdir):
            getAllFiles(subdir)
        else:
            stat(subdir,i)

getAllFiles("DC/")
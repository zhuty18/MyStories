import os

def write(info,f):
    f.write(info)
    print(info.strip())

def stat(path,name,f):
    if name.endswith(".md") and name!="README.md" and name!="字数统计.md":
        file=open(path,'r',encoding='utf-8')
        finished=False
        num=0
        info=""
        for i in file.readlines():
            num+=len(i.strip())
            if(i.__contains__("END")):
                finished=True
        info=name+"\t"+str(num)
        if finished:
            info+="\t"+"Finished"
        info+='\n\n'
        write(info,f)

def getAllFiles(path,f):
    list=os.listdir(path)
    for i in list:
        subdir=os.path.join(path,i)
        if os.path.isdir(subdir):
            getAllFiles(subdir,f)
        else:
            stat(subdir,i,f)


path = os.getcwd()
f=open('字数统计.md','w')
f.write("# 字数统计\n\n")
getAllFiles(path,f)
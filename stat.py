import os

def write(info,f):
    f.write(info)
    print(info.strip())

def stat(path,name,f):
    if name.endswith(".md") and name!="README.md":
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
f=open('README.md','w')
f.write('# MyStories\n\n')
f.write('This project is used as an archive for all of my stories.\n\n')
f.write('## Word Statistics\n\n')
f.write('only tested on python3.7.4\n\n')
f.write('`python stat.py`\n\n')
f.write("## Result\n\n")
getAllFiles(path,f)
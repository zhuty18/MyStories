import os

finish=[]
unfin=[]

def writeResults(f):
    f.write("### To Be Continued\n\n")
    f.write("|名称|位置|字数|\n")
    f.write("|:-|:-|:-|\n")
    for i in unfin:
        f.write(i+"\n")
    f.write("\n### Finished\n\n")
    f.write("|名称|位置|字数|\n")
    f.write("|:-|:-|:-|\n")
    for i in finish:
        f.write(i+"\n")

def write(info,fin):
    if fin:
        finish.append(info)
    else:
        unfin.append(info)

def stat(path,name):
    if name.endswith(".md") and name!="README.md":
        file=open(path,'r',encoding='utf-8')
        finished=False
        num=0
        info=""
        for i in file.readlines():
            num+=len(i.strip())
            if(i.__contains__("END")):
                finished=True
        info="|"+name[0:-3]+"|"
        k=path.replace(name,"")
        k=k.replace(os.getcwd(),".")
        k=k.replace("\\","/")
        if len(k)==1:
            k+="/"
        elif len(k)>2:
            k=k[0:-1]
        info+=k+"|"
        info+=str(num)+"|"
        write(info,finished)

def getAllFiles(path):
    list=os.listdir(path)
    for i in list:
        subdir=os.path.join(path,i)
        if os.path.isdir(subdir):
            getAllFiles(subdir)
        else:
            stat(subdir,i)

path = os.getcwd()
f=open('README.md','w',encoding="utf-8")
f.write('# MyStories\n\n')
f.write('This project is used as an archive for all of my stories.\n\n')
f.write('## Word Statistics\n\n')
f.write('only tested on python3.7.4\n\n')
f.write('`python stat.py`\n\n')
f.write("## Result\n\n")
getAllFiles(path)
writeResults(f)
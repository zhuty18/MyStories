import os
import time

finish=[]
unfin=[]
other=[]

def writeResults(f):
    f.write('### To Be Continued\n\n')
    str='|名称|位置|字数|修改时间|\n'
    str+='|:-|:-|:-|:-|\n'
    f.write(str)
    for i in unfin:
        f.write(i+'\n')
    f.write('\n### Finished\n\n')
    f.write(str)
    for i in finish:
        f.write(i+'\n')
    f.write('\n### Others\n\n')
    f.write(str)
    for i in other:
        f.write(i+'\n')

def write(info,type):
    if type=='fin':
        finish.append(info)
    elif type=='unfin':
        unfin.append(info)
    else:
        other.append(info)

def changeTime(path):
    t=os.path.getmtime(path)
    t=time.localtime(t)
    res=str(t.tm_mon).zfill(2)+'.'+str(t.tm_mday).zfill(2)+' '+str(t.tm_hour).zfill(2)+':'+str(t.tm_min).zfill(2)
    return res

def stat(path,name):
    if name.endswith('.md') and (not name.__contains__('README')):
        file=open(path,'r',encoding='utf-8')
        type=''
        num=0
        info=''
        for i in file.readlines():
            num+=len(i.strip())
            if(i.__contains__('END')):
                type='fin'
        if name.__contains__('摘抄'):
            type='other'
        if type=='':
            type='unfin'
        info='|'+name[0:-3]+'|'
        k=path.replace(name,'')
        k=k.replace(os.getcwd(),'.')
        k=k.replace('\\','/')
        if len(k)==1:
            k+='/'
        elif len(k)>2:
            k=k[0:-1]
        info+=k+'|'
        info+=str(num)+'|'
        info+=changeTime(path)+'|'
        print(name+'\t'+str(num)+'\t'+type)
        write(info,type)

def getAllFiles(path):
    list=os.listdir(path)
    for i in list:
        subdir=os.path.join(path,i)
        if os.path.isdir(subdir):
            getAllFiles(subdir)
        else:
            stat(subdir,i)

path = os.getcwd()
f=open('README.md','w',encoding='utf-8')
f2=open('README-o.md','r',encoding='utf-8')
for i in f2.readlines():
    f.write(i)
f2.close()
getAllFiles(path)
writeResults(f)
f.close()

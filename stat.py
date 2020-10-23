import os
import time
import jieba
import jieba.analyse

class KeyWord:
    def __init__(self,path):
        f=open(path,'r',encoding='utf-8')
        str=f.read()
        self.k1=jieba.analyse.extract_tags(str,topK=10)
        print(self.k1)
        self.k2=jieba.analyse.textrank(str,topK=10)
        print(self.k2)
        print()
        f.close()
    def keywords(self):
        return ' '.join(self.k1)+'\t'+' '.join(self.k2)

class Statics:
    def __init__(self):
        self.finish=[]
        self.unfin=[]
        self.other=[]
        path = os.getcwd()
        f=open('README.md','w',encoding='utf-8')
        f2=open('README-o.md','r',encoding='utf-8')
        for i in f2.readlines():
            f.write(i)
        f2.close()
        self.getAllFiles(path)
        self.writeResults(f)
        f.close()

    def length(self,str):
        res=0
        t=False
        for i in str:
            if i.isascii():
                t=True
                if i==' ':
                    res+=1
            else:
                res+=1
                if t:
                    res+=1
                    t=False
        if t:
            res+=1
        return res

    def writeResults(self,f):
        f.write('### To Be Continued\n\n')
        str='|名称|位置|字数|修改时间|\n'
        str+='|:-|:-|:-|:-|\n'
        f.write(str)
        for i in self.unfin:
            f.write(i+'\n')
        f.write('\n### Finished\n\n')
        f.write(str)
        for i in self.finish:
            f.write(i+'\n')
        f.write('\n### Others\n\n')
        f.write(str)
        for i in self.other:
            f.write(i+'\n')

    def write(self,info,type):
        if type=='fin':
            self.finish.append(info)
        elif type=='unfin':
            self.unfin.append(info)
        else:
            self.other.append(info)

    def changeTime(self,path):
        t=os.path.getmtime(path)
        t=time.localtime(t)
        res=str(t.tm_mon).zfill(2)+'.'+str(t.tm_mday).zfill(2)+' '+str(t.tm_hour).zfill(2)+':'+str(t.tm_min).zfill(2)
        return res

    def stat(self,path,name):
        if name.endswith('.md') and (not name.__contains__('README')):
            file=open(path,'r',encoding='utf-8')
            type=''
            num=0
            info=''
            for i in file.readlines():
                num+=self.length(i.strip())
                if i.__contains__('END'):
                    type='fin'
            file.close()
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
            info+=self.changeTime(path)+'|'
            print(name+'\t'+str(num)+'\t'+type)
            wc=KeyWord(path)
            self.write(info,type)

    def getAllFiles(self,path):
        list=os.listdir(path)
        list.sort()
        for i in list:
            subdir=os.path.join(path,i)
            if os.path.isdir(subdir):
                self.getAllFiles(subdir)
            else:
                self.stat(subdir,i)

def main():
    s=Statics()

main()
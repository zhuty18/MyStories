import os
import time
from pypinyin import lazy_pinyin

class WordStat:
    dirs=[]
    def __init__(self,path):
        WordStat.dirs.append(Statics(path))
        for i in self.dirs:
            i.writeResults()


class Statics:
    def __init__(self,path):
        self.finish=[]
        self.unfin=[]
        self.other=[]
        self.path=path
        self.dir=path.replace(os.getcwd(),'')
        self.dir=self.dir.replace('\\','/')
        self.dir=self.dir[1:]
        self.readHistory()
        self.getAllFiles(path)

    def readHistory(self):
        f=open(self.path+'/README.md','r',encoding='utf-8')
        l=f.readlines()
        f.close()
        self.former={}
        for i in l:
            if i.__contains__('.md'):
                t=self.getStat(i)
                self.former[t[0]]=t[1]

    def getStat(self,str):
        t=str.split('|')
        res=['',0]
        res[0]=t[1].split('[')[1]
        res[0]=res[0].split(']')[0]
        res[1]=int(t[2])
        return res

    def compareStat(self,k):
        t=self.getStat(k)
        before=0
        if t[0] in self.former.keys():
            before=self.former[t[0]]
        if before != t[1]:
            print(t[0]+'\t'+str(before)+'->'+str(t[1]))

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

    def writeResults(self):
        if len(self.unfin)+len(self.finish)+len(self.other)>0:
            f=open(self.path+'/README.md','w',encoding='utf-8')
            f.write('# Word Stat Result\n\n')
            str='|名称|字数|\n'
            str+='|:-|:-|\n'
            if len(self.unfin)>0:
                f.write('## To Be Continued\n\n')
                f.write(str)
                for i in self.unfin:
                    f.write(i+'\n')
                    self.compareStat(i)
            if len(self.finish)>0:
                f.write('\n## Finished\n\n')
                f.write(str)
                for i in self.finish:
                    f.write(i+'\n')
                    self.compareStat(i)
            if len(self.other)>0:
                f.write('\n## Others\n\n')
                f.write(str)
                for i in self.other:
                    f.write(i+'\n')
                    self.compareStat(i)
            f.close()

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
            info='|['+name[0:-3]+']('+name+')|'
            info+=str(num)+'|'
            self.write(info,type)

    def getAllFiles(self,path):
        list=os.listdir(path)
        list.sort(key=lambda char: lazy_pinyin(char)[0][0])
        for i in list:
            subdir=os.path.join(path,i)
            if os.path.isdir(subdir) and not subdir.__contains__('参考'):
                WordStat.dirs.append(Statics(subdir))  
            else:
                self.stat(subdir,i)

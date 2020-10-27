import os
import time

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
        self.getAllFiles(path)
        self.path=path
        self.dir=path.replace(os.getcwd(),'')
        self.dir=self.dir.replace('\\','/')
        self.dir=self.dir[1:]

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
            if len(self.finish)>0:
                f.write('\n## Finished\n\n')
                f.write(str)
                for i in self.finish:
                    f.write(i+'\n')
            if len(self.other)>0:
                f.write('\n## Others\n\n')
                f.write(str)
                for i in self.other:
                    f.write(i+'\n')
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
            print(name+'\t'+str(num)+'\t'+type)
            self.write(info,type)

    def getAllFiles(self,path):
        list=os.listdir(path)
        list.sort()
        for i in list:
            subdir=os.path.join(path,i)
            if os.path.isdir(subdir) and not subdir.__contains__('参考'):
                WordStat.dirs.append(Statics(subdir))  
            else:
                self.stat(subdir,i)

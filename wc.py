import os
import jieba
import jieba.analyse
import wordcloud
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

class WordPic:
    def __init__(self,path,job):
        self.font=fm.FontProperties(fname='myfont.ttf',size=15)
        self.job=job
        jieba.load_userdict('mydict')
        self.drawFiles(path)
    def drawFiles(self,path):
        list=os.listdir(path)
        list.sort()
        for i in list:
            subdir=os.path.join(path,i)
            if os.path.isdir(subdir):
                self.drawFiles(subdir)
            else:
                self.drawPic(subdir,i)
    def drawPic(self,path,name):
        if name.endswith('.md') and (not name.__contains__('README')):
            if self.job=='r':
                os.remove(path.replace('.md','.png'))
            else:
                f=open(path,'r',encoding='utf-8')
                str=f.read()
                keywords=jieba.analyse.extract_tags(str,withWeight=True,topK=50)
                print(name.replace('.md',''))
                print(keywords)
                print()
                fre={keyword[0]:keyword[1] for keyword in keywords}
                wc=wordcloud.WordCloud(font_path="myfont.ttf",width=600,height=400)
                wc.fit_words(fre)
                if self.job.__contains__('s'):
                    wc.to_file(path.replace('.md','.png'))
                if self.job.__contains__('p'):
                    plt.imshow(wc)
                    plt.title(path.replace('.md',''),fontproperties=self.font)
                    plt.ion()
                    plt.pause(1)
                    plt.close()
                if self.job.__contains__('r'):
                    os.remove(path.replace('.md','.png'))

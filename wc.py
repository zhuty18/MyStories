import os
import jieba
import jieba.analyse
import wordcloud

class WordPic:
    def __init__(self,path):
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
            f=open(path,'r',encoding='utf-8')
            str=f.read()
            keywords=jieba.analyse.extract_tags(str,withWeight=True,topK=50)
            fre={keyword[0]:keyword[1] for keyword in keywords}
            wc=wordcloud.WordCloud(font_path="myfont.ttf",width=600,height=400)
            wc.fit_words(fre)
            wc.to_file(path.replace('.md','.png'))

path = os.getcwd()
WordPic(path)
import os
import jieba
import jieba.analyse
import wordcloud
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

class WordPic:
    def __init__(self):
        self.font=FontProperties(fname=r"myfont.ttf", size=14)
        path = os.getcwd()
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
            keywords=jieba.analyse.extract_tags(str,withWeight=True)
            fre={keyword[0]:keyword[1] for keyword in keywords}
            wc=wordcloud.WordCloud(font_path="myfont.ttf")
            wc.fit_words(fre)
            plt.imshow(wc)
            plt.gca().get_xaxis().set_visible(False)
            plt.gca().get_yaxis().set_visible(False)
            plt.title(name.replace('.md',''),fontproperties=self.font)
            plt.ion()
            plt.pause(1)
            plt.close()

wp=WordPic()
import os
import re


epName = {}
list = os.listdir(".")


def rename(s2):
    t1 = re.compile(r'E(.*?) ', re.S)
    t2 = re.compile(r'- (.*?) [(]', re.S)
    s = 'E'+re.findall(t1, s2)[0]
    s1 = re.findall(t2, s2)[0]+'ddd'
    t3 = re.compile(r'- (.*?)ddd', re.S)
    s1 = re.findall(t3, s1)[0]
    s1 = s1.replace(' ', '')
    s1 = s1.replace('\'', '')
    s1 = s1.replace(',', '')
    s = "Justice.League.Action.Shorts.S01"+s+'.'+s1+".720p.WEB-DL.H.264"
    return s


def cut(str):
    t = re.compile(r'2019.(.*)1080p', re.S)
    return re.findall(t, str)[0]


def getEpName():
    for i in list:
        if i.__contains__(".ass"):
            k = cut(i)
            epName[k.split('.')[0]] = k
    print(epName)


def rename2(str):
    k = cut(str)
    if k.split('.')[0] in epName.keys():
        m = epName[k.split('.')[0]]
        str = str.replace(k, m)
    return str


def exc(forma):
    for i in list:
        if i.__contains__(forma):
            s = rename2(i)
            print(s)
            m = "ren \""+i+"\" \""+s+forma+"\""
            # print(m)
            os.system(m)

def exc2(f,t):
    for i in list:
        if i.__contains__(f):
            s = i.replace(f,t)
            print(s)
            m = "ren \""+i+"\" \""+s+"\""
            # print(m)
            os.system(m)

exc2("720p","1080p")
import sys
from utils import length

filename = sys.argv[1]
if not filename.endswith(".md"):
    print("only support MarkDown files!")
else:
    f = open(filename, 'r', encoding='utf-8')
    filename = filename.replace('\\', '/')
    filename = filename.split('/')
    filename = filename[-1]
    filename = filename.replace('.md', '')
    chapter = ''
    total = 0
    num = 0
    for i in f.readlines():
        if i.startswith('#'):
            if chapter != '':
                print(chapter+'\t'+str(num))
                total += num
                num = 0
            chapter = i.strip('#').strip()
        num += length(i.strip())
    print(chapter+'\t'+str(num))
    total += num
    print(filename+'\t'+str(total))

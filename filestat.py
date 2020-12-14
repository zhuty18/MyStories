import sys
import mystat

filename = sys.argv[1]
if not filename.endswith(".md"):
    print("only support MarkDown files!")
else:
    f = open(filename, 'r', encoding='utf-8')
    out = open('result.md', 'w', encoding='utf-8')
    out.write('# 字数统计结果\n\n')
    out.write('['+filename+']('+filename+')\n\n')
    filename = filename.replace('\\', '/')
    filename = filename.split('/')
    filename = filename[-1]
    filename = filename.replace('.md', '')
    out.write('|'+filename+'|字数|\n')
    out.write('|:-|:-|\n')
    chapter = ''
    total = 0
    num = 0
    for i in f.readlines():
        if i.startswith('#'):
            if chapter != '':
                out.write('|'+chapter+'|'+str(num)+'|\n')
                total += num
                num = 0
            chapter = i.strip('#').strip()
        num += mystat.Statistic.length(None, i)
    out.write('|'+chapter+'|'+str(num)+'|\n')
    total += num
    out.write('|全文|'+str(total)+'|\n')

path = "../DC/DC饶舌大战-箭闪.md"
k = "../DC/DC饶舌大战-箭闪-2.md"

inf = open(path, 'r', encoding='utf-8')
ouf = open(k, 'w', encoding='utf-8')

ouf.write(inf.readline())
ouf.write(inf.readline())

i = inf.readline()
while True:
    sen = i+inf.readline()
    while sen == "\n\n":
        ouf.write(sen)
        sen = inf.readline() + inf.readline()
    szh = inf.readline()
    inf.readline()
    ouf.write(szh+sen)
    i = inf.readline()
    if i == "":
        break

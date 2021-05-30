# coding=utf-8

def length(str):
    res = 0
    t = False
    for i in str:
        if i.isascii():
            t = True
            if i == ' ':
                res += 1
        else:
            res += 1
            if t:
                res += 1
                t = False
    if t:
        res += 1
    return res

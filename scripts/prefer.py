# coding=utf-8
# 是否使用git提交
commit = True
# 不使用-m参数时的提交默认信息
message = 'update'
# 是否推送到远程分支
push = True
# 主要工作路径，不要是根目录，README会被覆盖
myPath = 'DC'
# 是否进行字数统计
wordStat = True
# 字数统计的顺序
# time代表按文件上一次提交的时间排序
# name代表按文件名（拼音顺序）进行排序
order = 'time'
# 词云生成词云的文件范围
# 空字符串表示生成所有字数变化文件的词云
# none表示不生成词云
# 其他字符串表示生成文件名含此字符串的词云
wordCloud = 'none'
# 词云统计后要做的工作
# s 生成与文档同名的.png文件，并保存在同一路径下
# p 生成词云图片并显示
# r 删除保存的词云图片
# 可以同时使用多个工作，例如sp
wordCloudJob = 'p'

# My Archive

为我个人写过的故事做一个线上存档。

# all categories

|所有文件夹|
|:-|
|[DC](/DC)|
|[数码宝贝](/DM)|
|[鬼泣](/DMC)|
|[童话系列（欧美）](/FT)|
|[银魂](/GTM)|
|[漫威](/M)|
|[原创](/O)|
|[其他](/Others)|
|[全职](/QZ)|
|[影评](/SC)|
|[食物语](/SWY)|
|[X战警](/X)|
|[仙剑](/XJ)|
|[阴阳师](/YYS)|
|[蝙绿官糖](/batlantern)|
|[翻译](/translation)|

# Scripts

## 使用方法

1. 安装 python

开发使用的 python 版本是 3.7.4，在 Ubuntu20.04 & Ubuntu18.04 上，用 python3.8 做过测试。

请确保安装的 python 版本不低于 3.7。

2. 安装依赖

执行命令`python -m pip install --user -r data/requirements.txt`即可

3. 根据你需要的功能运行脚本

## 主要功能

在[scripts/personal.py](./scripts/personal.py)中进行了一些默认值的设定，请在其中根据自己的喜好进行修改

### 自动使用 git 提交

执行命令`python update.py`

相关参数如下

|参数|含义|效果|
|:-|:-|:-|
|-a|是否添加所有修改|使用此参数，行为与默认值不同|
|-c|是否提交|使用此参数，行为与默认值不同|
|-m|提交信息|与`git commit -m [message]`的效果类似<br>如果不使用此参数，则会按照默认的信息提交|
|-p|是否推送到远程分支|使用此参数，行为与默认值不同|

如果不提交，则参数没有意义。

### 字数统计

从工作文件夹起，统计其与其所有子文件夹（多层嵌套）内各自存在的 MarkDown 文档的字数，在对应路径下生成 README.md 文件。

会根据是否完成进行分类，文档内包含"END"（大小写敏感）会被认为是完成的作品，不包含则是未完成的作品。

相关参数如下

|参数|含义|效果|
|:-|:-|:-|
|-s|字数统计|使用此参数，统计行为与默认值不同|
|-o|排序顺序|使用此参数，排序方法与默认值不同|
<!--
|-wc|词云展示|默认值为不生成<br>使用此参数，设定词云展示的关键词，所有文件名包含有此关键词的 MarkDown 文件都会被统计|

- 词云展示
- 为了展示出中文词云，需要在根目录下添加 myfont.ttf，作为生成词云时使用的字体
- 为了更好地生成词云，在"mydict"文件（使用任意文本编辑器打开均可）文件里添加需要区分开的词语
-->

### 强制重构目录

`python scripts/work_record.py`

强制重构系统目录，包含自动生成html与自动隐藏已完成作品

## 把现有文档变为 MarkDown 文件

`python scripts/doc_format.py`

支持.doc、.docx、.txt，把其中的文本放置到同名的 MarkDown 文件中

对所有目录递推变更

| 参数 | 效果                                                 |
| :--- | :--------------------------------------------------- |
| -r   | 使用此参数，则在生成 MarkDown 文件后会把原始文件删除 |

## 搜索文件内容

`python scripts/search_for_key.py [关键词]`

会在所有 MarkDown 中搜索给定的关键词，在终端打印出结果

## 校正换行符

`python scripts/work_format.py`

从根目录起，把.txt 和.md 文件中的行尾符纠正为对应操作系统的；段首尾空白字符去除

把.py 文件的行尾符纠正为对应操作系统的

## 翻译名词

`python scripts/name_translate.py [filename]`

按预设的翻译方向翻译文本

|选项参数|效果|
|:-|:-|
|all|翻译所有文件|
|（文件夹）|翻译指定文件夹的所有文件|
|（关键词）|翻译标题含有关键词的文件|

## 格式化单个文档并统计字数

`python scripts/file_check.py [keyword] <option>`

找到所有文件名含有关键词的文件，翻译名词（可选），统计字数，并生成html文件

|选项参数|效果|
|:-|:-|
|（无）|根据预设中的翻译方法翻译名字|
|-t|根据预设中的正向翻译方向翻译名词|
|-b|反向翻译|
|-n|不进行名词翻译|

根据 MarkDown 的各级标题，把文件切分为若干部分，统计每一部分的字数，并在终端打印出结果

若输入纯文本文件，则只打印全文件的字数

## 随机姓氏

`python scripts/family_name.py`

生成一个随机中文姓氏

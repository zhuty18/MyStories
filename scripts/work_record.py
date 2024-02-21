# coding = utf-8

"""文件记录"""

import os
import sys
import re
import subprocess
from utils import (
    dirs,
    format_time,
    format_log_time,
    get_time,
    dir_name,
    file_length,
    file_fin,
    short_path,
)
import file_check
from personal import DEFAULT_ORDER
import web_make

try:
    from xpinyin import Pinyin
except ModuleNotFoundError:
    print("请安装xpinyin模块！")
    sys.exit()

stat_files = []


class FileRecord:
    """文件记录"""

    def __init__(self, name, length, time, fin):
        self.name = name
        self.length = length
        self.time = time
        self.fin = fin

    def update(self, length=None, fin=None):
        """更新文件信息"""
        self.length = length
        self.fin = fin
        self.time = format_time()

    def __str__(self) -> str:
        return f"{self.name}\t{self.length}\t{self.time}\t{self.fin}"

    def info(self):
        """信息条目"""
        return f"|[{self.name}]({self.name}.md)|{self.length}|{self.time}|"

    @staticmethod
    def from_readme(readme: str):
        """从readme中的信息条目读取"""
        t = readme.strip().split("\t")
        return FileRecord(t[0], int(t[1]), t[2], t[3] == "True")

    @staticmethod
    def from_path(name, path):
        """根据路径生成"""
        full_path = os.path.join(path, name)
        pipe = subprocess.Popen(["git", "log", full_path], stdout=subprocess.PIPE)
        output, _ = pipe.communicate()
        output = output.decode("utf8")
        commit = None
        for i in output.split("\n"):
            if i.startswith("Date:"):
                commit = i
                break
        if commit is not None:
            t = re.findall(re.compile(r"Date:\s*(.*?)\s*\+", re.S), commit)[0].strip()
            time_formatted = format_log_time(t)
        else:
            time_formatted = format_time()
        return FileRecord(name[0:-3], file_length(full_path), time_formatted, file_fin(full_path))


class WordCounter:
    """字数统计器"""

    def __init__(self):
        self.total_change = 0
        self.read_history()
        self.get_files()
        self.write_result()
        self.fin = []

    def read_history(self):
        """从历史记录中读取已有条目"""
        self.history = {}
        if os.path.exists("data/history.txt"):
            with open("data/history.txt", "r", encoding="utf-8") as f:
                for i in f.readlines():
                    t = FileRecord.from_readme(i)
                    self.history[t.name] = t

    def get_files(self):
        """读取变更的文件目录"""
        self.changes = []
        os.environ["PYTHONIOENCODING"] = "utf8"
        with subprocess.Popen(["git", "status", "-s"], stdout=subprocess.PIPE) as pipe:
            output = pipe.communicate()[0]
        output = output.decode("utf8")
        for i in output.split("\n"):
            try:
                i = i.split(" ")[2]
            except IndexError:
                pass
            if not "README" in i and i.endswith(".md") and "/" in i:
                if os.path.exists(i):
                    self.changes.append(i)
                    file_check.count_file(i)

    def write_result(self):
        """写入统计结果"""
        log = []
        for i in self.changes:
            name = re.findall(re.compile(r".*/(.*).md$", re.S), i)[0]
            try:
                length_new = file_length(i)
                try:
                    length_old = self.history[name].length
                except KeyError:
                    length_old = 0
                log.append(f"|[{name}]({i})|{length_old}|{length_new}|{length_new-length_old}|")
                self.total_change += length_new - length_old
                try:
                    self.history[name].update(length=length_new, fin=file_fin(i))
                except KeyError:
                    self.history[name] = FileRecord(name, length_new, format_time(), file_fin(i))
            except FileNotFoundError:
                self.history.pop(name)
                self.total_change -= self.history[name].length

        with open(os.getcwd() + "/README.md", "w", encoding="utf-8") as f:
            with open("data/README-template.md", "r", encoding="utf-8") as f1:
                log_str = ""
                if log:
                    log_str += "# files changed at last commit\n\n"
                    log_str += "|文件名|上次提交时字数|本次提交字数|字数变化|\n"
                    log_str += "|:-|:-|:-|:-|\n"
                    log += "\n".join(log)
                    log_str += "\n"
                log_str += "\n"
                log_str += dirs().strip()
                f.write(f1.read().replace("<archive info>", log_str))

    def update_history(self):
        """更新历史数据"""
        with open("data/history.txt", "w", encoding="utf-8") as f:
            for _, value in self.history.items():
                f.write(f"{value}\n")


class IndexBuilder:
    """索引目录建立器"""

    def __init__(self, path, counter: WordCounter, order):
        has_md = False
        for i in os.listdir(path):
            if i.endswith(".md"):
                has_md = True
                break
        if has_md:
            self.tbc = []
            self.fin = []
            self.build_index(path, counter)
            self.sort_index(self.tbc, order)
            self.sort_index(self.fin, order)
            self.write_index(path, counter)

    def get_info(self, info):
        """获得记录"""
        t = info.split("|")
        name = re.findall(re.compile(r"\[(.*?)\]", re.S), t[1])[0]
        return name, t[3]

    def build_index(self, path, counter: WordCounter):
        """建立索引"""
        for i in os.listdir(path):
            if i.endswith(".md") and not i.startswith("README"):
                if not i[0:-3] in counter.history.keys():
                    counter.history[i[0:-3]] = FileRecord.from_path(i, path)
                t = counter.history[i[0:-3]]
                if t.fin:
                    self.fin.append(t)
                else:
                    self.tbc.append(t)

    def sort_index(self, l: list, order):
        """索引排序"""
        pin = Pinyin()
        l.sort(key=lambda x: pin.get_pinyin(x.name))
        if order == "time":
            l.sort(key=lambda x: get_time(x.time), reverse=True)

    def write_index(self, path, counter):
        """写入索引"""
        if len(self.tbc) + len(self.fin) > 0:
            with open(path + "/README.md", "w", encoding="utf-8") as f:
                f.write("# Word Stat Result\n\n")
                title = "|名称|字数|修改时间|\n"
                title += "|:-|:-|:-|\n"
                if len(self.tbc) > 0:
                    f.write("## To Be Continued\n\n")
                    f.write(title)
                    for i in self.tbc:
                        f.write(i.info() + "\n")
                if len(self.fin) > 0:
                    f.write("\n## Finished\n\n")
                    f.write(title)
                    for i in self.fin:
                        f.write(i.info() + "\n")
                        counter.fin.append(f"{short_path(path)}/{i.name}.md")


def update_index(counter, path, order, force=False):
    """更新索引"""
    for i in os.listdir(path):
        subdir = os.path.join(path, i)
        if os.path.isdir(subdir) and not i.startswith("."):
            change = False
            for j in counter.changes:
                if short_path(subdir) in j:
                    change = True
                    break
            if change or force:
                update_index(counter, subdir, order, force)
    if path != os.getcwd() and dir_name(path):
        IndexBuilder(path, counter, order)


if __name__ == "__main__":
    wcr = WordCounter()
    update_index(wcr, os.getcwd(), DEFAULT_ORDER, True)
    wcr.update_history()
    web_make.all_html(force=True)
    web_make.auto_hide(wcr.fin, True)
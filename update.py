# coding = utf-8

"""
提交至git
"""

import os
import time
import argparse
import sys

if __name__ == "__main__":
    sys.path.append("./scripts")

    from personal import (
        GIT_ADD,
        GIT_COMMIT,
        GIT_PUSH,
        COUNT_WORD,
        WORD_CLOUD_TYPE,
        WORD_CLOUD_JOB,
        DEFAULT_MESSAGE,
        DEFAULT_ORDER,
        ALT_ORDER,
        GENERATE_WEB,
        GIT_NAME,
        GIT_EMAIL,
        GIT_WEB,
        CHANGE_SAVE,
        FILE_ROOT,
        POST_CHANGE,
    )

    COMMIT_TIME = time.time()
    FILE_DIR = os.path.join(os.getcwd(), FILE_ROOT)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--autocommit",
        type=bool,
        default=GIT_COMMIT,
        nargs="?",
        const=not GIT_COMMIT,
    )
    parser.add_argument("-m", "--message", default=DEFAULT_MESSAGE)
    parser.add_argument(
        "-s",
        "--statistic",
        type=bool,
        default=COUNT_WORD,
        nargs="?",
        const=not COUNT_WORD,
    )
    parser.add_argument(
        "-word", "--word_cloud", type=str, default=WORD_CLOUD_TYPE
    )
    parser.add_argument(
        "-o",
        "--sort_order",
        type=str,
        default=DEFAULT_ORDER,
        nargs="?",
        const=ALT_ORDER,
    )
    parser.add_argument(
        "-push",
        "--push",
        type=bool,
        default=GIT_PUSH,
        nargs="?",
        const=not GIT_PUSH,
    )
    parser.add_argument(
        "-page",
        "--pages",
        type=bool,
        default=GENERATE_WEB,
        nargs="?",
        const=not GENERATE_WEB,
    )
    parser.add_argument(
        "-a", "--add", type=bool, default=GIT_ADD, nargs="?", const=not GIT_ADD
    )
    parser.add_argument(
        "-w", "--web", type=bool, default=GIT_WEB, nargs="?", const=not GIT_WEB
    )
    parser.add_argument(
        "-post",
        "--post",
        type=bool,
        default=POST_CHANGE,
        nargs="?",
        const=not POST_CHANGE,
    )
    args = parser.parse_args()

    # 格式化所有文档
    import work_format

    work_format.format_all(FILE_DIR)

    # 字数统计
    if args.statistic:
        import work_record

        counter = work_record.WordCounter()
        counter.run()
        work_record.update_index(counter, FILE_DIR, args.sort_order)
        counter.update_history()
        counter.save_change(CHANGE_SAVE)
        from utils import auto_hide

        auto_hide()
    if args.post:
        import post

        post.post_change(counter)

    # 构建网页
    if args.pages:
        import web_make

        web_make.all_html(args.web)

    # 提交文件
    if args.autocommit:
        if args.add:
            os.system("git add .")
        os.system(f"git config user.name {GIT_NAME}")
        os.system(f"git config user.email {GIT_EMAIL}")

        # mes = format_time() + " "
        mes = args.message
        try:
            mes += " 更新了" + str(counter.total_change) + "字"
        except NameError:
            pass
        mes = 'git commit -m "' + mes + '"'
        os.system(mes)

        if args.push:
            os.popen("git pull").close()
            os.popen("git push").close()

    if args.word_cloud != "none":
        import word_cloud_make

        word_cloud_make.WordPic(
            path=FILE_DIR, job=WORD_CLOUD_JOB, file=[args.word_cloud]
        )

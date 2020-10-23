python3 stat.py > commit.log
git add .
git commit -m "$(date "+%m.%d %H:%M") update"
git push
code commit.log
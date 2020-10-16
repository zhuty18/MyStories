echo -m "%date:~3,2%%date:~6,2% %time:~0,2%%time:~3,2% update"
python stat.py
git add .
git commit -m "%date:~3,2%%date:~6,2% %time:~0,2%%time:~3,2% update"
git push
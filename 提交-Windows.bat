python stat.py
git add .
set h=%time:~0,2%%time:~3,2%
set h=%h: =0%
git commit -m "%date:~3,2%.%date:~6,2% %h% update"
git push
call cmd
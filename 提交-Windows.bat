python stat.py
git add .
set h=%time:~0,2%:%time:~3,2%
git commit -m "%date:~3,2%.%date:~6,2% %h: =0% update"
git push
call cmd

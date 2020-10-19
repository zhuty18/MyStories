python stat.py
git add .
set h=%time:~0,5%
git commit -m "%date:~3,2%.%date:~6,2% %h: =0% update"
git push

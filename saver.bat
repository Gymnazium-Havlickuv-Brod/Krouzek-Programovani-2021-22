REM Made by ostSTRUPpen
CLS
@ECHO off
TITLE saving
ECHO Jak chcete pojmenovat zmenu?
SET /p change=""
TITLE saving
git add .
git commit -m "%change%"
git push -u origin main
TITLE saved
PAUSE
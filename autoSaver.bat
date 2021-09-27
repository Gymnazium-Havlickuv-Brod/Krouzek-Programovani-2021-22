REM Made by ostSTRUPpen
@ECHO off
CLS
TITLE saver

REM K spuštění při startu je nuné provést několik kroků:
REM Vytvoř si zástupce pro každý autoSaver.bat
REM Pro spuštění pro každého uživatele:
REM 	Windows+R a napiš: "shell:common startup" nebo v průkumníku: "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"
REM Pro spuštění jen pro tebe:
REM 	Windows+R a napiš: "shell:startup" nebo v průkumníku: "C:\Users\%JménoUživatele%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
REM A přesuň do dané složky zástupce pro každý autoSaver.bat

git add .
git commit -m "AUTO_SAVE_%date%"
git push -u origin main

TITLE saved
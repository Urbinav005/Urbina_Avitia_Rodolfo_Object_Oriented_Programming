@echo off
cd /d "%~dp0"
py -m pip install -r requirements.txt || python -m pip install -r requirements.txt
echo.
echo Listo. Ya puedes ejecutar: py main.py
pause

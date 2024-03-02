@echo off
echo Making EXE File
pyinstaller .\wsh.py --noconfirm
echo If you dont want to cleanup, press Ctrl+C now.
pause
copy .\dist\*.* .
rd /s /q .\dist
rd /s /q .\build
del /f /q .\*.spec
echo Finished
pause
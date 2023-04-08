@echo off
rmdir /s /q %USERPROFILE%\Documents\PyTest > nul 2>&1
mkdir %USERPROFILE%\Documents\PyTest > nul 2>&1
copy main.py %USERPROFILE%\Documents\PyTest > nul 2>&1
C: 
cd %USERPROFILE%\Documents\PyTest > nul 2>&1
python main.py
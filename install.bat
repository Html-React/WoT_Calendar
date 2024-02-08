@echo off
python.exe -m venv .venv
call .\.venv\Scripts\activate.bat
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
echo @echo off > wot.bat
echo call .\.venv\Scripts\activate.bat >> wot.bat
echo python run.py >> wot.bat
echo Set WshShell = CreateObject("WScript.Shell") > wot.vbs
echo WshShell.Run "cmd.exe /c %~dp0wot.bat", 0, false >> wot.vbs
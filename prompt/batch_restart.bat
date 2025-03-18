@echo off

echo System will restart in 5 minutes. Please save your work.
echo Restarting PC? (Y/N)
choice /c yn /d y /t 600
if %errorlevel%==2 (
    echo Timeout. Restarting PC...
    shutdown /r /t 600
)



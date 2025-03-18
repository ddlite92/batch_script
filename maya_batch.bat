@echo.
@timeout 5
@pause
"C:\Program Files\Autodesk\Maya2023\bin\Render.exe" -rd "C:/Users/MON177/Desktop/SH001e/images/Sett_ref" -cam "SH05" -s 101 -e 105 -rl BG -skipExistingFrames 1 -x 1024 -y 2048 -r redshift "V:/PAPA/Work/Render/Benchmark/REEL_01/16. FLASHBACK - INT. POWER STATION - DAY/PAPA_Chapter_01_016_sh025/PAPA_Chapter_01_016_sh025_RENDER.ma"
@echo Restarting PC ...
shutdown /r /t 0


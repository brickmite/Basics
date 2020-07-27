@ECHO OFF

REM path to application
echo "Starting GDSPLOT"
START C:\WCAD\Gdsplot\gdsplt.exe

REM Time (in seconds) before killing the app
echo "Killing GDSPLOT in 6 minutes"
timeout /t 360 /nobreak
taskkill /f /im gds*



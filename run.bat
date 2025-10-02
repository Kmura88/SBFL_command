@echo off
cd /d %~dp0

rem %1 実行するjavaのmain関数があるクラス

set CLASS_NAME=%1

if "%CLASS_NAME%"=="" (
	echo [error] usage : run.bat class
	exit /b
)

java -javaagent:lib/jacocoagent.jar=destfile=jacoco.exec -cp classes %CLASS_NAME% 

java -jar lib/jacococli.jar report jacoco.exec --classfiles classes --sourcefiles src --xml Report.xml

python ./lib/command.py
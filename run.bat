@echo off
cd /d %~dp0

set CLASS_NAME=%1
set TMP_FOLDER=.SBFL_data

rem 構文チェック
if "%CLASS_NAME%"=="" (
	echo [error] usage : run.bat class
	exit /b
)

rem 一時フォルダが既にあれば削除 
if exist "%TMP_FOLDER%" (
	rd /s /q %TMP_FOLDER%
)

rem 一時フォルダの作成
mkdir %TMP_FOLDER%
attrib +h %TMP_FOLDER%

rem .execの生成
java -javaagent:lib/jacocoagent.jar=destfile=%TMP_FOLDER%/jacoco.exec,append=false -cp classes %CLASS_NAME%

rem .xmlの生成
java -jar lib/jacococli.jar report %TMP_FOLDER%/jacoco.exec --classfiles classes --sourcefiles src --xml %TMP_FOLDER%/report.xml

rem .xmlデータの読み込み
python ./lib/XmlAnalyzer.py %TMP_FOLDER%/report.xml

rem rd /s /q %TMP_FOLDER% 

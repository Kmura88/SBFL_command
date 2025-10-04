@echo off

rem クラス名、メソッド名を受け取り.xmlファイルを生成する。

set CLASS_NAME=%1
set METHOD_NAME=%2

if "%METHOD_NAME%"=="" (
	echo [Error] usage : %0 CLASS_NAME METHOD_NAME
	exit /b
)

rem 環境変数の読み込み
call config.cmd

rem .execの生成
java -javaagent:lib/jacoco/jacocoagent.jar=destfile=%TMP_FOLDER%/jacoco.exec,append=false -cp "lib/junit/junit-4.13.2.jar;lib/junit/hamcrest-core-1.3.jar;classes" RunSingleTest %CLASS_NAME% %METHOD_NAME%

rem .xmlの生成 テストが成功したか否かで分岐
if %ERRORLEVEL% == 0 (
	java -jar lib/jacoco/jacococli.jar report %TMP_FOLDER%/jacoco.exec --classfiles classes --sourcefiles src --xml %TMP_FOLDER%/pass_test/%CLASS_NAME%.%METHOD_NAME%.xml
	rem python ./lib/XmlAnalyzer.py %TMP_FOLDER%/pass_test/%CLASS_NAME%.%METHOD_NAME%.xml
) else (
	java -jar lib/jacoco/jacococli.jar report %TMP_FOLDER%/jacoco.exec --classfiles classes --sourcefiles src --xml %TMP_FOLDER%/fail_test/%CLASS_NAME%.%METHOD_NAME%.xml
	rem python ./lib/XmlAnalyzer.py %TMP_FOLDER%/fail_test/%CLASS_NAME%.%METHOD_NAME%.xml
)
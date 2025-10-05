@echo off
cd /d %~dp0

call lib\config.cmd

set CLASS_NAME=%1

rem 構文チェック
if "%CLASS_NAME%"=="" (
	echo [Error] usage : %0 CLASS_NAME
	exit /b 1
)

rem 一時フォルダが既にあれば一旦削除 
if exist "%TMP_FOLDER%" (
	rd /s /q %TMP_FOLDER%
)

rem classesフォルダが有るか
if not exist "classes" (
	echo [Error] classes Folder not found.
	exit /b 1
)

rem srcフォルダが有るか
if not exist "src" (
	echo [Error] src Folder not found.
	exit /b 1
)

rem 一時フォルダの作成
mkdir %TMP_FOLDER%
attrib +h %TMP_FOLDER%

rem 成功テスト・失敗テストの格納場所
mkdir %TMP_FOLDER%\pass_test
mkdir %TMP_FOLDER%\fail_test

rem MethodParserAndRunnerの実行
java -cp "lib/junit/junit-4.13.2.jar;lib/junit/hamcrest-core-1.3.jar;classes" MethodParserAndRunner %CLASS_NAME%

rem suspeciousの計算 cdを一度libへ変更する。
cd lib
python SBFL_Ochiai.py

rem cdを戻す
cd ..

exit /b 0
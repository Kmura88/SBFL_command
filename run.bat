rem %1 実行するjavaのmain関数があるクラス

@echo off
cd /d %~dp0

java -javaagent:lib/jacocoagent.jar=destfile=jacoco.exec -cp classes %1

java -jar lib/jacococli.jar report jacoco.exec --classfiles classes --sourcefiles src --xml Report.xml

python ./lib/command.py
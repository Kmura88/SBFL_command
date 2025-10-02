@echo off
cd /d %~dp0

java -jar lib/jacococli.jar report jacoco.exec --classfiles classes --sourcefiles src --xml Report.xml

python command.py
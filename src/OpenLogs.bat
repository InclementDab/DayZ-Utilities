@echo off
TITLE Log Viewer
color 0A
SETLOCAL EnableDelayedExpansion


REM ////SET THESE FILES////
set "NPPDirectory=C:\Program Files (x86)\Notepad++\"
set "ProfileDirectory=P:\profiles\Client\"
REM ///////////////////////

set "LatestFile="
set "SecondLatestFile="

for /F "delims=|" %%I in ('dir %ProfileDirectory%\*.log /B /O:D') do ( 
	set SecondLatestFile=!LatestFile!
	set LatestFile=%%I
)

CD /D %NPP_Directory%
notepad++ %ProfileDirectory%\%LatestFile%
notepad++ %ProfileDirectory%\%SecondLatestFile%

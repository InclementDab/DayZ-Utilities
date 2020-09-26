@echo off

setlocal enableextensions enabledelayedexpansion

set PREFIX=DayZ
set ROOT_DIR=P:\scripts

set list=1_Core 2_GameLib 3_Game 4_World 5_Mission editor\Workbench editor\plugins
for %%a in (%list%) do (
	set directory=!ROOT_DIR!\%%a
	mkdir !directory!\%PREFIX%
	for /f "tokens=*" %%D in ('dir /b "!directory!"') do (
		set found=%%~D
		if "!found!"=="%PREFIX%" (
			echo Skipping: !directory!\!found!
		) else (
			echo Processing: !directory!\!found!
			move !directory!\!found! !directory!\%PREFIX% > NUL
		)
	)
)

endlocal
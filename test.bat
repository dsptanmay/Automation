@echo off
local.py > Output
set /P MYVAR=<Output
ECHO %MYVAR%
PAUSE
DEL Output
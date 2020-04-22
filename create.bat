@ECHO off
SET default_path=%CD%
SET /p gpath="Enter the path to which your projects folder is located: "
CD /d "%gpath%"
SET /p f1="Enter the name of the project folder: "
mkdir %f1%
CD %f1%
ECHO %CD%
ECHO.>README.md
git init
ECHO Empty Repository Initialized
ECHO Running Local.py to create repository
python "%default_path%\local.py" %f1% > Output
ECHO Wait for the repository to be created and then press any key to continue!
PAUSE
SET /P MYVAR=<Output
ECHO Repository created!
git remote add origin %MYVAR%
ECHO Remote Added!
git add README.md
git commit -m "initial commit"
ECHO Initial Commit made
git push -u origin master
ECHO First commit pushed to master branch
code .
ECHO Code file opened
ECHO Press any button to close 
PAUSE
DEL Output
exit
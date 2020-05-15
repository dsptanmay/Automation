@ECHO off
SET default_path=%CD%
set /P email="Enter your email address: "
set /P passwd="Enter your password: "   
SET /p gpath="Enter the path to which your projects folder is located: "
CD /d "%gpath%"
SET /p f1="Enter the name of the project folder: "
MKDIR %f1%
CD %f1%
ECHO %CD%
ECHO.>README.md
git init
ECHO Running Local.py to create repository
python "%default_path%\local.py" %f1% %email% %passwd% > Output
ECHO Wait for the repository to be created and then press any key to continue!
PAUSE
SET /P MYVAR=<Output
ECHO Repository created !
git remote add origin %MYVAR%
ECHO Remote Added!
git add README.md
git commit -m "initial commit"
ECHO Initial Commit made
git push -u origin master
ECHO First commit pushed to master branch
DEL Output
PAUSE
ECHO Opening Code window
code .

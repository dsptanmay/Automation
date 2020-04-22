@echo off
set default_path=%cd%
set /p gpath="Enter the path to which your projects folder is located: "
cd /d "%gpath%"
set /p f1="Enter the name of the project folder: "
mkdir %f1%
cd %f1%
echo %cd%
echo.>README.md
git init
echo Empty Repository Initialized
echo Running Local.py to create repository
python "%default_path%\local.py" %f1%
echo Wait for the repository to be created and then press any key to continue!
pause
echo Repository created!
git remote add origin https://github.com/dsptanmay/%f1%.git
echo Remote Added!
git add README.md
git commit -m 'initial commit'
echo Initial Commit made
git push -u origin master
echo First commit pushed to master branch
code .
echo Code file opened
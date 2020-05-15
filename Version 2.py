from github import Github
import os
from os import path
import subprocess as sp

sp.run('pip install --upgrade PyGithub', shell=True)


def repoCreation(folderName):
    userName = str(input("Enter your Github Username: "))
    passwd = str(input('Enter your password: '))
    g = Github(userName, passwd)
    user = g.get_user()
    login = user.login  # Gives username to be put in remote link
    repo = user.create_repo(folderName)
    print('Repository successfully created!')
    commands = [f'echo __{repo.name}__ >> README.md',
                'echo README File succesfully created!',
                'git init',
                f'git remote add origin https://github.com/{login}/{folderName}.git',
                'echo Remote successfully added!',
                'git add .',
                'git commit -m "Initial Commit"',
                'git push -u origin master',
                'echo Opening Code Window',
                'code .'
                ]
    for c in commands:
        os.system(c)
    print('First commit made with push')


def folderCreation():
    while True:
        mainPath = str(
            input("Enter the path where the project wil be stored: "))
        mainPath = path.normpath(mainPath)
        if path.exists(mainPath) is True:
            print("Path Exists!")
            os.chdir(mainPath)
            break
        else:
            print('Invalid Path\nTry again!')
    while True:
        projectName = str(
            input('Enter the name of the project: ')).capitalize()
        newPath = path.join(mainPath, projectName)
        if path.exists(newPath) is True:
            print('Folder already exists!\nChoose another name!')
        else:
            break
    os.mkdir(projectName)
    print(f'{projectName} folder created locally')
    curPath = os.chdir(projectName)
    print(f'Current Path:{os.getcwd()}')
    repoCreation(projectName)


folderCreation()

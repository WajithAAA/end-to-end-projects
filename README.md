# End-to-end ml projects steps

- create local project directory
- open anaconda prompt and type `code .` to open the vscode project
- create new virtual env `conda create -p venv python==3.8 -y`
- activate virtual environment `conda activate venv/`

- create new git repository
- connect to new git repository with local project
    - `git init`
    - `git add README.md`
    - `git commit -m "first commit"`
    - `git status`
    - `git branch -M main`
    - `git remote -v`
    - `git push -u origin main`

- add change in git repository to local repository
    - `git pull`
- add changes in local repository to existing git repository
    - `git add .`
    - `git commit -m "second commit"`
    - `git push -u origin main`

- create git ignore file in `.gitignore` in git repository

- create setup.py file and requirements.txt 
    - install requirements.txt `pip install -r requirements.txt`

- create components and pipelines directory in src directory
- update logger and exception handler files





## Prerequisites

- Python 3.10, if your operating system doesn't have this version in the repo, you can use [Pyenv](https://github.com/pyenv/pyenv) to install it.
- You need to have [Poetry](https://python-poetry.org/docs/master/) installed, please notice that we are using the master branch because some functions depend on the latest beta version of Poetry.

## Get started

- Install `pyenv` in you machine \
   eg: `sudo apt install pyenv`
- Run `cd` to this project folder
- Run `pyenv install 3.10.5`
- After installed, Run `pyenv local 3.10.5` and later a file named `.pyton-version` \
  is created in the project folder.
- Next create virtualenv for the project by running `poetry env use 3.10.5`. \
  this will activate local environment shell for your project. Make sure you did not skip the steps.
- install dependencies by running `poetry lock --no-update && poetry install --with=dev,test`. \
  This action will install all dependencies you need to run the project.


## View commands

We have compiled all the commands to get started for you to get on board. To list all the commands, simply type this in your terminal:

## 1. `doit` command center
- all command wrapped in `command.py`

```
doit
```
## see available command
```
doit list
```

## run Command
- task name is in base or in def task_<task_name>
```
doit taskname
```
### zsh
### zsh completion scripts should be placed in a folder in the “autoload” path.
```
# add folder with completion scripts
fpath=(~/.zsh/tabcompletion $fpath)
cp _doit ~/.zsh/tabcompletion/_doit
```
```
# Use modern completion system
autoload -Uz compinit
compinit
```
###  Run `Unit Test`

To run unit tests, use `pytest -s` command as show below

```
pytest -s
```

## ADDITIONAL INFO:

Kindly check below link to get yourself comfortable with the project. Here we mentioned somes, feel free to go from the first list (Do not skip or jump it), so you will have a smooth experience with onboarding process to the project.

### 1. How `Django` Works

- [Django introduction](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction)

### 2. How `DBRouters` Works

- [Multiple databases](https://docs.djangoproject.com/en/4.1/topics/db/multi-db/)

### 3. How `Django Settings` Works

- [Django Settings](https://docs.djangoproject.com/en/4.1/topics/settings/)

### 4. How `Admin Page` Works

- [Django Admin](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/)

### 5. How `Pytest` and `fixture` Works

- [Pytest Django](https://pytest-django.readthedocs.io/en/latest/)
- [Fixture Pytest](https://pytest-django.readthedocs.io/en/latest/database.html#advanced-database-configuration)

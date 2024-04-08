# Study and Dev notes For Python and Django

## Django

1. Config and set a virtual environment

```python
pip3 install pipenv
```

2. Install django in a virtual environment
   Inside the project folder

```python
pipenv install django
```

The location for the virtual environment will be reflected in the installation
Inside there will be a bin file with all dependencies installed
Also there will be a Pipefile which is the project package management config file (like package.lock with npm or yarn.lock with yarn)

3. Use a Python interpreter that belongs to the virtual environment and not the global one. Activate the virtual environment

```python
# (this is the old virtualenv/project-folder/bin/activate)
pipenv shell
```

4. Use django-admin to create a new project

```python
# (this is the old django-admin.py startproject projectname)
django-admin startproject projectname
```

to avoid folder redundancy add a period to the command so that the current folder is taken as the main folder

```python
django-admin startproject projectname .
```

5. From this point on, instead of using django-admin utility, we will use manage.py which is a command-line utitlity wraper around django-admin but takes the project config into account

to check which commands they provide, access by typing

```python
django-admin
# or
python3 manage.py
```

6. Start the server

```python
python3 manage.py runserver
# or
python3 manage.py runserver portnumber
```

6. Set the integrated VScode terminal to work with the virtualenv proper interpreter

6.1. locate the path to the virtual environment interpreter
This is shown when the virtual environment is being created. Would be something like:
/[user]/.local/share/virtualenvs/folder-name-plus-some-characters

```python
pipenv --venv
```

6.2 In VSCode command palette search for Python interpreter and use the path there and append /bin/python at the end
Check it in .vscode settings.json
restart the terminal window in VSCode and the virtual environment terminal with the interpreter will be automatically activated

7. Running the development server

```python
# from the container project folder
python manage.py runserver #or
python3 manage.py runserver
```

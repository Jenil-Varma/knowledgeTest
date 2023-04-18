## knowledgeTest

KnowledgeTest is a web application for creating and taking quizzes. This project is built using the Django web framework.

## Features
- User registration and authentication
- Creating, updating and deleting quizzes
- Topic selection
- Taking a quiz, viewing results
- Viewing quiz taken history

## Structure/Organization

    ├── Django/
    │   ├─ accounts/
    │   │  ├─ migrations/
    │   │  │  ├─ __init__.py
    │   │  ├─ static/
    │   │  │  ├─ css/
    │   │  │  │  ├─ login.css
    │   │  │  │  ├─ signup.css
    │   │  ├─ __init__.py
    │   │  ├─ admin.py
    │   │  ├─ apps.py
    │   │  ├─ models.py
    │   │  ├─ tests.py
    │   │  ├─ urls.py
    │   │  ├─ views.py
    │   ├─ Django/
    │   │  ├─ __init__.py
    │   │  ├─ asgi.py
    │   │  ├─ settings.py
    │   │  ├─ urls.py
    │   │  ├─ views.py
    │   │  ├─ wsgi.py
    │   ├─ quiz/
    │   │  ├─ migrations/
    │   │  │  ├─ __init__.py
    │   │  ├─ static/
    │   │  │  ├─ css/
    │   │  │  │  ├─ index.css
    │   │  │  │  ├─ quiz-results.css
    │   │  │  │  ├─ select-topic.css
    │   │  │  │  ├─ take-a-quiz.css
    │   │  ├─ templates/
    │   │  ├─ __init__.py
    │   │  ├─ admin.py
    │   │  ├─ apps.py
    │   │  ├─ models.py
    │   │  ├─ urls.py
    │   │  ├─ views.py
    │   │  ├─ tests.py
    │   ├─ templates/
    │   │  ├─ account/
    │   │  │  ├─ login.html
    │   │  │  ├─ profile.html
    │   │  │  ├─ signup.html
    │   │  ├─ quiz/
    │   │  │  ├─ index.html
    │   │  │  ├─ results.html
    │   │  │  ├─ select-topic.html
    │   │  │  ├─ take-a-quiz.html
    │   │  ├─ error.html
    │   │  ├─ base.html
    ├────── .gitignore
    ├────── db.sqlite3 
    └────── manage.py

## Database diagram
![dbDiagram.png](images%2FdbDiagram.png)

## Getting Started
To get started with the project, follow these steps:

**Setup python interpreter**
- Go to File => Settings => Project: KnowledgeTest => Python Interpreter.
Select Add Interpreter => Add Local Interpreter
![interpretersetting.png](images%2Finterpretersetting.png)

- Keep all default settings then click OK
![interpretersetting2.png](images%2Finterpretersetting2.png)
![interpretersetting3.png](images%2Finterpretersetting3.png)


**Edit Configurations**
- Run => Edit Configurations
![editConfig1.png](images%2FeditConfig1.png)
- Config parameters<br>
Script path: select manage.py file <br>
Parameters: runserver
![editConfig2.png](images%2FeditConfig2.png)

**Start the project**
![startProject.png](images%2FstartProject.png)

## Common issues
**Cannot start the project - Django hasn't installed**
- Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?
![issue1.png](images%2Fissue1.png)
- Causes: Django hasn't installed
- Solution: <br>
Install Django for the project <br>
Open terminal: <br>
```cmd
Set-ExecutionPolicy Unrestricted -Scope Process
venv\Scripts\activate.ps1
 ```
![issue2.png](images%2Fissue2.png)

Install Django
```cmd
pip install django
 ```
![issue3.png](images%2Fissue3.png)

Start the project
![startProject.png](images%2FstartProject.png)
![startSuccess.png](images%2FstartSuccess.png)
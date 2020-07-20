# Django

## Installation

This will install Django on your machine.

```bash
    pip install django
```

## Initialize a django project

Create your repository folder then run:

```bash
    django-admin startproject myproject
```

## Project structure

1. manage.py: Runs commands for the project
2. [projectname]/__init__.py: Tells python that the folder contains python code (also called dunder init)
3. [projectname]/wsgi.py | asgi.py: Provides hooks for webservers such as Apache, Nginx, etc
4. [projectname]/settings.py: Configures the Django project
5. [projectname]/urls.py: Routes web requests based on URL

## To run the project

Navigate to your project path where manage.py exists, then run:

```bash
    python manage.py runserver
```

This command will also create a SqLite database for your project.

## What is a Django app

- A component in a Django project
- Each app fits a specific purpose e.g. Blog, Forum, Wiki etc
- A folder with a set of python files

To create an app in your Django project, navigate to your project folder then run where your manage.py is:

```bash
    python manage.py startapp myapp
```

Add your app name in settings.py in your main project folder.

App's folder structure

File/folder | Desc
---------|----------
 apps.py | settings related to the app (rare to use)
 models.py | database schema, queries, etc
 admin.py | administrative tasks
 urls.py | route options
 views.py | end user views
 tests.py | project tests
 migrations/ | db migrations related files

## Django MVC architecture

URL Patterns (routes user's request to its relevant view) **-->** Views uses Models (logics, db communications, etc) **-->** Templates (Response contents)

## Migration Commands

To run migration commands navigate to your main project folder where manage.py is, then run:

```bash
    python manage.py makemigrations # to create a new migration
    python manage.py showmigrations # to see your migrations
    python manage.py migrate # to apply your migrations
    python manage.py migrate <appname> <number> # to move to an specific migration
```

## Admin configuration

Add your model to your admin.py file, then create your super user by running:

```python
    from .models import Pet

    # Register your models here.
    @admin.register(Pet)
    class Admin(admin.ModelAdmin):
        pass
```

```bash
    python3 manage.py createsuperuser
```

## Template Syntax

- {{ variable }} e.g.

  ```html
    <h3>{{ pet.name }}</h3>
  ```

- {% tag %} e.g. for loop
  
  ```html
    {% for pet in pets %}
        <li>{{ pet.name }}</li>
    {% endfor %}
  ```

- {{ variable|filter }} e.g. datetime output formatting
  
  ```html
    <h3>{{ pet.name|capfirst }}</h3>
  ```

- some template tags doesn't have end tags e.g.
  
  ```python
    {% url 'home' %} #output is /
    {% url 'pet_detail' pet.id %} #output /myapp/1/
  ```

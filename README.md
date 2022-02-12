# Python ClI Docker Cookiecutter Template

Template for creating a project based on Python cli, using Docker.

## Project Structure

```
├── {{cookiecutter.project_slug}}
    ├── .pre-commit-config.yaml
    ├── .gitignore
    ├── .dockerignore
    ├── .coveragerc
    ├── README.md
    ├── Makefile
    ├── README.md
    ├── setup.py
    ├── setup.cfg
    ├── {{cookiecutter.project_slug}}
    │   ├── main.py
    │   └── __init__.py
    ├── tests
    │   ├── unit
    │   ├── component
    │   │   │   ├── test_application.main.py
    │   │   └── └── __init__.py
    │   ├── unit
    │   │   │   ├── test_main.py
    │   │   └── └── __init__.py    
    │   └── __init__.py
    └── __init__.py
```

## Creating a project

From the directory you want to create a new project in, run:
```shell
cookiecutter https://github.com/paulaceccon/cookiecutter-templates.git --checkout python-docker
```

## Testing changes
Please test by cutting a new project using [replay](https://cookiecutter.readthedocs.io/en/2.0.2/advanced/replay.html). For example, you can use:

```shell
cookiecutter https://github.com/paulaceccon/cookiecutter-templates.git --checkout python-docker --replay
```
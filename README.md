# Jupyter Notebook Cookiecutter Template

Template for creating a project based on jupyter notebooks.
It includes requirements to run Data Science / Machine Learning scripts.

## Project Structure

```
├── {{cookiecutter.project_slug}}
    ├── .pre-commit-config.yaml
    ├── .gitignore
    ├── README.md
    ├── Makefile
    ├── README.md
    ├── requirements.txt
    ├── setup.cfg
    ├── notebooks
    │   ├── template.ipynb
    └── index.ipynb
```

## Creating a project

From the directory you want to create a new project in, run:
```shell
cookiecutter https://github.com/paulaceccon/cookiecutter-templates.git --checkout notebook
```

## Testing changes
Please test by cutting a new project using [replay](https://cookiecutter.readthedocs.io/en/2.0.2/advanced/replay.html). For example, you can use:

```shell
cookiecutter https://github.com/paulaceccon/cookiecutter-templates.git --checkout notebook --replay
```
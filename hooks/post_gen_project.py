import os


if '{{cookiecutter.environment}}' != 'linux':
    os.remove(os.path.join(os.getcwd(), 'Procfile'))

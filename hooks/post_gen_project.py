import os
import sys



# Remove `Procfile` if OS is not linux
if '{{cookiecutter.environment}}' != 'linux':
    os.remove(os.path.join(os.getcwd(), 'Procfile'))



# Add python version to `runtime.txt`
with open('runtime.txt', 'w') as rt:
    rt.write(f'python-{sys.version.split(" ")[0]}')

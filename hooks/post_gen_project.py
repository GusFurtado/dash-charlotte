import os
import sys
from cookiecutter.utils import rmtree



# Remove `Procfile` if OS is not linux
if '{{cookiecutter.environment}}' != 'linux':
    os.remove(os.path.join(os.getcwd(), 'Procfile'))



# Remove `login` folder if `add_login_page` is `False`
if not {{cookiecutter.add_login_page}}:
    rmtree('pages/login')



# Add python version to `runtime.txt`
with open('runtime.txt', 'w') as rt:
    rt.write(f'python-{sys.version.split(" ")[0]}')

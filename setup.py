from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'dash-charlotte',
  packages = [
    'dash_charlotte',
    'dash_charlotte.components',
    'dash_charlotte.layouts',
    'dash_charlotte.themes',
  ],
  version = '0.2.2',
  license = 'MIT',
  description = 'A package of themes, tools and components for Plotly-Dash web dashboards.',
  long_description = long_description,
  long_description_content_type = 'text/markdown', 
  author = 'Gustavo Furtado',
  author_email = 'gustavofurtado2@gmail.com',
  url = 'https://github.com/GusFurtado/dash-charlotte',
  download_url = 'https://github.com/GusFurtado/dash-charlotte/archive/0.2.2.tar.gz',

  keywords = [
    'dashboard',
    'plotly'
  ],

  install_requires = [
    'dash',
    'dash-labs',
    'dash-bootstrap-components'
  ],

  classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Software Development :: User Interfaces',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6'
  ]
)
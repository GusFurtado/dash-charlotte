This cookiecutter contains some components that will kickstart your multipage web dashboard built in [**Dash**](https://dash.plotly.com/).

[**Dash**](https://dash.plotly.com/) is a low-code framework for rapidly building data apps in Python.

## Installation

Make sure you have `cookiecutter` installed on your environment

```
pip install cookiecutter
```

After that, install **Charlotte** using the following command:

```
cookiecutter https://github.com/GusFurtado/dash-charlotte
```

Follow the installation steps and a folder should appear in the selected directory.

Don't forget to install the requirements. The list of dependencies is inside the main folder.

```
pip install -r requirements.txt
```

## Live Demo

- (Temporarily deactivated)

## Submodules

- [`assets`](https://github.com/GusFurtado/dash-charlotte/tree/main/%7B%7Bcookiecutter.app_name%7D%7D/assets): `.css` and `.svg` files;
- [`colors`](https://github.com/GusFurtado/dash-charlotte/tree/main/%7B%7Bcookiecutter.app_name%7D%7D/colors): Color palettes for consistent styling;
- [`components`](https://github.com/GusFurtado/dash-charlotte/tree/main/%7B%7Bcookiecutter.app_name%7D%7D/components): HTML components.
- [`pages`](https://github.com/GusFurtado/dash-charlotte/tree/main/%7B%7Bcookiecutter.app_name%7D%7D/pages): Layouts and callbacks.

## Structure

```
{{app_name}}
  └─ assets
       └─ css
            └─ theme.css
       └─ img
            └─ forbidden_403.svg
            └─ log.svg
            └─ not_found_404.svg
            └─ register.svg
            └─ settings.svg
  └─ colors
       └─ __init__.py
       └─ bootstrap.py
       └─ charlotte_dark.py
       └─ charlotte_light.py
       └─ colorblind.py
       └─ colors.py
       └─ dracula.py
       └─ README.md
  └─ components
       └─ __init__.py
       └─ box.py
       └─ dashboard.py
       └─ drawer.py
       └─ footer.py
       └─ fullscreen_message.py
       └─ navbar.py
       └─ README.md
  └─ data
       └─ errorlog.log
  └─ pages
       └─ login
            └─ login_auth.py
            └─ login_layout.py
            └─ login.py
       └─ page1
            └─ page1.py
       └─ forbidden_403.py
       └─ not_found_404.py
  └─ .gitignore
  └─ app.py
  └─ Procfile
  └─ requierements.txt
  └─ runtime.txt
```

## Deprecated Components Package

**Dash Charlotte** used to be a dash components package before switching to a cookiecutter app.

The old package can still be downloaded [here](https://github.com/GusFurtado/dash-charlotte/releases/tag/0.3.1), but it is deprecated in favor of this cookiecutter.

## License

- [MIT](https://github.com/GusFurtado/dash-charlotte/blob/main/LICENSE)

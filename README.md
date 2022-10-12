# Charlotte

## A Cookiecutter for Dashboards made in Dash

This cookiecutter contains some components that will kickstart your multipage web dashboard built in [**Dash**](https://dash.plotly.com/).

[**Dash**](https://dash.plotly.com/) is a low-code framework for rapidly building data apps in Python.

## Summary

- [Installation](https://github.com/GusFurtado/dash-charlotte#installation)
- [Live Demo](https://dash-charlotte.herokuapp.com/)
- [Submodules](https://github.com/GusFurtado/dash-charlotte#submodelus)
- [Structure](https://github.com/GusFurtado/dash-charlotte#structure)
- [License](LICENSE)

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

- https://dash-charlotte.herokuapp.com/


## Submodules

- [`assets`](assets): `.css` and `.svg` files;
- [`colors`](colors): Color palettes for consistent styling;
- [`components`](components): HTML components.
- [`pages`](pages): Layouts and callbacks.

## Structure

```
{{app_name}}
  └─ assets
       └─ css
            └─ theme.css
       └─ img
            └─ log.svg
            └─ not_found_404.svg
            └─ register.svg
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
       └─ navbar.py
       └─ table.py
       └─ README.md
  └─ pages
       └─ login
            └─ login_layout.py
            └─ login.py
       └─ page1
            └─ page1.py
       not_found_404.py
  └─ app.py
```

## License

- [MIT](LICENSE)

# Dash Charlotte Themes

Tools for easy and consistent styling.

Add them in Dash's `external_stylesheet` argument:

```python
from dash import Dash
import dash_labs as dl
import dash_bootstrap_components as dbc

from dash_charlotte import themes

app = Dash(
    name = __name__,
    title = 'Dash Charlotte',
    plugins = [dl.plugins.pages],
    external_stylesheets = [
        dbc.themes.BOOTSTRAP,
        themes.BOOTSTRAP,
        themes.BOXICONS,
        themes.FONTAWESOME,
        themes.CHARLOTTE_LIGHT
    ]
)
```

---

- Colors
    - [**Bootstrap**](https://github.com/GusFurtado/dash-charlotte/blob/main/dash_charlotte/themes/bootstrap.py)
    - [**Charlotte Dark**](https://github.com/GusFurtado/dash-charlotte/blob/main/dash_charlotte/themes/charlotte_dark.py)
    - [**Charlotte Light**](https://github.com/GusFurtado/dash-charlotte/blob/main/dash_charlotte/themes/charlotte_light.py)
    - [**Colorblind**](https://github.com/GusFurtado/dash-charlotte/blob/main/dash_charlotte/themes/colorblind.py)
    - [**Dracula**](https://github.com/GusFurtado/dash-charlotte/blob/main/dash_charlotte/themes/dracula.py)
- [**Fonts**](https://github.com/GusFurtado/dash-charlotte/blob/main/dash_charlotte/themes/fonts.py)
    - Fire Code
    - Montserrat
    - Nunito
    - Poppins
    - Roboto
- [**Icons**](https://github.com/GusFurtado/dash-charlotte/blob/main/dash_charlotte/themes/icons.py)
    - Bootstrap Icons
    - Boxicons
    - FontAwesome
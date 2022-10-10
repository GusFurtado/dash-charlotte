# Dash Charlotte Themes

Tools for easy and consistent styling.

Add them in Dash's `external_stylesheet` argument:

```python
from dash import Dash
import dash_bootstrap_components as dbc
from dash_charlotte import themes

app = Dash(
    name = __name__,
    title = 'Dash Charlotte',
    use_pages = True,
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

## Working with `Colors` objects

Import the color module corresponding to your dashboard theme and instanciate a `Color` object, which can be:

   - A default color. Usually red, orange, yellow, green, cyan, blue, purple or pink;
   - One of the eight shades of grey, from zero to seven, ordered by level of contrast with the theme background.

```python
from dash_charlotte.themes import charlotte_light as light

# Default colors
red = light.RED
blue = light.BLUE

# Shades of grey
white = light.SHADE0
grey = light.SHADE4
black = light.SHADE7
```

It is also possible to create a custom `Color` object.

```python
from dash_charlotte.themes import Color

firebrick = Color('#B22222')
midnight = Color('#191970')
```

Lastly, use the `__call__` method of the `Color` object to change the lightness of the color.

```python
red = light.RED
lighter_red = red(0.9)
darker_red = red(0.1)
```
---

## Working with CSS color classes

Simply pass the shade or color name to the className attribute of a Dash component. Add a `bg-*` prefix to change the background color.

```python
colorful_spans = [
    html.Span('Span 1', className='blue me-2'),
    html.Span('Span 2', className='shade0 bg-shade7')
]
```

---

## Working with Icons

After adding the icon package in the `external_stylesheets` argument of the Dash app, add a icon reference in the `className` atribute of an `html.I` component.

```python
from dash import Dash
from dash_charlotte import themes

app = Dash(
    __name__,
    external_stylesheets = [
        themes.FONTAWESOME
        themes.BOXICONS,
        themes.BOOTSTRAP
    ]
)

app.layout = html.Div(
    id = 'icons-of-boxes',
    children = [
        html.I(className='bi bi-box'),
        html.I(className='bx bxs-box'),
        html.I(className='fas fa-box')
    ]
)
```

---

- Color Themes
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
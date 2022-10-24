# Dash Colors

Color palettes for easy and consistent styling.

---

## Working with `Colors` objects

Import the color module corresponding to your dashboard theme and instanciate a `Color` object, which can be:

   - A default color. Usually red, orange, yellow, green, cyan, blue, purple or pink;
   - One of the eight shades of grey, from zero to seven, ordered by level of contrast with the theme background.

```python
from colors import charlotte_light as light

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
from colors import Color

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

## Color themes

- [**Bootstrap**](https://github.com/GusFurtado/dash-charlotte/blob/main/dash_charlotte/themes/bootstrap.py)
- [**Charlotte Dark**](https://github.com/GusFurtado/dash-charlotte/blob/main/dash_charlotte/themes/charlotte_dark.py)
- [**Charlotte Light**](https://github.com/GusFurtado/dash-charlotte/blob/main/dash_charlotte/themes/charlotte_light.py)
- [**Colorblind**](https://github.com/GusFurtado/dash-charlotte/blob/main/dash_charlotte/themes/colorblind.py)
- [**Dracula**](https://github.com/GusFurtado/dash-charlotte/blob/main/dash_charlotte/themes/dracula.py)

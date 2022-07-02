# Dash Charlotte Components

A set of standard Dash components for a fast and modular dashboard building.

- [**Box**](https://github.com/GusFurtado/dash-charlotte/blob/main/dash_charlotte/components/box.py): A formatted wrapper for miscellaneous content.
- [**Dashboard**](https://github.com/GusFurtado/dash-charlotte/blob/main/dash_charlotte/components/dashboard.py): Main component that holds a drawer, a navbar and the page content.
- [**Drawer**](https://github.com/GusFurtado/dash-charlotte/blob/main/dash_charlotte/components/drawer.py): The side-navigation bar.
- [**Footer**](https://github.com/GusFurtado/dash-charlotte/blob/main/dash_charlotte/components/footer.py): A discrete footer.
- [**Navbar**](https://github.com/GusFurtado/dash-charlotte/blob/main/dash_charlotte/components/navbar.py): Standard navbar with a button to open the drawer.
- [**Table**](https://github.com/GusFurtado/dash-charlotte/blob/main/dash_charlotte/components/table.py): HTML Table creation helper.

```python
from dash import (
    Dash,
    html,
    page_container
)

from dash_chatlotte import themes
from dash_charlotte.components import (
    Dashboard,
    Drawer,
    Navbar
)


app = Dash(
    __name__,
    external_stylesheets = [
        themes.CHARLOTTE_LIGHT,
        themes.BOXICONS,
        themes.FONTAWESOME
    ]
)

app.layout = Dashboard(
    children = page_container,
    navbar = Navbar(title='Navbar'),
    drawer = Drawer(
        logo_name = 'Dash Charlotte',
        logo_icon = 'fas fa-rocket'
    )
)
```
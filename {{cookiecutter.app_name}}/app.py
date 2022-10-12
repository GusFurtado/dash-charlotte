from dash import Dash, page_container
import dash_bootstrap_components as dbc

from components import (
    Dashboard,
    Drawer,
    DrawerSingleItem,
    DrawerMultiItem,
    DrawerSubItem,
    DrawerFooter,
    Navbar
)



app = Dash(
    name = __name__,
    title = '{{cookiecutter.app_name}}',
    use_pages = True,
    external_stylesheets = [
        dbc.themes.BOOTSTRAP
    ]
)



nav_links = [
    DrawerSingleItem(
        name = 'Login',
        icon = 'bx:log-in',
        href = '/login'
    ),
    DrawerSingleItem(
        name = 'Page 1',
        icon = 'bx:scatter-chart',
        href = '/page1'
    ),
    DrawerMultiItem(
        name = 'Page2',
        icon = 'bx:line-chart',
        href = '/page2/subpage1',
        submenu = [
            DrawerSubItem(
                name = 'Subpage 1',
                href = '/page2/subpage1'
            ),
            DrawerSubItem(
                name = 'Subpage 2',
                href = '/page2/subpage2'
            )
        ]
    ),
    DrawerFooter(
        title = 'Footer',
        subtitle = 'Footer Subtitle'
    )
]



app.layout = Dashboard(
    children = page_container,
    navbar = Navbar(
        title = '{{cookiecutter.app_name}}'
    ),
    drawer = Drawer(
        menu = nav_links,
        logo_name = 'Charlotte',
        logo_icon = 'heroicons:rocket-launch-20-solid'
    )
)



server = app.server
if __name__ == '__main__':
    app.run_server(
        host = '0.0.0.0',
        port = {{cookiecutter.port}}
    )

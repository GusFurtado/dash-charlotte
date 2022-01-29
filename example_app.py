from dash import Dash
import dash_bootstrap_components as dbc
import dash_labs as dl
import plotly.io as pio

from dash_charlotte.components import (
    BOXICONS,
    Dashboard,
    Drawer,
    DrawerSingleItem,
    DrawerMultiItem,
    DrawerSubItem,
    Navbar
)



app = Dash(
    name = __name__,
    title = 'Dash Charlotte',
    plugins=[dl.plugins.pages],
    external_stylesheets = [
        BOXICONS,
        dbc.themes.GRID
    ]
)



pio.templates.default = 'plotly_white'



nav_links = [
    DrawerSingleItem(
        name = 'Page 1',
        icon = 'bx bx-pie-chart-alt-2',
        href = '/page1'
    ),
    DrawerSingleItem(
        name = 'Page 2',
        icon = 'bx bx-line-chart',
        href = '/page2'
    ),
    DrawerSingleItem(
        name = 'Dashboard',
        icon = 'bx bx-grid-alt'
    ),
    DrawerMultiItem(
        name = 'Category',
        icon = 'bx bx-collection',
        submenu = [
            DrawerSubItem('HTML & CSS'),
            DrawerSubItem('JavaScript'),
            DrawerSubItem('PHP & MySQL')
        ]
    ),
    DrawerMultiItem(
        name = 'Posts',
        icon = 'bx bx-book-alt',
        submenu = [
            DrawerSubItem('Web Design'),
            DrawerSubItem('Login Form'),
            DrawerSubItem('Card Design')
        ]
    ),
    DrawerMultiItem(
        name = 'Plugins',
        icon = 'bx bx-plug',
        submenu = [
            DrawerSubItem('UI Face'),
            DrawerSubItem('Pigments'),
            DrawerSubItem('Box Icons')
        ]
    ),
    DrawerSingleItem(
        name = 'Explore',
        icon = 'bx bx-compass'
    ),
    DrawerSingleItem(
        name = 'History',
        icon = 'bx bx-history'
    ),
    DrawerSingleItem(
        name = 'Setting',
        icon = 'bx bx-cog'
    )
]



LOGO_IMG = 'https://upload.wikimedia.org/wikipedia/commons/a/ab/Logo_TV_2015.png'
LOGO_ICON = 'bx bxl-c-plus-plus'



app.layout = Dashboard(
    children = dl.plugins.page_container,
    navbar = Navbar(
        title = 'Navbar'
    ),
    drawer = Drawer(
        menu = nav_links,
        logo_name = 'Charlotte',
        #logo_icon = LOGO_ICON,
        logo_img = LOGO_IMG
    )
)



if __name__ == '__main__':
    app.run_server()

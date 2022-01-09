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
        link_name = 'Dashboard',
        icon = 'bx bx-grid-alt'
    ),
    DrawerMultiItem(
        link_name = 'Category',
        icon = 'bx bx-collection',
        submenu = ['HTML & CSS', 'JavaScript', 'PHP & MySQL']
    ),
    DrawerMultiItem(
        link_name = 'Posts',
        icon = 'bx bx-book-alt',
        submenu = ['Web Design', 'Login Form', 'Card Design']
    ),
    DrawerSingleItem(
        link_name = 'Analytics',
        icon = 'bx bx-pie-chart-alt-2'
    ),
    DrawerSingleItem(
        link_name = 'Chart',
        icon = 'bx bx-line-chart'
    ),
    DrawerMultiItem(
        link_name = 'Plugins',
        icon = 'bx bx-plug',
        submenu = ['UI Face', 'Pigments', 'Box Icons']
    ),
    DrawerSingleItem(
        link_name = 'Explore',
        icon = 'bx bx-compass'
    ),
    DrawerSingleItem(
        link_name = 'History',
        icon = 'bx bx-history'
    ),
    DrawerSingleItem(
        link_name = 'Setting',
        icon = 'bx bx-cog'
    )
]



app.layout = Dashboard(
    children = dl.plugins.page_container,
    navbar = Navbar(
        title = 'Teste de Navbar'
    ),
    drawer = Drawer(
        menu = nav_links,
        logo_name = 'Charlotte',
        logo_icon = 'bx bxl-c-plus-plus'
    )
)



if __name__ == '__main__':
    app.run_server()

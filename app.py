from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

from components import (
    BOXICONS,
    Dashboard,
    Drawer,
    DrawerSingleItem,
    DrawerMultiItem
)



app = Dash(
    name = __name__,
    external_stylesheets = [
        BOXICONS,
        dbc.themes.GRID
    ]
)



section = html.Section(
    className = 'home-section',
    children = [
        html.Div(
            className = 'home-content',
            children = [
                html.I(
                    className = 'bx bx-menu',
                    id = 'open-drawer'
                ),
                html.Span(
                    className = 'text',
                    children = 'Drop Down Sidebar'
                )
            ]
        ),
        html.Div(
            dcc.Graph(
                figure = go.Figure(
                    data = go.Scatter(
                        x = list('abcdefgh'),
                        y = [10,2,20,30,10,20,10,12],
                        mode = 'markers+lines'
                    ),
                    layout = {'paper_bgcolor': 'rgba(0,0,0,0)'}
                )
            )
        ),
        dbc.Row([
            dbc.Col(
                'Apenas um Teste Qualquer',
                style = {'background-color': 'lime'},
                width = 3
            ) for _ in range(4)
        ])
    ]
)



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
    children = section,
    drawer = Drawer(
        menu = nav_links,
        logo_name = 'Charlotte',
        logo_icon = 'bx bxl-c-plus-plus'
    )
)



app.run_server()

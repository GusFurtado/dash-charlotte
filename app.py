from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.io as pio

from components import (
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
    external_stylesheets = [
        BOXICONS,
        dbc.themes.GRID
    ]
)



pio.templates.default = 'plotly_white'



class Box(html.Div):
    def __init__(self, children=None):
        super().__init__(
            children = children,
            style = {
                'background-color': 'white',
                'margin': 20,
                'border-radius': 15,
                'box-shadow':' 5px 10px 8px #888888'
            }
        )



section = [
    dbc.Row([
        dbc.Col(
            Box(
                children = dcc.Graph(
                    figure = go.Figure(
                        data = go.Bar(
                            x = ['Banana', 'Laranja', 'Maçã', 'Acabaxi', 'Uva'],
                            y = [15, 10, 20, 18, 12]
                        ),
                        layout = {
                            'paper_bgcolor': 'rgba(0,0,0,0)',
                            'margin': {
                                't': 20, 'b': 20, 'l': 20, 'r': 20
                            }
                        }
                    )
                )
            ),
            width = 6
        ),
        dbc.Col(
            Box(
                children = dcc.Graph(
                    figure = go.Figure(
                        data = go.Scatter(
                            x = [19,10,11,17,16,16,20,7],
                            y = [10,2,20,30,10,20,10,12],
                            mode = 'markers',
                            marker = {
                                'size': 10,
                                'line': {
                                    'width': 2,
                                    'color': 'black'
                                }
                            }
                        ),
                        layout = {
                            'paper_bgcolor': 'rgba(0,0,0,0)',
                            'margin': {
                                't': 20, 'b': 20, 'l': 20, 'r': 20
                            }
                        }
                    )
                )
            ),
            width = 6
        )
    ],
        className = 'g-0'
    )
]



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
    navbar = Navbar(
        title = 'Teste de Navbar'
    ),
    drawer = Drawer(
        menu = nav_links,
        logo_name = 'Charlotte',
        logo_icon = 'bx bxl-c-plus-plus'
    )
)



app.run_server()

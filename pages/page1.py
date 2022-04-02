import dash
from dash import dcc
import dash_bootstrap_components as dbc
import numpy as np
import plotly.graph_objects as go

from dash_charlotte.components import Box
import dash_charlotte.themes.charlotte_light as cl



dash.register_page(
    __name__,
    path = '/page1',
    title = 'Example Page 1'
)



COLORS = [
    str(cl.YELLOW),
    str(cl.ORANGE),
    str(cl.RED),
    str(cl.BLUE),
    str(cl.PURPLE)
]



layout = [
    dbc.Row([
        dbc.Col(
            Box(
                children = dcc.Graph(
                    figure = go.Figure(
                        data = go.Bar(
                            x = ['Banana', 'Orange', 'Apple', 'Blueberry', 'Grape'],
                            y = np.random.random(5),
                            marker_color = COLORS
                        ),
                        layout = {
                            'plot_bgcolor': 'rgba(0,0,0,0)',
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
                            x = np.random.randint(1,20,20),
                            y = np.random.randint(1,20,20),
                            mode = 'markers',
                            marker = {
                                'size': 10,
                                'color': np.random.choice(COLORS, 20),
                                'line': {
                                    'width': 2,
                                    'color': 'black'
                                }
                            }
                        ),
                        layout = {
                            'plot_bgcolor': 'rgba(0,0,0,0)',
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
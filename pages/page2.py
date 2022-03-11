import dash
from dash import dcc
import dash_bootstrap_components as dbc
import numpy as np
import plotly.graph_objects as go

from dash_charlotte.components import Box
import dash_charlotte.themes.charlotte_light as cl



dash.register_page(
    __name__,
    path = '/page2',
    title = 'Example Page 2'
)



COLORS = [
    str(cl.RED),
    str(cl.YELLOW),
    str(cl.ORANGE),
    str(cl.BLUE)
]



layout = [
    dbc.Row([
        dbc.Col(
            Box(
                children = dcc.Graph(
                    figure = go.Figure(
                        data = go.Scatter3d(
                            x = np.random.random(30),
                            y = 10 * np.random.random(30) - 5,
                            z = np.random.random(30) ** 2,
                            mode = 'markers',
                            marker_color = np.random.choice(COLORS, 30)
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
                        data = go.Pie(
                            labels = ['Apple', 'Banana', 'Orange', 'Blueberry'],
                            values = np.random.random(4),
                            marker = {
                                'colors': COLORS
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
from typing import Optional

from dash import html
import dash_bootstrap_components as dbc



class Footer(html.Footer):

    def __init__(
            self,
            left_text: Optional[str] = None,
            right_text: Optional[str] = None
        ):

        super().__init__(
            children = dbc.Row([
                dbc.Col(
                    children = left_text,
                    width = 'auto',
                    style = {'font-size': 14},
                    className = 'shade6'
                ),
                dbc.Col(
                    children = right_text,
                    width = 'auto',
                    style = {'font-size': 14},
                    className = 'shade6'
                )
            ],
                className = 'g-0 mt-4',
                justify = 'between',
                style = {'padding': 20}
            )
        )
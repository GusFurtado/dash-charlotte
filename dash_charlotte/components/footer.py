from typing import Optional
from uuid import uuid4

from dash import html
import dash_bootstrap_components as dbc



class Footer(html.Footer):
    """Default footer.

    Parameters
    ----------
    left_text : str | Dash Components, optional
        Content shown on the left side of the footer.
    rught_text : str | Dash Components, optional
        Content shown on the right side of the footer.
    id : str, optional
        Component id.

    Components IDs
    --------------
    {id}
        Main content (children).
    {id}--left
        Content of the left side of the footer.
    {id}--right
        Content of the right side of the footer.

    """

    def __init__(
            self,
            left_text: Optional[str] = None,
            right_text: Optional[str] = None,
            id: Optional[str] = None
        ):

        id = id or str(uuid4())

        super().__init__(
            id = id,
            children = dbc.Row([
                dbc.Col(
                    children = left_text,
                    id = f'{id}--left',
                    width = 'auto',
                    style = {'font-size': 14},
                    className = 'shade6'
                ),
                dbc.Col(
                    children = right_text,
                    id = f'{id}--right',
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

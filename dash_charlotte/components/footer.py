from typing import Optional
from uuid import uuid4

from dash import html
from dash.development.base_component import Component



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
            left_text: Optional[Component] = None,
            right_text: Optional[Component] = None,
            id: Optional[str] = None
        ):

        id = id or str(uuid4())

        super().__init__(
            id = id,
            children = html.Div([
                html.Span(
                    children = left_text,
                    id = f'{id}--left',
                    style = {'font-size': 14},
                    className = 'shade6'
                ),
                html.Span(
                    children = right_text,
                    id = f'{id}--right',
                    style = {'font-size': 14},
                    className = 'shade6'
                )
            ],
                style = {
                    'display': 'flex',
                    'justify-content': 'space-between',
                    'margin-top': '1.5rem',
                    'padding': '1.2rem'
                }
            )
        )

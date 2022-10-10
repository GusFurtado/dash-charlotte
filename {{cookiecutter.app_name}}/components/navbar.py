from typing import Optional
import uuid

from dash import html
from dash.development.base_component import Component



class Navbar(html.Nav):
    def __init__(
            self,
            title: Component,
            children: Optional[Component] = None,
            id: Optional[str] = None
        ):
        """Navbar components.

        Parameters
        ----------
        title : str | Dash Component
            Text displayed inside the navbar.
        children : Dash Component, optional
            Content in the right of the navbar.
        id : str, optional
            Component's ID.

        Components IDs
        --------------
        {id}--title
            Navbar title.
        {id}--children
            Content in the right of the navbar.
        
        """

        id = id or str(uuid.uuid4())

        super().__init__(
            className = 'home-content shade7',
            children = [
                html.I(
                    className = 'fas fa-bars',
                    id = 'open-drawer'
                ),
                html.Span(
                    children = [
                        html.Span(
                            className = 'text',
                            children = title,
                            id = f'{id}--title'
                        ),
                        html.Span(
                            className = 'text',
                            children = children,
                            id = f'{id}--children'
                        )
                    ],
                    style = {
                        'width': '100%',
                        'display': 'flex',
                        'justify-content': 'space-between'
                    }
                )
            ]
        )

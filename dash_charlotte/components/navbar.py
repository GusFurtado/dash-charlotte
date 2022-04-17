from typing import Optional, Union
import uuid

from dash import html
from dash.development.base_component import Component



class Navbar(html.Nav):
    def __init__(
            self,
            title: Union[str, Component],
            id: Optional[str] = None
        ):
        """Navbar components.

        Parameters
        ----------
        title : str | Dash Component
            Text displayed inside the navbar.
        id : str, optional
            Component's ID.
        
        """

        super().__init__(
            className = 'home-content shade7',
            children = [
                html.I(
                    className = 'fas fa-bars',
                    id = 'open-drawer'
                ),
                html.Span(
                    className = 'text',
                    children = title,
                    id = id or str(uuid.uuid4())
                )
            ]
        )

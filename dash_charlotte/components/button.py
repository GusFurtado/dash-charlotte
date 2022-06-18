from typing import Optional

from dash import html
from dash.development.base_component import Component



class Button(html.Button):
    """A button using Marko Denic's design.

    Parameters
    ----------
    children : Dash Components, optional
        Content of the button.
    type : {'arrow', 'shadow'}, default='shadow'
        One of the types of buttons.
    color : str
        Background color.
    **button_kwargs
        Any argument of a `dash.html.Button` component.

    References
    ----------
    .. [1] https://markodenic.com/tools/buttons-generator/

    """

    def __init__(
            self,
            children: Optional[Component] = None,
            type: str = 'shadow',
            color: str = 'blue',
            **button_kwargs
        ):
        
        className = f'css-button-{type} bg-{color} '
        if 'className' in button_kwargs:
            className += button_kwargs['className']
            button_kwargs.pop('className')

        super().__init__(
            children = children,
            className = className,
            **button_kwargs
        )

from typing import Optional
from uuid import uuid4

from dash import html



class Box(html.Div):
    """Default box.

    Parameters
    ----------
    children : Dash component | list of Dash components, optional
        Main content of the box.
    title : Dash component | list of Dash components, optional
        Box title.
    subtitle : Dash component | list of Dash components, optional
        Box subtitle.
    title_color : str, default='blue'
        Title color.
    title_style : dict[str, str], optional
    icon : str, optional
        Icon next to the title.
    header_content : Dash component | list of Dash components, optional
        Content on the upper right of the box.
    style : dict[str, str], optional
        Style of the box.
    padding : float, default=10
        Level of spacing between components.
    id : str, optional
        Component id.

    Components IDs
    --------------
    {id}
        Main content (children).
    {id}--title
        Title of the box.
    {id}--subtitle
        Subtitle of the box.
    {id}--title-style
        Style of the box title.
    {id}--header-content
        Content on the upper right of the box.

    """

    def __init__(
            self,
            children = None,
            title = None,
            subtitle = None,
            title_color: str = 'blue',
            title_style: Optional[dict] = None,
            icon: Optional[str] = None,
            header_content = None,
            style: Optional[dict] = None,
            padding: float = 10,
            id: Optional[str] = None
        ):

        id = id or str(uuid4())

        box_style = {
            'border-radius': 10,
            'margin': 10
        }

        if isinstance(style, dict):
            box_style.update(style)

        super().__init__(
            style = box_style,
            className = 'bg-shade0 shadow',
            children = [
                self.header(
                    title = title,
                    subtitle = subtitle,
                    title_color = title_color,
                    title_style = title_style,
                    icon = icon,
                    header_content = header_content,
                    padding = padding,
                    id = id
                ),
                self.content(
                    content = children,
                    padding = padding,
                    id = id
                )
            ]
        )


    def header(
            self,
            title,
            subtitle,
            title_color,
            title_style,
            icon,
            header_content,
            padding,
            id
        ) -> html.Div:

        title = html.Span(
            title,
            id = f'{id}--title'
        )

        subtitle = html.Span(
            children = subtitle,
            id = f'{id}--subtitle',
            className = 'shade4',
            style = {
                'font-size': 16
            }
        )

        if icon is not None:
            icon = html.I(
                className = f'{icon} me-2',
                id = f'{id}--icon'    
            )

        header_content = html.Div(
            children = header_content,
            id = f'{id}--header-content'
        )

        style = {
            'font-size': 22,
            'font-weight': 'bold'
        }
        if title_style is not None:
            style.update(title_style)

        title_stuff = html.Div([
            html.Div(
                children = [icon, title],
                className = title_color,
                style = style,
                id = f'{id}--title-style'
            ),
            subtitle
        ])

        return html.Div(
            children = [
                title_stuff,
                header_content
            ],
            style = {
                'display': 'flex',
                'justify-content': 'space-between',
                'padding': f'{padding}px {2*padding}px'
            }
        )


    def content(self, content, padding, id) -> html.Div:
        return html.Div(
            children = content,
            id = id,
            style = {
                'padding': 2 * padding,
                'padding-top': padding
            }
        )

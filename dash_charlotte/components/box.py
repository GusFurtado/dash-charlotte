from typing import Optional

from dash import html



class Box(html.Div):
    """Simple box.

    Subclass of dash.html.Div.
    
    """

    def __init__(
            self,
            children = None,
            title = None,
            subtitle = None,
            icon: Optional[str] = None,
            header_content = None,
            style: Optional[dict] = None,
            padding: float = 10
        ):

        box_style = {
            'background-color': 'white',
            'border-radius': 10,
            'box-shadow': '5px 10px 8px #888888',
            'margin': 10
        }

        if isinstance(style, dict):
            box_style.update(style)

        super().__init__(
            style = box_style,
            children = [
                self.header(
                    title = title,
                    subtitle = subtitle,
                    icon = icon,
                    content = header_content,
                    padding = padding
                ),
                self.content(
                    content = children,
                    padding = padding
                )
            ]
        )


    def header(
            self,
            title,
            subtitle,
            icon,
            content,
            padding
        ) -> html.Div:

        if title is not None:
            title = html.Span(title)

        if subtitle is not None:
            subtitle = html.Span(
                children = subtitle,
                className = 'shade4',
                style = {
                    'font-size': 16
                }
            )

        if icon is not None:
            icon = html.I(className=f'{icon} me-2')

        if content is not None:
            content = html.Div(content)

        title_stuff = html.Div([
            html.Div(
                children = [icon, title],
                className = 'blue',
                style = {
                    'font-size': 22,
                    'font-weight': 'bold'
                }
            ),
            subtitle
        ])

        return html.Div(
            children = [
                title_stuff,
                content
            ],
            style = {
                'display': 'flex',
                'justify-content': 'space-between',
                'padding': f'{padding}px {2*padding}px'
            }
        )


    def content(self, content, padding) -> html.Div:
        return html.Div(
            children = content,
            style = {
                'padding': 2 * padding,
                'padding-top': padding
            }
        )

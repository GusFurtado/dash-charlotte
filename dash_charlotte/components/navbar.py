from dash import html



class Navbar(html.Nav):
    def __init__(self, title:str):
        super().__init__(
            className = 'home-content shade7',
            children = [
                html.I(
                    className = 'bx bx-menu',
                    id = 'open-drawer'
                ),
                html.Span(
                    className = 'text',
                    children = title
                )
            ]
        )

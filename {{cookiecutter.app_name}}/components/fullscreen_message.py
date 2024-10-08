from dash import html


class FullscreenMessage(html.Div):
    """Layout for fullscreen messages.

    Parameters
    ----------
    top_message : str | list of Dash components
        Main text of the page.
    bottom_message : str | list of Dash components
        Subtext of the page.
    src : str
        Image source.
    color : str, default='blue'
        Color class of the top message.

    """

    def __init__(
        self,
        top_message: str,
        bottom_message: str,
        src: str,
        color: str = "blue",
    ):

        super().__init__(
            children=html.Div(
                [
                    html.H1(children=top_message, className=color),
                    html.H4(children=bottom_message, className="shade6"),
                    html.Img(
                        src=src,
                        height=300,
                        style={"max-width": "100%", "margin-top": 20},
                    ),
                ]
            ),
            style={
                "display": "flex",
                "justify-content": "center",
                "align-items": "center",
                "text-align": "center",
                "min-height": "90vh",
            },
        )

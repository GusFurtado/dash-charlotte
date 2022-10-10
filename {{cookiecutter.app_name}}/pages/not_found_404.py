from dash import (
    html,
    register_page
)



register_page(
    __name__,
    path = '/',
    title = '404 - Not Found'
)



class NotFound404(html.Div):
    """Layout for 404 error page.

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
            color: str = 'blue'
        ):

        super().__init__(
            children = html.Div([
                html.H1(
                    children = top_message,
                    className = color
                ),
                html.H4(
                    children = bottom_message,
                    className = 'shade6 mb-3'
                ),
                html.Img(
                    src = src,
                    height = 300,
                    style = {'max-width': '100%'}
                )
            ]),
            style = {
                'display': 'flex',
                'justify-content': 'center',
                'align-items': 'center',
                'text-align': 'center',
                'min-height': '90vh'
            }
        )



layout = NotFound404(
    top_message = 'Page Not Found',
    bottom_message = 'Use the sidebar to navigate',
    src = '/assets/img/not_found_404.svg'
)

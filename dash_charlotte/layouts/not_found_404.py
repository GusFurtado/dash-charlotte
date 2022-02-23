from dash import html



class NotFound404(html.Div):
    def __init__(self, top_message, bottom_message):
        super().__init__(
            children = html.Div([
                html.H2(
                    children = top_message,
                    className = 'blue'    
                ),
                html.H3(
                    children = bottom_message,
                    className = 'shade7 mb-3'
                ),
                html.Img(
                    src = '/assets/img/not_found_404.svg',
                    height = 300
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

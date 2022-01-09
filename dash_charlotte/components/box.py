from dash.html import Div



class Box(Div):
    """Simple box.

    Subclass of dash.html.Div.
    
    """

    def __init__(self, **kwargs):
        super().__init__(
            style = {
                'background-color': 'white',
                'margin': 20,
                'border-radius': 10,
                'box-shadow':' 5px 10px 8px #888888'
            },
            **kwargs
        )
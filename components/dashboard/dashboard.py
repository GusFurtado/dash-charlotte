from dash.html import Div



class Dashboard(Div):
    def __init__(
            self,
            children = None,
            navbar = None,
            drawer = None
        ):

        super().__init__(
            children = [
                navbar,
                drawer,
                children
            ]
        )

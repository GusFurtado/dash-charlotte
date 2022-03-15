from dash import dcc, html
from dash_bootstrap_components import Container



class Dashboard(Container):
    """Container principal da aplicação.

    Parameters
    ----------
    children : Dash component | list of Dash components, optional
        The container main content.
    navbar : dash_charlotte.Navbar, optional
        Navbar added at the top of the dashboard.
    drawer : dash_charlotte.Drawer, optional
        The dashboard sidenav.
    id : str, default='dashboard'
        Dashboard ID.

    Components IDs
    --------------
    {id}
        Container principal.
    {id}--data
        Componente para armazenamento de dados.
    {id}--location
        Componente que gerencia a URL da página.

    """

    def __init__(
            self,
            children = None,
            navbar = None,
            drawer = None,
            id: str = 'dashboard'
        ):

        if not isinstance(children, list):
            children = [children]

        super().__init__(
            id = id,
            fluid = True,
            className = 'dashboard-container shade7',
            children = [
                dcc.Location(id=f'{id}--location'),
                dcc.Store(id=f'{id}--data'),
                drawer,
                html.Section(
                    className = 'home-section',
                    children = [navbar] + children
                )
            ]
        )

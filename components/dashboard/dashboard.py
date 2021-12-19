from dash import dcc, html



class Dashboard(html.Div):
    """Container principal da aplicação.

    Parameters
    ----------
    children : Dash component | list of Dash components, optional
        Conteúdo do container.
    navbar : dash_charlotte.Navbar, optional
        Objeto Navbar que será adicionado ao Dashboard.
    drawer : dash_charlotte.Drawer, optional
        Objeto Drawer que será adicionado ao Dashboard.
    id : str, default='dashboard'
        ID do Dashboard.

    Components IDs
    --------------
    {id}
        Container principal.
    {id}-data
        Componente para armazenamento de dados.
    {id}-location
        Componente que gerencia a URL da página.

    """

    def __init__(
            self,
            children = None,
            navbar = None,
            drawer = None,
            id: str = 'dashboard'
        ):

        super().__init__(
            id = id,
            className = 'dashboard-container shade0',
            children = [
                dcc.Location(id=f'{id}-location'),
                dcc.Store(id=f'{id}-data'),
                navbar,
                drawer,
                children
            ]
        )

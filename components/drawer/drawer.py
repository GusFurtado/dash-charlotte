from typing import List
import uuid

from dash import html, callback, Input, Output, State, MATCH



class DrawerSingleItem(html.Li):
    def __init__(self, link_name:str, icon:str):
        super().__init__(
            children = [
                html.A(
                    href = '#',
                    children = [
                        html.I(className = f'{icon} shade7'),
                        html.Span(
                            className = 'link-name shade7',
                            children = link_name
                        )
                    ]
                ),
                html.Ul(
                    className = 'sub-menu blank bg-blue',
                    children = [
                        html.Li(
                            html.A(
                                className = 'link-name shade7',
                                href = '#',
                                children = link_name
                            )
                        )
                    ]
                )
            ]
        )



class DrawerMultiItem(html.Li):

    class ids:
        li = lambda aio_id: {
            'component': 'DrawerMultiLi',
            'subcomponent': 'Li',
            'aio_id': aio_id
        }
        arrow = lambda aio_id: {
            'component': 'DrawerMultiLi',
            'subcomponent': 'arrow',
            'aio_id': aio_id
        }
    ids = ids

    def __init__(
            self,
            link_name: str,
            icon: str,
            submenu: list,
            aio_id = None
        ):

        if aio_id is None:
            aio_id = str(uuid.uuid4())

        super().__init__(
            className = 'hideMenu',
            id = self.ids.li(aio_id),
            children = [
                html.Div(
                    className = 'iocn-link',
                    children = [
                        html.A(
                            href = '#',
                            children = [
                                html.I(className=f'{icon} shade7'),
                                html.Span(
                                    className = 'link-name shade7',
                                    children = link_name
                                )
                            ]
                        ),
                        html.I(
                            className = 'bx bxs-chevron-down arrow shade7',
                            id = self.ids.arrow(aio_id)
                        )
                    ]
                ),
                html.Ul(
                    className = 'sub-menu bg-blue',
                    children = [
                        html.Li(
                            html.A(
                                className = 'link-name shade7',
                                href = '#',
                                children = link_name
                            )
                        )
                    ] + [
                        html.Li(
                            html.A(
                                href = '#',
                                className = 'shade7',
                                children = subitem
                            )
                        ) for subitem in submenu
                    ]
                )
            ]
        )

    @callback(
        Output(ids.li(MATCH), 'className'),
        Input(ids.arrow(MATCH), 'n_clicks'),
        State(ids.li(MATCH), 'className'),
        prevent_initial_call = True)
    def open_li(_, state):
        if state == 'showMenu':
            return 'hideMenu'
        return 'showMenu'



class DrawerFooter(html.Li):
    def __init__(
            self,
            title: str,
            subtitle: str
        ):

        super().__init__(
            children = [
                html.Div(
                    className = 'profile-details bg-blue',
                    children = [
                        html.Div(
                            className = 'profile-content',
                            # children = html.Img(
                            #     src = 'image/profile.jpg',
                            #     alt = 'profileImg'
                            # )
                        ),
                        html.Div(
                            className = 'name-job',
                            children = [
                                html.Div(
                                    className = 'profile_name shade7',
                                    children = title
                                ),
                                html.Div(
                                    className = 'job shade7',
                                    children = subtitle
                                )
                            ]
                        ),
                        html.I(className='bx bx-log-out')
                    ]
                )
            ]
        )



class Drawer(html.Div):
    """Barra vertical de navegação.

    Parameters
    ----------
    menu : List of dash.html.Li
        Lista de DrawerItems.
    logo_name : str, optional
        Nome da logo.
    logo_icon : str, optional
        Ícone da logo.

    Notes
    -----
    Para abrir o Drawer, adicione ao layout um componente com ID 'open-drawer'
    que ativará o callback via `n_clicks`.

    """
    
    def __init__(
            self,
            menu: List[html.Li],
            logo_name: str = None,
            logo_icon: str = None
        ):

        if logo_name is None and logo_icon is None:
            logo = None
        else:
            logo = html.Div(
                className = 'logo-details shade7',
                children = [
                    html.I(className=logo_icon),
                    html.Span(
                        className = 'logo_name shade7',
                        children = logo_name
                    )
                ]
            )

        super().__init__(
            className = 'sidebar bg-shade0 close',
            id = 'drawer',
            children = [
                logo,
                html.Ul(
                    className = 'nav-links',
                    children = menu
                )
            ]
        )

    @callback(
        Output('drawer', 'className'),
        Input('open-drawer', 'n_clicks'),
        State('drawer', 'className'),
        prevent_initial_call = True)
    def click(_, state):
        if state == 'sidebar bg-shade0':
            return 'sidebar bg-shade0 close'
        return 'sidebar bg-shade0'

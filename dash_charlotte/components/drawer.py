from typing import List, Optional
import uuid

from dash import (
    html,
    callback,
    Input,
    Output,
    State,
    MATCH
)



class DrawerSingleItem(html.Li):
    """An item for the Drawer menu.
    
    Parameters
    ----------
    name : str
        Display name.
    icon : str
        Boxicon or Fontawesome icon code.
    href : str, default='#'
        Link reference.

    """

    def __init__(
            self,
            name: str,
            icon: str,
            href: str = '#'
        ):

        super().__init__(
            children = [
                html.A(
                    href = href,
                    children = [
                        html.I(className = f'{icon} shade7'),
                        html.Span(
                            className = 'link-name shade7',
                            children = name
                        )
                    ]
                ),
                html.Ul(
                    className = 'sub-menu blank bg-blue',
                    children = [
                        html.Li(
                            html.A(
                                className = 'link-name shade7',
                                href = href,
                                children = name
                            )
                        )
                    ]
                )
            ]
        )



class DrawerSubItem(html.Li):
    """An item for the DrawerMultiItem submenu.
    
    Parameters
    ----------
    name : str
        Display name.
    href : str, default='#'
        Link reference.

    """

    def __init__(
            self,
            name: str,
            **kwargs
        ):

        super().__init__(
            children = html.A(
                children = name,
                className = 'shade7',
                **kwargs
            )
        )



class DrawerMultiItem(html.Li):
    """An AIO component for the Drawer menu containing a submenu.

    Parameters
    ----------
    name : str
        Display name.
    icon : str
        Boxicon or Fontawesome icon code.
    submenu : list of dash_charlotte.components.drawer.DrawerSubitem
        A list of DrawerSubItem.
    aio_id : str
        AIO identification.
    href : str, default='#'
        Link reference.
    
    """

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
            name: str,
            icon: str,
            submenu: List[DrawerSubItem],
            aio_id: str = None,
            href: str = '#'
        ):

        aio_id = aio_id or str(uuid.uuid4())
        if not isinstance(submenu, list):
            submenu = [submenu]

        super().__init__(
            className = 'hideMenu',
            id = self.ids.li(aio_id),
            children = [
                html.Div(
                    className = 'iocn-link',
                    children = [
                        html.A(
                            href = href,
                            children = [
                                html.I(className=f'{icon} shade7'),
                                html.Span(
                                    className = 'link-name shade7',
                                    children = name
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
                                href = href,
                                children = name
                            )
                        )
                    ] + submenu
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
            title = None,
            subtitle = None,
            icon: str = 'bx bx-log-out',
            img_src: str = None
        ):

        super().__init__(
            children = [
                html.Div(
                    className = 'profile-details bg-blue',
                    children = [
                        html.Div(
                            className = 'profile-content',
                            children = html.Img(src=img_src)
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
                        html.I(className = f'{icon} shade7')
                    ]
                )
            ]
        )



class Drawer(html.Div):
    """Barra vertical de navegação.

    Parameters
    ----------
    menu : List of dash.html.Li
        Add a list of href icons.
    logo_name : str, optional
        Name displayed above the menu.
    logo_icon : str, optional
        Class name of the web icon.
    logo_img : str, optional
        Link of an image.

    Notes
    -----
    [1] To open the Drawer, add a component with 'open-drawer' as ID to your
        layout. Activete the callback by its `n_clicks` attribute.
    [2] You can only add one `logo_icon` or `logo_img` arguments.

    """
    
    def __init__(
            self,
            menu: List[html.Li],
            logo_name: Optional[str] = None,
            logo_icon: Optional[str] = None,
            logo_img: Optional[str] = None,
        ):

        # No logo at all
        if all(x is None for x in [logo_name, logo_icon, logo_img]):
            logo = None

        # Oops... You shouldn't choose both of them
        elif (logo_icon is not None) and (logo_img is not None):
            raise ValueError('One of `logo_icon` or `logo_img` must be `None`.')

        else:

            if logo_icon is not None:
                logo_i = html.I(className=logo_icon)
            elif logo_img is not None:
                logo_i = html.Span(
                    html.Img(src=logo_img),
                    className = 'logo_img_wrapper'
                )

            logo = html.Div(
                className = 'logo-details shade7',
                children = [
                    logo_i,
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
        cls = 'sidebar bg-shade0'
        if state == cls:
            return f'{cls} close'
        return cls

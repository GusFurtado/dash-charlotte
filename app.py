from dash import Dash, html

from components import (
    BOXICONS,
    Dashboard,
    Drawer,
    DrawerSingleLi,
    DrawerMultiLi
)



app = Dash(
    name = __name__,
    external_stylesheets = [BOXICONS]
)



section = html.Section(
    className = 'home-section',
    children = html.Div(
        className = 'home-content',
        children = [
            html.I(
                className = 'bx bx-menu',
                id = 'open-drawer'
            ),
            html.Span(
                className = 'text',
                children = 'Drop Down Sidebar'
            )
        ]
    )
)



nav_links = [
    DrawerSingleLi(
        link_name = 'Dashboard',
        icon = 'bx bx-grid-alt'
    ),
    DrawerMultiLi(
        link_name = 'Category',
        icon = 'bx bx-collection',
        submenu = ['Category', 'HTML & CSS', 'JavaScript', 'PHP & MySQL']
    ),
    DrawerMultiLi(
        link_name = 'Posts',
        icon = 'bx bx-book-alt',
        submenu = ['Posts', 'Web Design', 'Login Form', 'Card Design']
    ),
    DrawerSingleLi(
        link_name = 'Analytics',
        icon = 'bx bx-pie-chart-alt-2'
    ),
    DrawerSingleLi(
        link_name = 'Chart',
        icon = 'bx bx-line-chart'
    ),
    DrawerMultiLi(
        link_name = 'Plugins',
        icon = 'bx bx-plug',
        submenu = ['Plugins', 'UI Face', 'Pigments', 'Box Icons']
    ),
    DrawerSingleLi(
        link_name = 'Explore',
        icon = 'bx bx-compass'
    ),
    DrawerSingleLi(
        link_name = 'History',
        icon = 'bx bx-history'
    ),
    DrawerSingleLi(
        link_name = 'Setting',
        icon = 'bx bx-cog'
    )
]



app.layout = Dashboard(
    children = section,
    drawer = Drawer(
        title = 'Charlotte',
        menu = nav_links
    )
)



app.run_server()

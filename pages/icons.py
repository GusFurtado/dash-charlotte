from dash_charlotte.components import Box, Footer

from dash import register_page, html
from dash_bootstrap_components import Container



register_page(
    __name__,
    path = '/icons',
    title = 'Dash Charlotte Icons'
)



ICON_PACKAGES = {
    'Bootstrap': [
        'bi bi-bootstrap-fill',
        'bi bi-box',
        'bi bi-bug',
        'bi bi-cloud',
        'bi bi-basket',
        'bi bi-cart',
        'bi bi-bell',
        'bi bi-flag',
        'bi bi-trash',
        'bi bi-tags',
        'bi bi-alarm',
    ],
    'Boxicons': [
        'bx bxs-package',
        'bx bxs-box',
        'bx bxs-bug',
        'bx bxs-cloud',
        'bx bxs-basket',
        'bx bxs-cart',
        'bx bxs-bell',
        'bx bxs-flag',
        'bx bxs-trash',
        'bx bxs-purchase-tag-alt',
        'bx bxs-alarm',
    ],
    'FontAwesome': [
        'fas fa-flag',
        'fas fa-box',
        'fas fa-bug',
        'fas fa-cloud',
        'fas fa-shopping-basket',
        'fas fa-shopping-cart',
        'fas fa-bell',
        'fas fa-flag',
        'fas fa-trash-alt',
        'fas fa-tags',
        'fas fa-stopwatch'
    ]
}



def box(pack:dict) -> Box:

    icons = [html.I(
        className = icon,
        style = {
            'margin': 10,
            'height': 50,
            'width': 50,
            'text-align': 'center'
        }
    ) for icon in ICON_PACKAGES[pack][1:]]

    return Box(
        title = pack,
        icon = ICON_PACKAGES[pack][0],
        padding = 15,
        children = html.Div(
            children = icons,
            className = 'shade5',
            style = {'font-size': 50}
        )
    )



layout = Container(
    children = [
        html.Div(box(icon_pack)) for icon_pack in ICON_PACKAGES
    ] + [
        Footer(right_text = 'Dash Charlotte')
    ]
)

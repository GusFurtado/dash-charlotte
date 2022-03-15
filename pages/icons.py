from dash_charlotte.components import Box

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
        'bi bi-basket',
        'bi bi-box',
        'bi bi-bug',
        'bi bi-bell',
        'bi bi-cart',
        'bi bi-cloud',
        'bi bi-flag',
        'bi bi-trash-fill',
        'bi bi-alarm',
        'bi bi-tags-fill'
    ],
    'Boxicons': [
        'bx bxs-package',
        'bx bxs-alarm',
        'bx bxs-basket',
        'bx bxs-box',
        'bx bxs-bug',
        'bx bxs-cart',
        'bx bxs-bell',
        'bx bxs-cloud',
        'bx bxs-flag',
        'bx bxs-purchase-tag-alt',
        'bx bxs-lock-open-alt'
    ],
    'FontAwesome': [
        'fas fa-flag',
        'fas fa-box',
        'fas fa-bug',
        'fas fa-cloud',
        'fas fa-ghost',
        'fas fa-helicopter',
        'fas fa-anchor',
        'fas fa-bell',
        'fas fa-cat',
        'fas fa-chess-knight',
        'fas fa-charging-station'
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
    children = [html.Div(box(icon_pack)) for icon_pack in ICON_PACKAGES]
)

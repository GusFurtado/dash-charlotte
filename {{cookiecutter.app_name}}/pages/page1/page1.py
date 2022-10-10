from dash import (
    html,
    register_page
)



register_page(
    __name__,
    path = '/page1',
    title = 'Page 1'
)



layout = html.H1('Page 1')

from dash import register_page
from dash_charlotte.layouts.not_found_404 import NotFound404



register_page(
    __name__,
    path = '/',
    title = '404 - Not Found'
)



layout = NotFound404(
    top_message = 'Page Not Found',
    bottom_message = 'Use the sidebar to navigate'
)

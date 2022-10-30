from dash import register_page
from components.fullscreen_message import FullscreenMessage



register_page(
    __name__,
    title = 'Big Data - 403',
    path = '/forbidden'
)



layout = FullscreenMessage(
    top_message = 'Forbidden',
    bottom_message = 'Use the sidebar to navigate',
    src = '/assets/images/forbidden_403.svg'
)

from dash import register_page

from components.fullscreen_message import FullscreenMessage


register_page(
    module=__name__,
    path="/",
    title="404 - Not Found",
)


layout = FullscreenMessage(
    top_message="Page Not Found",
    bottom_message="Use the sidebar to navigate",
    src="/assets/img/not_found_404.svg",
)

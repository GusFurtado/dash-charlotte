from dash import html, register_page

from components import Box


register_page(
    module=__name__,
    path="/page1",
    title="Page 1",
)


layout = html.Div(
    children=Box(children="Content", title="Page 1"),
    style={"margin-top": 20},
)

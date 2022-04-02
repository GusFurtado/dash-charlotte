from dash import (
    register_page,
    dcc,
    html,
    Input,
    Output,
    State,
    callback
)
import dash_bootstrap_components as dbc

from dash_charlotte.components import Box



register_page(
    __name__,
    path = '/box',
    title = 'Dash Charlotte Box'
)



column1 = dbc.Col([
    dbc.Label(html.B('Title')),
    dbc.Input(
        id = 'input-title',
        value = 'Change title',
        type = 'text'
    ),
    html.Hr(),
    dbc.Label(html.B('Subtitle')),
    dbc.Input(
        id = 'input-subtitle',
        value = 'Change subtitle',
        type = 'text'
    )
])



column2 = dbc.Col([
    dbc.Label(html.B('Title Color')),
    dcc.Dropdown(
        value = 'blue',
        id = 'input-color',
        clearable = False,
        options = [
            {'label': c.title(), 'value': c} for c in [
                'blue', 'orange', 'yellow', 'green', 'cyan', 'purple', 'pink'
            ]
        ]
    ),
    html.Hr(),
    dbc.Label(html.B('Header Content')),
    dbc.Input(
        id = 'input-header-content',
        value = 'Edit header content',
        type = 'text'
    )
])



layout = dbc.Container(
    children = Box(
        children = dbc.Row([
            column1,
            column2
        ]),
        icon = 'bx bx-box',
        id = 'the-box'
    )
)



@callback(
    Output('the-box--title', 'children'),
    Input('input-title', 'value'))
def input_title(title):
    return title



@callback(
    Output('the-box--subtitle', 'children'),
    Input('input-subtitle', 'value'))
def input_subtitle(subtitle):
    return subtitle



@callback(
    Output('the-box--title-style', 'style'),
    Input('input-color', 'value'),
    State('the-box--title-style', 'style'))
def input_title(color, style):
    style['color'] = color
    return style



@callback(
    Output('the-box--header-content', 'children'),
    Input('input-header-content', 'value'))
def input_header_content(header_content):
    return header_content

from dash import (
    register_page,
    callback,
    Output,
    Input,
    State
)

from . import login_layout as ll



register_page(
    __name__,
    path = '/login',
    title = 'Log In'
)



left_panel = ll.LoginForm(
    id = 'login-form',
)

right_panel = ll.LoginSvgPanel(
    src = '/assets/img/register.svg',
    background = 'blue',
    padding = 50
)

layout = ll.LoginPage(
    left_panel = left_panel,
    right_panel = right_panel
)



@callback(
    Output('login-form--subtitle', 'children'),
    Input('login-form--button', 'n_clicks'),
    Input('login-form--password', 'value'),
    State('login-form--user', 'value'),
    prevent_initial_call = True)
def login(submit_click, password, user):

    # INSERT HERE YOUR AUTHENTICATION FUNCTIONS

    return 'Logged in!'

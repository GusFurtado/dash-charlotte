from dash import (
    register_page,
    callback,
    Output,
    Input,
    State
)

from dash_charlotte.layouts import login



register_page(
    __name__,
    path = '/login',
    title = 'Log In'
)



left_panel = login.LoginForm(
    id = 'login-form',
)

right_panel = login.SvgImage(
    src = '/assets/img/register.svg'
)

layout = login.LoginPage(
    left_panel = left_panel,
    right_panel = right_panel
)



@callback(
    Output('login-form--subtitle', 'children'),
    Input('login-form--button', 'n_clicks'),
    Input('login-form--password', 'value'),
    State('login-form--email', 'value'),
    prevent_initial_call = True)
def login(submit_click, password, email):
    return 'Logged in!'

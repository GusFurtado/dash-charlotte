from socket import gethostname

from dash import (
    register_page,
    callback,
    Output,
    Input,
    State,
    html,
    no_update
)

from . import login_layout as ll
from .login_auth import LoginAuth, LoginError



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
    right_panel = right_panel,
    id = 'login-page'
)



@callback(
    Output('login-page--location', 'href'),
    Output('login-form--subtitle', 'children'),
    Input('login-form--button', 'n_clicks'),
    Input('login-form--password', 'value'),
    State('login-form--user', 'value'),
    State('login-page--location', 'search'),
    prevent_initial_call = True)
def login(_, password, username, search):

    # Trying to authenticate
    try:
        LoginAuth(username, password)
        path = '/'.join(search.split('/')[1:])

    # Error on authentication
    except LoginError as err:
        return (
            no_update,
            html.Span([
                html.I(className = 'fas fa-times-circle me-2'),
                html.Span(str(err))
            ],
                className = 'red'
            )
        )

    # Default initial page
    except ValueError:
        path = 'page1'

    # Successfully authenticated
    return (
        f'http://{gethostname()}:{{cookiecutter.port}}/{path}',
        html.Span([
            html.I(className = 'fas fa-check-circle me-2'),
            html.Span('Logged in!')
        ],
            className = 'green'
        )
    )

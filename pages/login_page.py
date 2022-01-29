from dash import register_page

from dash_charlotte.layouts.login import LoginContainer



register_page(
    __name__,
    path = '/login',
    title = 'Log In'
)



layout = LoginContainer()
